#from django.test import TestCase
from items.models import Survivors
from rest_framework.test import APIClient, APITestCase
from django.shortcuts import get_object_or_404

import json

class TestSurvivorsModel(APITestCase):
    def setUp(self):
        self.survivor = Survivors.objects.create(pk=1,name="TestPerson1",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)

    def infect(self,pk):
        Survivors.objects.filter(pk=pk).update(infected=1)
        surv = get_object_or_404(Survivors,pk=pk)
        surv.save()
        surv.refresh_from_db()

    #udates user infection via put
    def test_infection(self):
        client = APIClient()
        r=self.client.put("/survivors/1/",{
            "infected": "1",
        })
        Survivors.objects.filter(pk=1).first().refresh_from_db()

        self.assertEquals(get_object_or_404(Survivors,pk=1).infected,1)

    #survivors from 2 to 6 will be infected, then, the base survivor (nº1) will become infected.
    def test_five_infected_survivors_effect(self):

        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        survivor3 = Survivors.objects.create(pk=3,name="TestPerson3",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        survivor4 = Survivors.objects.create(pk=4,name="TestPerson4",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        survivor5 = Survivors.objects.create(pk=5,name="TestPerson5",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        survivor6 = Survivors.objects.create(pk=6,name="TestPerson6",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)

        for x in range(2,7):
            self.infect(x)

        client = APIClient()
        r=self.client.get("/reports")
        jsonResp=json.loads(r.content)

        self.survivor.refresh_from_db()
        self.assertEquals(self.survivor.infected,1)
