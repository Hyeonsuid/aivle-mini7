from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
from keras.models import load_model
from keras.preprocessing import image
# from pybo.model import Result
from .models import Result

# Create your views here.

logger = logging.getLogger('mylogger')

def index(request):
    return render(request, 'index.html')




def upload(request):
    result_list = []
    count = 0
    if request.method == 'POST':
        images = request.FILES.getlist('files')
        for image in images:
        #todo form에서 전송한 파일을 획득한다.
            file = image
            # logger.error('file', file)
            # class names 준비
            class_names = list(string.ascii_lowercase)
            class_names = np.array(class_names)

            #todo 모델 로딩
            model_path = './model/sign_model.h5'# model위치를 setting에 정의해놨으니 활용해서 채워보세요. 위치는 본인이 원하는 다른곳에 해도 됩니다.
            model = load_model(model_path)

            #todo history 저장을 위해 객체에 담아서 DB에 저장한다.
            # 이때 파일시스템에 저장도 된다.
            result = Result()
            result.answer = request.POST.getlist('answer')[count] # answer를 채워봅시다.
            result.image = file # image를 채워봅시다.
            result.pub_date = timezone.datetime.now()
            result.save()

            img_path = result.image.url
            img = cv2.imread('./'+img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (28, 28))
            test_sign = img.reshape(1,28,28,1)
            test_sign = test_sign / 255.
            pred = model.predict(test_sign)
            pred = pred.argmax(axis=1)
            result.result = class_names[pred][0]#예측결과
            # if(result.result == result.answer):
            #     is_check_list.append(True) 
            # else:
            #     is_check_list.append(False) 
            result.save() 
            result_list.append(result)
            count+=1
        context = {
            'result_list': result_list
        }
        print(result_list)
    # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠.
    else:
        test = request.GET['test']
        logger.error(('Something went wrong!!',test))
    
    return render(request, 'result.html', context) 

