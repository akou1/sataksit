# في views.py
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
import json
from baladia.main_printer import print_full_bundle
from baladia.taksitprivet import print_privet_tk
from .models import addclients, Worker

# Create your views here.
def addnew(request):
    if request.method == 'GET':
        # يعرض الصفحة عندما يزورها المستخدم
        # return render(request, 'addnew/index.html')
      return render(request ,"pages/addtaksit.html")
    elif request.method == 'POST':
        # يستقبل البيانات عندما يرسل النموذج
        try:
            
           
            data = json.loads(request.body)
             

            print("\n--- بيانات التقسيط الواصلة ---")
            personelinfo = data['personal_info']
            monthlypay = data['financial_info']
            print(f"bla bla bla {personelinfo['datecute']}")
            # print(f"datecute {monthlypay['datecute']}")
            print(f"bla bla bla {monthlypay}")
            print(f"bla bla bla {personelinfo}")
            print_full_bundle(personelinfo , monthlypay)
            # fill_pdf_form(
   
            # "filledform.pdf",
            # personelinfo , monthlypay , mode="full"
            # )
            # generate_ccp_page(personelinfo ,monthlypay ,"cc.pdf", mode="full")
            # print(f"bla bla bla {data['ccp']}")
            # print(f"bla bla bla {data['personal_info']['ccp']}")
        
        # طباعة البيانات بشكل منظم في الـ CMD
            # print(f"الرسالة: {data.get('message')}")
            # print(f"المبلغ الإجمالي: {data['personal_info']['ccp']}")
            # print(f"المبلغ الإجمالي: {data}")
            # print(f"القسط الشهري: {data['financial_info']['monthly_cut']}")
            print("----------------------------\n")
        
            return JsonResponse({'status': 'success', 'msg': 'تم استقبال بيانات التقسيط بنجاح!'})
  
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'msg': str(e)
            }, status=400)

def privettaksit(request):
    if request.method == 'GET':
        # يعرض الصفحة عندما يزورها المستخدم
        # return render(request, 'addnew/index.html')
      return render(request ,"pages/privettaksit.html")
    elif request.method == 'POST':
        # يستقبل البيانات عندما يرسل النموذج
        try:
            
           
            data = json.loads(request.body)
             

            print("\n--- بيانات التقسيط الواصلة ---")
            personelinfo = data['personal_info_privet']
            monthlypay = data['financial_info_privet']
            # print(f"bla bla bla {personelinfo['datecute']}")
            # print(f"datecute {monthlypay['datecute']}")
            print(f"bla bla bla {monthlypay}")
            print(f"bla bla bla {personelinfo}")
            print_privet_tk(personelinfo , monthlypay )
            # print_full_bundle(personelinfo , monthlypay)
            # fill_pdf_form(
   
            # "filledform.pdf",
            # personelinfo , monthlypay , mode="full"
            # )
            # generate_ccp_page(personelinfo ,monthlypay ,"cc.pdf", mode="full")
            # print(f"bla bla bla {data['ccp']}")
            # print(f"bla bla bla {data['personal_info']['ccp']}")
        
        # طباعة البيانات بشكل منظم في الـ CMD
            # print(f"الرسالة: {data.get('message')}")
            # print(f"المبلغ الإجمالي: {data['personal_info']['ccp']}")
            # print(f"المبلغ الإجمالي: {data}")
            # print(f"القسط الشهري: {data['financial_info']['monthly_cut']}")
            print("----------------------------\n")
        
            return JsonResponse({'status': 'success', 'msg': 'تم استقبال بيانات التقسيط بنجاح!'})
  
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'msg': str(e)
            }, status=400)

def taksitcompany(request):
    if request.method == 'GET':
        # يعرض الصفحة عندما يزورها المستخدم
        # return render(request, 'addnew/index.html')
      return render(request ,"pages/taksitcompany.html")
    elif request.method == 'POST':
        # يستقبل البيانات عندما يرسل النموذج
        try:
            
           
            data = json.loads(request.body)
             

            print("\n--- بيانات التقسيط الواصلة ---")
            personelinfo = data['personal_info_privet']
            monthlypay = data['financial_info_privet']
            # print(f"bla bla bla {personelinfo['datecute']}")
            # print(f"datecute {monthlypay['datecute']}")
            print(f"bla bla bla {monthlypay}")
            print(f"bla bla bla {personelinfo}")
            print_privet_tk(personelinfo , monthlypay )
            # print_full_bundle(personelinfo , monthlypay)
            # fill_pdf_form(
   
            # "filledform.pdf",
            # personelinfo , monthlypay , mode="full"
            # )
            # generate_ccp_page(personelinfo ,monthlypay ,"cc.pdf", mode="full")
            # print(f"bla bla bla {data['ccp']}")
            # print(f"bla bla bla {data['personal_info']['ccp']}")
        
        # طباعة البيانات بشكل منظم في الـ CMD
            # print(f"الرسالة: {data.get('message')}")
            # print(f"المبلغ الإجمالي: {data['personal_info']['ccp']}")
            # print(f"المبلغ الإجمالي: {data}")
            # print(f"القسط الشهري: {data['financial_info']['monthly_cut']}")
            print("----------------------------\n")
        
            return JsonResponse({'status': 'success', 'msg': 'تم استقبال بيانات التقسيط بنجاح!'})
  
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'msg': str(e)
            }, status=400)

def addclient(request):
    if request.method == 'GET':
        return render(
            request, "pages/addclient.html", {"pro": addclients.objects.all()}
        )
    elif request.method == "POST":
        # يستقبل البيانات عندما يرسل النموذج
        try:

            data = json.loads(request.body)

            print("\n--- بيانات التقسيط الواصلة ---")
            personelinfo = data["personal_info_sy"]
            print(personelinfo)
            addclientse = addclients.objects.create(
                cle=personelinfo["cle"],
                ccp=personelinfo["ccp"],
                name=personelinfo["first_name"],
                lastname=personelinfo["last_name"],
            )

            return JsonResponse(
                {"status": "success", "msg": "تم التسجيل!"}
            ) 

        except Exception as e:
            return JsonResponse({"status": "error", "msg": str(e)}, status=400)


def update(request, id):
    # 1. جلب بيانات العميل الحالي بناءً على الـ id أو إظهار خطأ 404 إذا لم يكن موجوداً
    client = get_object_or_404(addclients, id=id)

    # 2. التحقق مما إذا كان الطلب من نوع POST (إرسال بيانات)
    if request.method == "POST":
        try:
            # تحويل البيانات القادمة بصيغة JSON إلى قاموس (Dictionary)
            data = json.loads(request.body)
            personelinfo = data.get("personal_info_sy", {})

            # تحديث حقول العميل بالقيم الجديدة
            client.cle = personelinfo.get("cle", client.cle)
            client.ccp = personelinfo.get("ccp", client.ccp)
            client.name = personelinfo.get("first_name", client.name)
            client.lastname = personelinfo.get("last_name", client.lastname)

            # حفظ التعديلات في قاعدة البيانات
            client.save()

            # إرجاع استجابة بنجاح العملية للفرونت إند
            return JsonResponse(
                {"status": "success", "message": "تم تحديث البيانات بنجاح"}
            )

        except (ValueError, KeyError):
            # إرجاع خطأ في حال كانت البيانات المرسلة غير صالحة
            return JsonResponse(
                {"status": "error", "message": "بيانات غير صالحة"}, status=400
            )

    # 3. إذا كان الطلب من نوع GET، يتم عرض صفحة التعديل مع تمرير بيانات العميل الحالية
    return render(request, "pages/update.html", {"client": client})


def delete(request, id):
    client = get_object_or_404(addclients, id=id)

    if request.method == "POST":
        client.delete()

        return JsonResponse({"status": "success", "message": "تم حذف البيانات بنجاح"})

    return render(request, "pages/delete.html", {"client": client})


def worker_search(request):
    query = request.GET.get("q", "")

    workers = Worker.objects.filter(name__icontains=query)

    results = list(workers.values("id", "name"))

    return JsonResponse(results, safe=False)

def workers_page(request):
    return render (request, "pages/workers.html")