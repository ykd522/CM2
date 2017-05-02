"""CM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'register$', views.Register),
    url(r'api-token-auth$', obtain_jwt_token),
    url(r'getRequestList$', views.GetRequestList), 
    url(r'acceptRequest$', views.AcceptRequest),
    url(r'rejectRequest$', views.RejectRequest),
    url(r'addAdminUser$', views.AddAdminUser),
    url(r'changePassword$', views.ChangePassword),
    url(r'forgetPassword$', views.ForgetPassword),
    url(r'viewFile$', views.ViewFile),
    url(r'search$', views.FirstSearch),
    url(r'downloadFile$', views.download),
    url(r'deleteFile$', views.DeleteFile),
    url(r'getFileDetail$', views.GetFileDetail),
    




    
]
