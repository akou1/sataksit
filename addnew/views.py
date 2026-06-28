# في views.py
from django.shortcuts import render
from django.http import JsonResponse
import json
from baladia.main_printer import print_full_bundle
from baladia.taksitprivet import print_privet_tk


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
    return render(request, "pages/addclient.html" )
