from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from widget.models import Widget
from datetime import datetime, timedelta
from widget.serializers import WidgetSerializer
import time


#############################
###       UNIT TEST       ###
###        CASES          ###
#############################
class WidgetTest(TestCase):
    """
    Test module for Widget Model
    """

    def setUp(self):
        Widget.objects.create(name="Folders", parts=10)
        Widget.objects.create(name="Settings", parts=15)

    def test_time(self):
        folders = Widget.objects.get(name="Folders")
        settings = Widget.objects.get(name="Settings")
        
        # Test that the creation time 
        present = datetime.now()
        self.assertLessEqual(folders.created.isoformat(), present.isoformat())
        self.assertLessEqual(settings.created.isoformat(), present.isoformat())

        # Test that Update and Create time are initially the same
        delta = timedelta(seconds=1)
        self.assertAlmostEqual(folders.created, folders.updated, delta=delta)
        self.assertAlmostEqual(settings.created, settings.updated, delta=delta)



#############################
###   FUNCTIONAL TEST     ###
###        CASES          ###
#############################
class WidgetCreateTestCase(APITestCase):
    def test_create_widget(self):
        initial_widget_count = Widget.objects.count()
        widget_attrs = {
            'name': "New Widget",
            'parts': 10,
        }
        response = self.client.post('/widgets/', widget_attrs)
        if response.status_code == status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(
            Widget.objects.count(), 
            initial_widget_count + 1
        )

        for attr, expected_value in widget_attrs.items():
            self.assertEqual(response.data[attr], expected_value)


class WidgetDestroyTestCase(APITestCase):

    def setUp(self):
        self.folders = Widget.objects.create(name='Folders', parts='32')
        self.settings = Widget.objects.create(name='Settings', parts='21')


    def test_delete_widget(self):
        # Confirm the DB contains 2 objects
        initial_widget_count = Widget.objects.count()
        self.assertEqual(initial_widget_count, 2)

        widget_id = Widget.objects.first().id

        # Delete the first widget
        response = self.client.delete(f'/widgets/{widget_id}/')
        self.assertEqual(
            Widget.objects.count(), 
            initial_widget_count - 1
        )
        self.assertRaises(
            Widget.DoesNotExist, 
            Widget.objects.get, id=widget_id
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class WidgetListTestCase(APITestCase):

    def setUp(self):
        self.folders = Widget.objects.create(name='Folders', parts='32')
        self.settings = Widget.objects.create(name='Settings', parts='21')
    
    def test_list_widgets(self):
        # Confirm the DB contains 2 objects
        initial_widget_count = Widget.objects.count()
        self.assertEqual(initial_widget_count, 2)
        # get API response
        response = self.client.get('/widgets/')
        
        # get data from the db
        widgets = Widget.objects.all()
        serializer = WidgetSerializer(widgets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WidgetUpdateTestCase(APITestCase):
    def setUp(self):
        self.folders = Widget.objects.create(name='Folders', parts='32')
        self.settings = Widget.objects.create(name='Settings', parts='21')

        self.valid_payload = {
            'name': "Folders", 
            'parts': 34,
        }

        # 65 characters long
        self.invalid_payload ={
            'name':  "hdLowviK2pS3kNJ22RcOuVjPOhyraUOWQi1GN17bpY5PRe93dRDxbE1muFjjvBfSJ",
            'parts': 34,
        }

    def test_update_widget(self):
        # Confirm the DB contains 2 objects
        initial_widget_count = Widget.objects.count()
        self.assertEqual(initial_widget_count, 2)

        widget = Widget.objects.first()
        # Test that the update and create fields are the same
        delta = timedelta(seconds=1)
        self.assertAlmostEqual(widget.created, widget.updated, delta=delta)

        # Test that the update and create time are different
        time.sleep(1)
        response = self.client.put('/widgets/1/',self.valid_payload)
        created = datetime.strptime(response.data['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
        updated = datetime.strptime(response.data['updated'], '%Y-%m-%dT%H:%M:%S.%fZ')
        self.assertNotAlmostEqual(created, updated, delta=delta)

        # Test that the fields are limited to 64 characters
        response = self.client.put('/widgets/1/',self.invalid_payload)
        self.assertEqual(response.data['name'][0] ,"Ensure this field has no more than 64 characters.")