from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='post_details'),    
    path('profile_detail/', views.profile_details, name='form'),
    path('profile/',views.getProfileData, name="profile"),
    path('profile-edit/', views.EditStudentProfile, name="myprofile"),
    path('like/', views.LikeView, name="like_post"),
    path('comment/<int:id>/', views.post_comment, name="comment"),
    path('followers_count/', views.followers_count, name="followers_count")
]
