"""little_kitten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from little_kitten.views import probar_template_legacy, saludo, segunda_vista, dia, my_name, age, probar_template_legacy, probar_template, template_amor   


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('svista/', segunda_vista),
    path('fecha/', dia ),
    path('mi-nombre-es/<nombre>/', my_name),
    path('edad/<int:edad>/', age),
    path('template-1/', probar_template_legacy),
    path('template-2/', probar_template),
    path('template-love/', template_amor),
]
