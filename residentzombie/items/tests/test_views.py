
from items.models import Survivors,Item
from rest_framework.test import APIClient, APITestCase

class TestItemView(APITestCase):
    def setUp(self):
        self.survivor = Survivors.objects.create(pk=1,name="TestPerson1",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        self.item = Item.objects.create(pk=1,name="fiji_water",points=14,owner=self.survivor)
        Survivors.objects.filter(pk=1).update(fiji_water=1)

    def test_list_item_view(self):
        client = APIClient()
        r= self.client.get("/items/")
        self.assertEquals(r.status_code,200)


    def test_detail_item_view(self):
        client = APIClient()
        r=self.client.get("/items/1/")
        self.assertEqual(r.status_code,200)

    def test_not_created_detail_item_view(self):
        client = APIClient()
        r=self.client.get("/items/2/")
        self.assertEquals(r.status_code,404)

    def test_cannot_create_item(self):
        client = APIClient()
        r=self.client.post("/items/",{
            "id": 3333,
            "name": "ak47",
            "points": 8,
            "owner": 1
        })

        self.assertEquals(r.status_code,405)

    def test_cannot_create_item(self):
        client = APIClient()
        r=self.client.delete("/items/1/")

        self.assertEquals(r.status_code,405)
