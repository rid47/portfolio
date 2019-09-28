from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.allblogs, name="allblogs"),
    path('blog/<int:blog_id>/', views.detail, name='detail')


]
