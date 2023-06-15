from django.contrib import admin
from django.urls import path
from about import views
from blog import views as Blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', Blog.blog, name='blog'),
]
