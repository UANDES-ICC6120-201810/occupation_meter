from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from .models import CountRequest

class ModelTestCase(TestCase):
    """This class defines the test suite for the count request model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.count_request_source_endpoint = "http://zapo-storage.ny3.digitaloceanspaces.com"
        self.count_request_source_bucket = "occupation_images/202481589213556"
        self.count_request_source_filename = "201805312205.png"
        self.count_request = CountRequest(source_endpoint=self.count_request_source_endpoint,
                                          source_bucket=self.count_request_source_bucket,
                                          source_filename=self.count_request_source_filename)

    def test_model_can_create_a_counting_request(self):
        """Test the count request model can create a count_request."""
        old_count = CountRequest.objects.count()
        self.count_request.save()
        new_count = CountRequest.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.count_request_data = {
            'source_endpoint': 'http://zapo-storage.ny3.digitaloceanspaces.com',
            'source_bucket': 'occupation_images/202481589213556',
            'source_filename': '201805312205.png'}
        self.response = self.client.post(
            reverse('create'),
            self.count_request_data,
            format="json")

    def test_api_can_create_a_count_request(self):
        """Test the api has count_request creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_count_request(self):
        """Test the api can get a given bucketlist."""
        count_request = CountRequest.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': count_request.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, count_request)

    def test_api_can_update_count_request(self):
        """Test the api can update a given bucketlist."""
        count_request = CountRequest.objects.first()
        change_count_request = {'count': '4'}
        res = self.client.put(
            reverse('details', kwargs={'pk': count_request.id}),
            change_count_request, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_count_request(self):
        """Test the api can delete a bucketlist."""
        count_request= CountRequest.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': count_request.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
