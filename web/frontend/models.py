from django.db import models
import uuid
from backend.models import Post
# Create your models here.

class Result(models.Model):
  id = models.BigAutoField(primary_key=True)
  uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  version = models.CharField(max_length=50)
  image = models.ImageField(blank=True)
  answer = models.CharField(max_length=10)
  result = models.CharField(max_length=10)
  is_answer_check = models.BooleanField(max_length=10)
  pub_date = models.DateTimeField('date published')
