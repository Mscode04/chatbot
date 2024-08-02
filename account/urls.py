from django.urls import path
from .views import *


urlpatterns=[
    path('sin',SignInView.as_view(),name="sin"),
    path('sout',SignOutView.as_view(),name="sout"),
    path('sup',SignUpView.as_view(),name="sup")
    
]