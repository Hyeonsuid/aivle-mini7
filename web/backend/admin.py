from django.contrib import admin
from backend.models import Post
from sklearn.metrics import accuracy_score
from keras.models import load_model
import pandas as pd

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  # fields = ['version', 'file', 'create_dt', 'selected']
  list_display = ['name', 'file', 'version', 'selected', 'create_dt']
  actions = ['make_accuracy']
  # search_fields = ['create_dt', 'version', 'file']

  @admin.action(description="Make Accuracy")
  def make_accuracy(self, request, queryset):
    pass
    # queryset.update(accuracy = eval(request.))

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

# class AIModelAdmin(admin.ModelAdmin):
#   fields = ['ai_version', 'ai_file', 'created', 'is_selected']
#   list_display = ['ai_version', 'ai_file', 'is_selected', 'created']
#   search_fields = ['created', 'ai_version', 'ai_file']
#   ordering = ['-created']
# admin.site.register(Result)
# admin.site.register(AImodel, AIModelAdmin)