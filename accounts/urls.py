from __future__ import unicode_literals
from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.dashboard, name="accounts_dashboard"),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="accounts_login"),
    path('saida/', LogoutView.as_view(), {'next_page':'core_home'}, name="accounts_logout"),
    path('cadastre-se/', views.register, name="accounts_register"),
    path('nova-senha/', views.password_reset, name="accounts_password_reset"),
    path('confirmar-nova-senha/<int:key/', views.password_reset_confirm, name="accounts_password_reset_confirm"),
    path('editar/', views.edit, name="accounts_edit"),
    path('editar-senha/', views.edit_password, name="accounts_edit_password"),
]