from django.urls import path ,include
from . import views

urlpatterns = [
    path("addnew/addtaksit.html/", views.addnew, name="addnew"),
    path("addnew/privettaksit.html/", views.privettaksit, name="privettaksit"),
    path("addnew/taksitcompany.html/", views.privettaksit, name="taksitcompany"),
    path("addnew/addclient.html/", views.addclient, name="addclient"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("api/workers/", views.worker_search, name="workers"),
    path("workers-page/", views.workers_page, name="workerspage"),
]
