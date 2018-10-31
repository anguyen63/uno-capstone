from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [

   path('', views.cpipage, name='cpipage'),
   path('home',views.home, name='home'),
   path('campusHome',views.campusHome, name='campusHome'),
   path('CommunityHome',views.CommunityHome, name='CommunityHome'),
   path('k12map', views.k12map, name='k12map'),
   path('map', views.map, name='map'),
   path('projectmap', views.projectmap, name='projectmap'),
   path('registerCampusPartnerUser/', views.registerCampusPartnerUser, name='registerCampusPartnerUser'),
   path('registerCommunityPartnerUser/', views.registerCommunityPartnerUser, name='registerCommunityPartnerUser'),
   path('signupuser/registerCampusPartnerUser/', views.registerCampusPartnerUser, name='registerCampusPartnerUser'),
   path('signupuser/registerCommunityPartnerUser/', views.registerCommunityPartnerUser,name='registerCommunityPartnerUser'),
   path('signup/', views.signup, name='signup'),
   path('signupuser/', views.signupuser, name='signupuser'),
   path('upload_project/', views.upload_project, name='upload_project'),
   path('upload_community/', views.upload_community, name='upload_community'),
   path('upload_campus/', views.upload_campus, name='upload_campus'),
   path('projectreport/', views.projectreport, name='projectreport'),
   path('projectInfo/', views.project_partner_info, name='project_partner_info'),
   path('engageType/', views.engagement_info, name='engagement_info'),

]
