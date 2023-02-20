from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.Register.as_view(), name='register'),
    path('profile', views.profile, name='profile')


    # path('adminclick', views.adminclick_view),
    # path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    # path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
]
