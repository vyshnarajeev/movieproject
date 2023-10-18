from django.urls import path,include
from .import views
app_name='movieapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('movie/<int:movie_id>',views.details,name='details'),
    path('add', views.add_movie, name='add_movie'),
    path('update/<int:id>', views.update, name='update')

]