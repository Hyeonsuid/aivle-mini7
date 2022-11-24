from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models import Q
import os, uuid

# Create your models here.

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('모델명', max_length=50, null=True)
  file = models.FileField(max_length=254, blank=True, upload_to='model/')
  version = models.CharField(max_length=50, default='1.0')
  selected = models.BooleanField(default=None, verbose_name='운영중')
  create_dt = models.DateTimeField('생성시간', auto_now_add=True)
  update_dt = models.DateTimeField('수정시간', auto_now=True)
  accuracy = models.IntegerField(blank=True, null=True)

  class Meta:
    ordering = ('update_dt', )
    constraints = [
        models.UniqueConstraint(fields=['selected'], condition=Q(
            selected=True), name='unique_selected')
    ]

  def __str__(self):
    return self.name

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

  # def save(self, *args, **kwargs):
  #   acc = eval(self.file.path)
  #   self.accuracy = acc*100
  #   super().save(*args, **kwargs)

# def eval(model_path):
#   testdata = pd.read_csv('/home/hyeonsu/test2/web/backend/test_data.csv')
#   target = 'label'
#   x_test = testdata.drop(target, axis=1)
#   y_test = testdata.loc[:, target]

#   x_test2 = x_test.values
#   x_test2 = x_test2.reshape(-1,28,28,1)
#   x_test2 = x_test2/ 255.
#   model = load_model(model_path)
#   pred = model.predict(x_test2).argmax(axis=1)
#   return accuracy_score(y_test, pred)


# class Result(models.Model):
#     image = models.ImageField(blank=True)
#     answer = models.CharField(max_length=10)
#     result = models.CharField(max_length=10)
#     pub_date = models.DateTimeField('date published')

# class AImodel(models.Model):
#     ai_file = models.FileField(upload_to='model/',blank=True)
#     ai_version = models.CharField(max_length=50,default=1.0)
#     is_selected = models.BooleanField(default=False)
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
