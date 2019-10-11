from django.views import View
from VueApp.models import Class_info
from django.http import JsonResponse
from django.shortcuts import render_to_response

class ClassInfo(View):
    def __init__(self):
        super(ClassInfo,self).__init__()
        self.response = {
            "code": 200,
            "D": []
        }
    def get(self,request):
        self.response["D"] = [
            {
                "class_number":line.class_number,
                "class_name": line.class_name,
                "rx_time": line.rx_time,
                "yx": line.yx,
            }
            for line in Class_info.objects.all()
        ]
        return JsonResponse(self.response)

    def post(self, request):
        class_number = request.POST.get("class_number")
        class_name = request.POST.get("class_name")
        rx_time = request.POST.get("rx_time")
        yx = request.POST.get("yx")

        cif = Class_info()
        cif.class_number = class_number
        cif.class_name = class_name
        cif.rx_time = rx_time
        cif.yx = yx
        cif.save()

        self.response["data"] = "保存成功"
        return JsonResponse(self.response)

    def put(self, request):
        return JsonResponse(self.response)

    def delete(self, request):
        return JsonResponse(self.response)

def class_info(request):
    return render_to_response("vueapp/class_info.html",locals())
# Create your views here.
