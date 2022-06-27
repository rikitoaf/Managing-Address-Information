import unittest
from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse, resolve
from .views import *
from rest_framework.test import APITestCase, APIClient
from address.models import *
# Create your tests here.


class ApiUrlsTests(SimpleTestCase):
    
    def test_get_parents_is_resolved(self): #test 1
        url = reverse('parent') 
        print(url)
        #testing urls function's origin is same as expected or not
        self.assertEquals(resolve(url).func.view_class,ParentViewSet)

class ApiViewTests(TestCase): # for parent
    parent_url = reverse('parent')
    client = Client()

    def test_success_children_link(self):
        client = Client()
        response = client.get('/children/')
        self.assertEqual(response.status_code, 200)   

    def setUp(self):
        Parent.objects.create(first_name = "Tokbuk",
        last_name = "Bakir",
        email_name = "17201039@gmail.edu",
        phone_num = "+88015210515",
        address_name = "101/2")
    
    def test (self):
        parent = Parent.objects.get(first_name='Tokbuk')
        
        self.assertEqual(parent.first_name,'Tokbuk')

    # def test2 (self):
    #     response = self.client.delete(self.parent_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test1(self):
        client = Client()
        response = client.get('/parent/')
        self.assertEqual(response.status_code, 200)
    
    def test2 (self): #checking create object feedback
        data ={
        
        "first_name": "Zadul",
        "last_name": "Bakib",
        "email_name": "17201039@gmail.edu",
        "phone_num": "+88015210515",
        "address_name": "101/2 A "
    }
        
        response = self.client.post(self.parent_url, data, format = 'json')
        print (response.status_code)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class ApiViewTests2(TestCase): 

    client = Client()
    child_url = reverse('children')
        # response = client.get('/children/')
    data ={
            
            "parent_name": 5 ,
            "first_name": "Baddul",
            "last_name": "Bakib"

    }

    def test1 (self): #checking status of child url
        client = Client()

        response = self.client.get(self.child_url)
        print (response.status_code)
        self.assertEqual(response.status_code,200)
