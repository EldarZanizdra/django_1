from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    # path('aboutMe', views.about, name='aboutMe'),
    # path('page1', views.page1, name='page1'),
    # path('page2', views.page2, name='page2'),
    # path('page3', views.page3, name='page3'),
    # path('filmpage', views.films, name='films'),
    # path('book', views.books, name='books'),
    path('register', views.registration, name='register'),
    path('login', views.login, name='login'),
    path('project_create', views.project_create, name='project_create'),
    path('project_page/<int:id>', views.project, name='project_page'),
   ]