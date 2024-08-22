from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:pk>', views.delete,name='delete'),
    path('<int:pk>/completed/', views.completed,name='completed'),
    path('<int:pk>/uncompleted/', views.uncompleted,name='uncompleted'),
    path('<int:pk>/update/', views.update,name='update'),

    

]
