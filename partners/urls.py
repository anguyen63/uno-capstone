from django.urls import path
from . import views
app_name = 'partners'

urlpatterns = [
     path('registerCampusPartner/', views.registerCampusPartner, name='registerCampusPartner'),
     path('registerCommunityPartner/', views.registerCommunityPartner, name='registerCommunityPartner'),
     path('profile/userprofile/', views.userProfile, name='userprofile'),
     path('profile/userprofileupdate/', views.userProfileUpdate,name='userprofileupdate'),
     path('profile/orgprofile/', views.orgProfile, name='orgprofile'),
     path('profile/orgprofileupdate/', views.orgProfileUpdate, name='orgprofileupdate'),
     path('orgprofile/campus_partner_add/', views.CommunityPartnerAdd, name='campuspartneradd'),
	 path('SuggestCommunity/', views.ajax_load_project, name='ajax_load_project'),

]
