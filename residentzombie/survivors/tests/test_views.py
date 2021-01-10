#from django.test import TestCase
from items.models import Survivors
from rest_framework.test import APIClient, APITestCase
from django.shortcuts import get_object_or_404
from django.http.response import Http404

class TestSurvivorsModel(APITestCase):
    def setUp(self):
        self.survivor = Survivors.objects.create(pk=1,name="TestPerson1",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
    #tests user creation via post request
    def test_user_creation(self):
        client = APIClient()
        r=self.client.post("/survivors/",{
            "name": "viktor",
            "age": 23,
            "gender": 0,
            "latitude": -11,
            "longitude": 23,
            "fiji_water": 0,
            "campbell_soup": 0,
            "first_aid_pouch": 0,
            "ak47": 0
        })
        self.assertEquals(get_object_or_404(Survivors,name="viktor").pk,2)

    #tests user location update via put request
    def test_user_alter_location(self):
        client = APIClient()
        r=self.client.put("/survivors/1/",{
            "latitude": -11,
            "longitude": 45,
            })

        self.assertEquals(get_object_or_404(Survivors,pk=1).latitude,-11)

    def test_user_deletion(self):
        client = APIClient()
        r=self.client.delete("/survivors/1/")

        r=self.client.get("/survivors/1/")

        self.assertEquals(r.status_code,404)
