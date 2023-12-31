from . import views
from django.urls import path
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('aboutMe', views.about, name='aboutMe'),
    # path('page1', views.page1, name='page1'),
    # path('page2', views.page2, name='page2'),
    # path('page3', views.page3, name='page3'),
    # path('films', views.films, name='films'),
    # path('book', views.books, name='books'),
    path('registration', views.RegistrationView.as_view(), name='register'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('project_create', views.ProjectView.as_view(), name='project_create'),
    path('project_page/<int:id>/', views.ProjectView.as_view(), name='project_page'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('test', views.TestPage.as_view(), name='test')
   ]