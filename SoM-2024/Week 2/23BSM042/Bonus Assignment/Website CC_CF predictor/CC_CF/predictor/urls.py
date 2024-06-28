# predictor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('codeforces_to_codechef/', views.predict_codechef_from_codeforces, name='codeforces_to_codechef'),
    path('codechef_to_codeforces/', views.predict_codeforces_from_codechef, name='codechef_to_codeforces'),
]
