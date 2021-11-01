from django.urls import path
from . import views

urlpatterns = [
    path('new_review/<product_id>/', views.new_review, name='new_review'),
]
