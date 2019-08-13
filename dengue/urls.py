from django.urls import path
from .import views 
from django.contrib.auth import views as auth_views
urlpatterns = [  
    #path('admin/', admin.site.urls),
    path('', views.viewshome, name="index"),

    #adminpanel
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),  
    path('accounts/reg_form/',views.register, name="register"),
    path('accounts/profile/',views.profile, name="profile"),

    #setting
    path('setting/activitylog/', views.activitylog, name="activitylog"),

]  