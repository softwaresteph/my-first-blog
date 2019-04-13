from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.post_list, name="post_list"), # The empty quotation marks means that this will be the default route
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]