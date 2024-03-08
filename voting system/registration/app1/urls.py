from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('profile/',views.view_profile,name='profile'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('candidate_dashboard/',views.candidate_dashboard,name='candidate_dashboard'),
    path('voter_dashboard/',views.voter_dashboard,name='voter_dashboard'),
    path('users/',views.display_users,name='users'),
    path('report/',views.display_report,name='report'),
    path('analytics/',views.display_analytics,name='analytics'),
    path('events/',views.display_events,name='events'),
    path('dashboard/',views.display_dashboard,name='dashboard')
]
    # path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    # path('candidate_dashboard/',views.candidate_dashboard,name='candidate_dashboard'),
    path('voterdashboard/',views.voterdashboard,name='voterdashboard'),
    path('profile/',views.profile,name='profile'),
    path('next_page/',views.next_page,name='next_page'),
    path('index/',views.index,name='index'),
    
    

    

]
