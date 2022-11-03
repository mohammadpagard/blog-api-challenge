from django.urls import path
from . import views


app_name = 'article'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
