from django.urls import path
from .views import (SpellcheckListview, SpellUpdateDeleteApiView,)
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('spellcheck/', SpellcheckListview.as_view(), name='SpellcheckListview'), 
    path('spell/<int:pk>/', SpellUpdateDeleteApiView.as_view(), name='SpellUpdateDeleteApiView'),
]