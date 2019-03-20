from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
         url(r'^home/$', views.home, name='home'),
         url(r'^$', views.index, name='index'),
         url(r'^accounts/login/$', views.login1, name='login1'),
         url(r'^course/$', views.courses, name='courses'),
         url(r'^aboutus/$', views.about, name='about'),
         url(r'^pharma-and-life-sciences-crm/$', views.pharma, name='pharma-and-life-sciences-crm'),
         url(r'^hospitality-crm/$', views.hospitality, name='hospitality-crm'),
         url(r'^real-estate-crm/$', views.real, name='real-estate-crm'),
         url(r'^manufacturing-crm/$', views.manufacturing, name='manufacturing-crm'),
         url(r'^agri-products-crm/$', views.agri, name='agri-products-crm'),
         url(r'^it-ites-crm/$', views.ites, name='it-ites-crm'),
         url(r'^nonprofits-crm/$', views.nonprofits, name='nonprofits-crm'),
         url(r'^partners/$', views.partners, name='partners'),
         url(r'^leadsquared/$', views.leadsquared, name='leadsquared'),
         url(r'^microsoftdynamics/$', views.microsoftdynamics, name='microsoftdynamics'),
         url(r'^contact/$', views.contactus, name='contactus'),
         url(r'^registration/$', views.regform, name='regform'),
         url(r'^logout/$',auth_views.LogoutView.as_view,{'next_page': 'login1'}, name='logout'),
         url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
         url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
         url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetCompleteView.as_view(), name='password_reset_confirm'),
         url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
        ]