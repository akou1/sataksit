from django.urls import path ,include
from . import views

urlpatterns = [
    path("addnew/addtaksit.html/", views.addnew, name="addnew"),
    path("addnew/privettaksit.html/", views.privettaksit, name="privettaksit"),
    path("addnew/taksitcompany.html/", views.privettaksit, name="taksitcompany"),
    path("addnew/addclient.html/", views.addclient, name="addclient"),
]
