from django.shortcuts import render
from django.shortcuts import redirect
import logging
from .models import AImodel
logger = logging.getLogger('mylogger')
# Create your views here.


def index(request):
    #서비스 처리 
    models = AImodel.objects.all()
    return render(request, 'model_input.html',{'models':models})



def upload(request):
    #서비스 처리 
    if request.method == 'POST' and request.FILES['files']:

        #form에서 전송한 파일을 획득한다.

        file = request.FILES['files']
              
        aimodel = AImodel(ai_file=file, ai_version=request.POST['num'])
        
        aimodel.save(aimodel)
        
        
        
   
    # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠
    else:
        test = request.GET['test']
        logger.error(('Something went wrong!!',test))

    return redirect('backend:index')  