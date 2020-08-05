"""django_afx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django_afx import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/',include(('app01.urls','app01'))),
    path('app02/',include(('app02.urls','app02'))),
    path('app03/',include(('app03.urls','app03'))),
    path('app04/',include(('app04.urls','app04'))),
    path("app05/",include(('app05.urls',"app05"))),
    path('captcha/',include("captcha.urls"))
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[
        path("__debug__/",include(debug_toolbar.urls)),
    ]+urlpatterns