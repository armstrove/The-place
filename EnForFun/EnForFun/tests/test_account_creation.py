import pytest
from accounts.models import User
from accounts.models import UserManager
import time

@pytest.mark.django_db
def authenticated_user(client, django_user_model):
    email       = "some@gmail.com",
    password    = "Bobo!@34",
    full_name   = "Vazgen",
    is_active      = True,
    is_staff       = False,
    is_admin       = False,
    user = django_user_model.objects.create_user(
       email       = "some@gmail.com",
       password    = "Bobo!@34",
       full_name   = "Vazgen",
       is_active      = True,
       is_staff       = False,
       is_admin       = False,
   )
    # Use this:
    client.force_login(user)
    # Or this:
    #client.login(email=email, password=password)
    #response = client.get('/private')
    #assert response.content == 'Protected Area'

#@pytest.mark.django_db
#def test_account_create():

   #account = create_user(
   #    email       = "some@gmail.com",
   #    password    = "Bobo!@34",
   #    full_name   = "Vazgen",
   #    is_active      = True,
   #    is_staff       = False,
   #    is_admin       = False,
   #)

   #print(dir(account))
   #assert account.email == "some@gmail.com"
time.sleep(5)
