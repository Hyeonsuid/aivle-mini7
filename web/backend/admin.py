from django.contrib import admin
from backend.models import Post,Result,AImodel

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'used', 'create_dt', 'update_dt')

class AIModelAdmin(admin.ModelAdmin):
  fields = ['ai_version', 'ai_file',  'is_selected']
  list_display = ['ai_version', 'ai_file', 'is_selected']
  search_fields = [ 'ai_version', 'ai_file']
  
admin.site.register(Result)
admin.site.register(AImodel, AIModelAdmin)