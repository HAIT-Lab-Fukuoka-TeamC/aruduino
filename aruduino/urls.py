"""aruduino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from serialLED.views import IndexTemplateView_1
#from serialLED.views import IndexTemplateView_2
#from serialLED.views import SampleCopyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('serialLED/', IndexTemplateView_1.as_view(),name='index_1')
#    path('serialLED/', IndexTemplateView_2.as_view(),name='index_2')
    # path('serialLED_2/', IndexTemplateView_2.as_view(),name='index_2')
]
