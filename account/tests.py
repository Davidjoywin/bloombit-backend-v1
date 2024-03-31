from django.test import TestCase

# Create your tests here.
from .utils import create_token

from .models import UserProfile

user = UserProfile.objects.get(username='davidjoy')
token = create_token()
print(user)

# fetch('http://localhost:8000')
# .then(res => res.json())
# .then(data => console.log(data))