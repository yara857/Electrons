from os import name
from django.urls import path,include
from . import views
from .views import index_sch 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , views.index, name='index'),
    path('login', views.log_in, name="login"), 
    path('logout', views.log_out, name="logout"),
    path('profile',views.index_sch , name ='profile'),
    path('profile_signed',views.profile_signed , name ='profile_signed'),
    path('material',views.material_stu , name ='material'), 
    # path('assignment' ,views.assignment , name = 'assignment'),
    path('assignment' , views.assignment_ass , name="assignment")
    
]
urlpatterns +=  static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)