
from items.models import Survivors,Item
from rest_framework.test import APIClient, APITestCase
import json

class TestModel1(APITestCase):
    def setUp(self):
        self.survivor = Survivors.objects.create(pk=1,name="TestPerson1",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=1,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        #self.item = Item.objects.create(pk=1,name="fiji_water",points=14,owner=self.survivor)
        Survivors.objects.filter(pk=1).update(fiji_water=1)

    def test_view(self):
        client = APIClient()
        r=self.client.get("/reports")
        self.assertEquals(r.status_code,200)

    def test_water_item_amt(self):
        jsonResp = self.apiClientRequest()
        self.assertEquals(jsonResp["water_mean"],1)

    def test_infected_percent_update(self):
        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        Survivors.objects.filter(pk=2).update(infected=1)
        self.survivor.refresh_from_db()
        survivor2.refresh_from_db()

        jsonResp=self.apiClientRequest()

        self.assertEquals(jsonResp["infected_percent"],50.0)

    def test_item_percent_after_infection(self):
        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=4,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)

        Survivors.objects.filter(pk=2).update(infected=1)
        survivor2.refresh_from_db()

        jsonResp=self.apiClientRequest()

        self.assertEquals(jsonResp["water_mean"],0.5)

    #tests amount of points lost due to infected survivors
    def test_lost_points(self):
        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=4,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)

        Survivors.objects.filter(pk=2).update(infected=1)
        survivor2.refresh_from_db()

        jsonResp=self.apiClientRequest()

        self.assertEquals(jsonResp["lost_points"],56)

    def apiClientRequest(self):
        client = APIClient()
        r=self.client.get("/reports")
        jsonResp=json.loads(r.content)

        return jsonResp
