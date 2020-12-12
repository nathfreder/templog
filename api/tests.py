from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status
from .views import TemperatureViewSet


class TemperatureTestCase(APITestCase):
    def setUp(self):
        # Create test superuser
        User.objects.create_superuser(username='test')

    def test_create_temperature(self):
        """
        Ensure we can create a new temperature object.
        """
        factory = APIRequestFactory()
        user = User.objects.get(username='test')
        view = TemperatureViewSet.as_view({'post': 'create'})
        request = factory.post('/api/temps', {'temperature': 10.0, 'date': '2020-12-11T00:09:46Z'}, format='json')
        force_authenticate(request, user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_temperatures(self):
        """
        Ensure we can get all temperature objects.
        """
        factory = APIRequestFactory()
        view = TemperatureViewSet.as_view({'get': 'list'})
        request = factory.get('/api/temps')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
