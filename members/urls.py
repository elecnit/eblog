from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('register/',views.UserRegisterView.as_view(),name='register'),
   path('edit_profile/',views.UserEditView.as_view(),name='edit_settings'),
   #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
   path('password/',views.PasswordsChangeView.as_view(template_name='registration/change-password.html'),name='change_password'),
   path('user_profile/<int:pk>/',views.ShowProfilePageView.as_view(),name='show_profile'),
   path('edit_user_profile/<int:pk>',views.EditProfilePageView.as_view(),name='edit_profile'),
   path('Create_user_profile',views.CreateProfileView.as_view(),name='create_profile'),  
   path('successful_password_change/',views.SuccessfulPasswordChangeView,name='successfull_password_change')
]