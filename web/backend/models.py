from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField('모델명', max_length=50)
  description = models.CharField('설명', max_length=100, blank=True, help_text='설명을 적어주세요.')
  upload = models.FileField(max_length=254, blank=True)
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
  

