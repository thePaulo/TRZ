#from django.test import TestCase
from items.models import Survivors,Item
from rest_framework.test import APIClient, APITestCase

import json

class TestItemModel(APITestCase):
    def setUp(self):
        self.survivor = Survivors.objects.create(pk=1,name="TestPerson1",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=1,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        #self.item = Item.objects.create(pk=1,name="fiji_water",points=14,owner=self.survivor)
        self.item = Item.objects.filter(pk=1).first()

    def test_trade_not_matching_points(self):

        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=1,
                                                first_aid_pouch=0,ak47=0)

        client = APIClient()
        r= self.client.get("/trading",{'s1':'1','s2':'2'})
        self.item.refresh_from_db()

        self.assertEquals(r.status_code,403)

    def test_trade_items_different_survivor(self):
        Item.objects.create(name="fiji_water",points=14,owner=self.survivor)
        Item.objects.create(name="fiji_water",points=14,owner=self.survivor)

        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=4,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)

        client = APIClient()
        r= self.client.get("/trading",{'s1':'1 4','s2':'5 6'})

        self.assertEquals(r.status_code,403)

    #tests trade between two users via get request
    def test_trade_successful(self):
        Item.objects.create(name="fiji_water",points=14,owner=self.survivor)
        Item.objects.create(name="fiji_water",points=14,owner=self.survivor)
        Item.objects.create(name="fiji_water",points=14,owner=self.survivor)

        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=7)

        client = APIClient()
        r= self.client.get("/trading",{'s1':'1 2 3 4','s2':'5 6 7 8 9 10 11'})#56 pontos
        self.assertEquals(r.status_code,302)#usuario é redirecionado para pagina de itens para verificar a troca

    #tests trade with an infected user via get request
    def test_trade_on_infected(self):
        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=1,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        Survivors.objects.filter(pk=1).update(infected=1)
        self.survivor.refresh_from_db()
        client = APIClient()
        r= self.client.get("/trading",{'s1':'1','s2':'2'})
        self.assertEquals(r.status_code,403)
