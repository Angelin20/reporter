from django.urls import path, include
from . import views
from rest_framework import routers
from .views import getPDF

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('getPDF',getPDF.as_view(),name='getPDF')
]