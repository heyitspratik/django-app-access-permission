from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('usermodel.urls')),
    # path('',include('app1.urls')),
    # path('',include('app2.urls')),
    path('', include(router.urls)),

]