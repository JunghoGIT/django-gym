from django.contrib import admin
from django.urls import path, include
from study.views import create_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('student', create_student),
]
