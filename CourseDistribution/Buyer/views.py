from MyAdmin.models import Profile
from django.shortcuts import redirect, render, get_object_or_404
from accounts.models import User
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from Supplier.models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import geocoder
import folium
from geopy.geocoders import Nominatim

def demo(request):
    posts = CreatePost.objects.all().order_by("id").reverse()    
    
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    print('Country:',address['country'])
    return render(request, "buyer/index.html", {'posts': posts, 'address':address})


def profile_details(request):    
    if request.method == 'POST':
        address = request.POST['address']
        buying = request.POST['buy']
        looking = request.POST['looking']
        country = request.POST['country']
        state = request.POST['state']
        
        details = User.objects.filter(id=request.user.id)
        details.update(address=address, buying_op=buying, looking_for=looking, country=country, state=state)
        # details.save()
        messages.success(request, "Your Profile completed Enjoy MarketPlace Application.")
        return redirect('/buyer-app/')
    else:
        buy_op = Qualification.objects.all()
        look_for = LookingFor.objects.all()
        coun = Country.objects.all()
        sts = State.objects.all()
        user = User.objects.get(id=request.user.id)
              
        return render(request, "buyer/profile_complete.html", {'A':buy_op, 'B':look_for, 'C':coun, 'D':sts, 'user':user})




def getProfileData(request):
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    print('Country:',address['country'])
    # get user data
    data = User.objects.get(id=request.user.id)
    return render(request, "buyer/profile.html", {'data':data, 'address':address})



def EditStudentProfile(request):
    look = LookingFor.objects.all()
    qualifi = Qualification.objects.all()
    country = Country.objects.all()
    state = State.objects.all()
    if request.method == 'POST':
        name = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        qualification = request.POST['qualification']
        looks = request.POST['look']
        count = request.POST['country']
        sta = request.POST['state']
        address = request.POST['address']
        contact = request.POST['contact']
        # dp = request.FILES['profile_img']
        
        
        
        getData = User.objects.filter(id=request.user.id)
        getData.update(first_name=name,
                            email=email,
                            username=username,
                            is_staff=True,
                            # display_picture = dp,
                            # bg_picture= bg_img,
                            contact_no = contact,
                            qualification = qualification,
                            looking_for = looks,
                            country = count,
                            state = sta,
                            address = address,
                            )
        messages.success(request, 'Profile Updated Successfull.')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
       
    else:
        getData = User.objects.get(id=request.user.id)
        return render(request, "buyer/profile-edit.html", {'getData':getData,'look':look,'state':state,'country':country, 'qualifi':qualifi})



def LikeView(request):
    # print("Buyer Calling......")
    user = request.user
    if request.method =="POST":
        post_id = request.POST.get('post_id')
        post_obj = CreatePost.objects.get(id=post_id)
        # profile = User.objects.get(user=request.user)
        
        
        if user in post_obj.like.all():
            post_obj.like.remove(user)
        else:
            post_obj.like.add(user)

        like, created = LikePost.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()
    return redirect('/buyer-app/')



def post_comment(request, id):
    if request.method == "POST":  # submit comment and then reload page
        user = request.user.id
        caption = request.POST['body']
        post_Id = id
        
        bio = CommentForPost(user_id=user, text=caption, post_id=post_Id)
        bio.save()
        
    getPost = CreatePost.objects.get(id=id)
    comment = CommentForPost.objects.all().filter(post=id)
    count_comm = CommentForPost.objects.all().filter(post=id).count()
    # print(count_comm)
    return render(request, "buyer/comments.html", {'comment':comment,'getPost':getPost, 'numofComment':count_comm})




# Code for Follow user By Shubham Raikwar

def followers_count(request):
    
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        
        if value == 'follow':
            followers_cnt = FollowersCount.objects.create(follower=follower, user=user)
            followers_cnt.save()
            print("Working follower")
            return redirect('/buyer-app/followers_count/')
        else:
            followers_cnt = FollowersCount.objects.get(follower=follower, user=user)
            followers_cnt.delete()
            return redirect('/buyer-app/followers_count/')  
    else:
        current_user = request.user
        print(current_user)
        logged_in_user = request.user.username
        user_followers = len(FollowersCount.objects.filter(user=current_user))
        user_following = len(FollowersCount.objects.filter(follower=current_user))
        user_followers0 = FollowersCount.objects.filter(user=current_user)
        user_followers1 = []
        for i in user_followers0:
            user_followers0 = i.follower
            user_followers1.append(user_followers0)
        if logged_in_user in user_followers1:
            follow_button_value = 'unfollow'
        else:
            follow_button_value = 'follow'

        print(user_followers)
        return render(request, 'buyer/follower.html', {
            'current_user': current_user,
            'user_followers': user_followers,
            'user_following': user_following,
            'follow_button_value': follow_button_value
        })

            
        # return render(request, "buyer/follower.html")
