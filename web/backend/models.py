from django.db import models
from django.conf import settings
from django.dispatch import receiver
import os, uuid

# Create your models here.
class Post(models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  id = models.BigAutoField(primary_key=True)
  title = models.CharField('모델명', max_length=50)
  description = models.CharField('설명', max_length=100, blank=True, help_text='설명을 적어주세요.')
  file = models.FileField(max_length=254, blank=True)
  used = models.BooleanField(default=False, verbose_name='운영중', unique=True)
  create_dt = models.DateTimeField('생성시간', auto_now_add=True)
  update_dt = models.DateTimeField('수정시간', auto_now=True)

  class Meta:
    ordering = ('update_dt', )

  def __str__(self):
    return self.title
  
  
class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

class AImodel(models.Model):
    ai_file = models.FileField(upload_to='model/',blank=True)
    ai_version = models.CharField(max_length=50,default=1.0)
    is_selected = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  

@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
  if instance.file:
    if os.path.isfile(instance.file.path):
      os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
  if not instance.pk:
    return False
  try:
    old_file = Post.objects.get(pk=instance.pk).file
  except Post.DoesNotExist:
    return False

  new_file = instance.file
  if not old_file == new_file:
    if os.path.isfile(old_file.path):
      os.remove(old_file.path)
  

class Statistic(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  model = models.CharField(max_length=50)
  count = models.IntegerField()
  hit = models.IntegerField()