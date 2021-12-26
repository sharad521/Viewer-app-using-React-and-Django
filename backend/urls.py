from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import current_user, UserList
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
     path('about/', views.AboutList.as_view()),
    path('about/<int:pk>/', views.AboutDetail.as_view()),
     path('current_user/', current_user),
    path('users/', UserList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)