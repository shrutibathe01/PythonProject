from . import views
from django.urls import path

urlpatterns = [
    path('',views.mainDesktop,name='maindesktop'),
    path('TenantSignup/',views.TenantSignup,name='TenantSignup'),
    path('tenantDashboard/',views.tenantDashboard,name='tdashboard'),
    path('pgDetails/<int:key>',views.pgDetails,name='pgdetails'),
    path('contact/',views.contact,name='contact'),
    path('aboutUs/',views.aboutUs,name='aboutUs'),
    path('faq/',views.faq,name='faq'),
    path('forgotP/',views.ForgotP,name='forgotP'),
    path('OwnerSignup/',views.OwnerSignup,name='OwnerSignup'),
    path('TenantInfo/',views.TenantInfo,name='TenantInfo'),
    path('Saved_Pg/',views.Saved_Pg,name='Saved_Pg'),
    path('RegisterTenant/',views.RegisterTenant,name='RegisterTenant'),
    path('DeleteTenant/<int:key>',views.DeleteTenant,name='DeleteTenant'),
    path('DeleteOwner/<int:key>',views.DeleteOwner,name='DeleteOwner'),
    path('SearchPg/',views.SearchPg,name='SearchPg'),
    path('OwnerInfo/',views.OwnerInfo,name='OwnerInfo'),
    path('logout/',views.logout,name='logout'),
    path('SearchPgDetails/<int:key>',views.SearchPgDetails,name='SearchPgDetails'),
    
]