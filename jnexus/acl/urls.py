from django.urls import path
from acl.views import GoogleView
from . import views
from . import profileView
from .profileView import UserList, UserDetails, SocialMediaAccountList, SocialMediaAccountDetail

urlpatterns = [
 
    path('google-auth/', GoogleView.as_view(), name="google"),
    path('resources/', views.create_resource,name='Acl'),
    path('resources/<int:resourceId>/', views.get_resource,name='Acl'),
    path('resources/<int:resourceId>/permissions/', views.update_resource_permissions,name='Acl'),
    path('users/', UserList.as_view() ,name='User'),
    path('users/<str:username>/', UserDetails.as_view(),name='User'),
    path('users/<str:username>/social-media-accounts/', SocialMediaAccountList.as_view(),name='User'),
    path('users/<str:username>/social-media-accounts/<int:index>/', SocialMediaAccountDetail.as_view(),name='User'),

]
