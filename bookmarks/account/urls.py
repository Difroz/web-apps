from django.conf.urls import url
from django.contrib.auth import views as views_auth
from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),

    # login/logout urls
    url(r'^login/$', views_auth.LoginView.as_view(), name='login'),
    url(r'^logout/$', views_auth.LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login/$', views_auth.logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    # change password urls
    url(r'^password-change/$', views_auth.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', views_auth.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password
    url(r'^password-reset/$', views_auth.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', views_auth.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', views_auth.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', views_auth.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # register
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
]
