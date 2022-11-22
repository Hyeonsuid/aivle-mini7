from django.contrib import admin
from backend.models import Post,Result,AImodel

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'upload', 'create_dt', 'update_dt')
  
  
admin.site.register(Result)
admin.site.register(AImodel)