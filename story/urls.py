from django.urls import path
from .views import indexView, Search

urlpatterns = [
    path('', indexView.as_view(), name='story-list'),
    path('/search', Search.as_view(), name='search')
]
