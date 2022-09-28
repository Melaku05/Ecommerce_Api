from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestCreateCollection:
  def test_if_user_is_anonymous_returns_401(self):
    client = APIClient()
    response = client.post('/collections/', {'title':'a'}) 
    assert response.status_code == status.HTTP_401_UNAUTHORIZED 
   # Authenticating the user (The client is authenticated, but the current user is not an admin)
  def test_if_user_is_not_admin_returns_403(self):
    client = APIClient()
    client.force_authenticate({})
    response = client.post('/collections/', {'title':'a'}) 
    assert response.status_code == status.HTTP_403_FORBIDDEN