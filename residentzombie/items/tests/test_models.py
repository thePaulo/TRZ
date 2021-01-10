#from django.test import TestCase
from items.models import Survivors,Item
from rest_framework.test import APIClient, APITestCase

class TestItemModel(APITestCase):
    def setUp(self):
        self.survivor = Survivors.objects.create(pk=1,name="TestPerson1",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=1,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        self.item = Item.objects.filter(pk=1).first()

    def test_item_owner_after_trade(self):

        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=35,gender=1,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=0,ak47=0)
        item2 = Item.objects.create(pk=2,name="fiji_water",points=14,owner=survivor2)

        client = APIClient()
        r= self.client.get("/trading",{'s1':'1','s2':'2'})
        self.item.refresh_from_db()
        self.assertEquals(self.item.owner.pk,survivor2.pk)

    def test_on_user_creation_nobjects_creation(self):
        survivor2 = Survivors.objects.create(pk=2,name="TestPerson2",age=15,gender=0,
                                                latitude=10,longitude=180,infected=0,
                                                fiji_water=0,campbell_soup=0,
                                                first_aid_pouch=5,ak47=0)

        num= len( Item.objects.filter(name='first_aid_pouch') )
        self.assertEquals(num,5)
