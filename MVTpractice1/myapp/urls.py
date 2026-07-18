from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.getstudents,name='students'),
    path('add/',views.addstudent,name='add'),
    path('find/<int:id>/',views.getstudent),
    path('edit/<int:id>/',views.editstudent),
    path('delete/<int:id>/',views.deletestudent),
]