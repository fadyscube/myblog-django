from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path('', views.index, name='index'),
	path('post/<int:id>/', views.show, name='show'),
	path('new_post/', views.new_post, name='new_post'),
	path('update_post/<int:id>/', views.update_post, name='update_post'),
	path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
	path('search_posts/', views.search_posts, name='search_posts'),
]