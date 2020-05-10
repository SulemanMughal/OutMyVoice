from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)

# App View Import Statements
from . import views

urlpatterns = [
    
    
    # Home View URL
    url(r'^$', 
        views.home, 
        name="home_page"
    ),
    
    # User Login View URL
    url(r'^login/$',
        views.login_User,
        name="login_user_url"
    ),
    
    # User Logout View URL
    url(r'^logout/$', 
        views.logout_User, 
        name= "logout_user_url"
    ),

    # User Dashboard View URL
    url(r'^dashbaord/$', 
        views.dashboard, 
        name = "dashboard"
    ),
    
    # User Registration View URL
    url(r'^register/$', 
        views.register_user, 
        name= "register"
    ),
    
    # Register Account Email Confirmation View URL
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, 
        name='activate'
    ),
    
    # -------------------------------------------------------------------------------------------------------
    # Password Reset URL(s)
    path('password_reset/', 
        PasswordResetView.as_view(), 
        name='password_reset' 
    ),
    path('password_reset/done/', 
        PasswordResetDoneView.as_view(), 
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(), 
        name='password_reset_confirm'
    ),
    path('reset/done/', 
        PasswordResetCompleteView.as_view(), 
        name='password_reset_complete'
    ),
    
    # ------------------------------------PROFILE URL(s)---------------------------------------
    
    # Profile View URL
    url(r'^profile/$', 
        views.profile_user, 
        name= "profile"
    ),
    
    
    # ****************************************************************
    # User Profile Page
    # ****************************************************************
    path("view-users-profiles/", views.UserProfiles, name="UserProfiles"),
    
    # ****************************************************************
    # Update Specific User Profile
    # ****************************************************************
    path("view-users-profiles/<int:user_id>", views.UserProfiles, name="UserProfilesUpdate"),
    
    # ****************************************************************
    # Remove Specific User
    # ****************************************************************
    path("remove-user/<int:user_id>", views.removeUser, name="removeUser"),
    
    # **************************************PROFILE URL(s)***************************************
    
    # User Change Password View URL
    url(r'^change_password/$', 
        views.change_password, 
        name = "change_password"
    ),
    
    # ------------------------------------PETITION URL(s)---------------------------------------
    
    # ****************************************************************
    # Petitions URL(s)
    # ****************************************************************
    
    # ****************************************************************
    # Create Petition View URL
    # ****************************************************************
    path("petition_start/",  views.petition_start,  name="Start-a-Petition" ),
    
    
    # ****************************************************************
    # User Itself Petitions
    # ****************************************************************
    path("view-petitions/",  views.User_Petitions,  name="Self-Petitions" ),
    
    
    # ****************************************************************
    # Submit a Petition Response 
    # ****************************************************************
    path("submit-a-response-petition/<int:petition_id>/", views.PetitionResponseFeedbackView, name="PetitionResponse"),


    # ****************************************************************
    # Delete Petition By A Global Admin
    # ****************************************************************
    path("delete-a-petition/<int:petition_id>/", views.DeletePetition, name="DeletePetition"),

    # ****************************************************************
    # Petition Detail View in case of no responses submitted
    # ****************************************************************  
    path("patition-detail-no-response/<int:petition_id>/", views.NoResponsePetitionDetailView, name="Petition_No_response"),


    # ****************************************************************
    # Edit Petition By A Global Admin
    # ****************************************************************
    path("petition/Edit/<int:petition_id>/", views.EditPetition, name="EditPetition"),


    # ****************************************************************
    # Set Petition Time Response 
    path("petition/set-time-response/<int:petition_id>", views.setPetitionTime, name="PetitionTimeResponse"),
    # ****************************************************************
    
    # **************************************PETITION URL(s)***************************************
    
    
    # ****************************************************************
    # Create a Commendation
    # ****************************************************************
    path("commendation_start/",  views.commendation_start,  name="Start-a-Commendation" ),
    
    # ****************************************************************
    # Commendations View
    # ****************************************************************
    url(r'^all-commendations/$', views.All_Commendations, name="all-commendations-url"),
    
    # Uer Commendation Response Feedback View URL
    path("submit-a-response-commendation/<int:commendation_id>/",
        views.CommendationResponseFeedbackView,
        name="CommendationResponse"),
    
    # User (Itself) Commendation View URL
    path("view-commendation/", 
        views.User_Commendation, 
        name="Self-Commendation"
    ),

    # Global Admin Petitons Responses URL
    path("view-peition-responses-admin-global", views.globalAdminResponses, name="globalAdminResponses_URL"),

    # Global Admin Commendations Responses URL
    path("view-commendation-responses-admin-global", views.globalAdminResponsesCommendations, name="globalAdminResponsesCommendations_URL"),


    # Approve Petition by Global Admin
    path("approve-petition/<int:petition_id>", views.approved_petition, name="approved_petition_URL"),
    
    path("approve/<int:petition_id>/", views.approved, name="approve-that-petition"),
    
    # Approve Commendation by Global Admin
    path("approve-commendation/<int:commendation_id>", views.approved_commendation, name="approved_commendation_URL"),
    

    # ****************************************************************
    # Specific Petition Responses View
    # ****************************************************************
    path("view-specific-petition-responses/<int:petition_id>", views.SpecificViewPetition, name="SpecificViewPetition_URL"),
    
    # Specific Commendation Responses View
    path("view-specific-Commendation-responses/<int:commendation_id>", views.SpecificViewCommendation, name="SpecificViewCommendation_URL"),

    # Petition Details View
    path('view-specific-peition/<int:petition_id>/', views.Petition_Details, name="Petition_Details"),
    

    # See Specific Petition Response View URL
    path("specific-petition-response/<int:petition_id>/", views.SpecificPetitonResponse, name="ViewSpecificPetitionResponse_URL"),
    
    # See Specific Commendation Response View URL
    path("specific-commendation-response/<int:commendation_id>/", views.SpecificCommendationResponse, name="ViewSpecificCommendationResponse_URL"),
    
    # Commendation Details View
    path('view-specific-commendation/<int:commendation_id>/', views.Commendation_Details, name="Commendation_Details"),
    
    # Petitions Live View URL (Both Auth and Unauth)
    path('live-petitions',
        views.LivePetitions,
        name="LivePetitions_URL"),
    
    path('live-search-petitions',
        views.searchPetition,
        name="LivePetitionsSearch_URL"),
    
    # Petitions Live Detail View URL (Both Auth and Unauth)
    path('live-petitions-deatil-view/<int:petition_id>/',
        views.LivePetitionsDetailView,
        name="LivePetitionsDetails_URL"),
    
    # Petitions Live Detail View Comment URL (Both Auth and Unauth)
    path('live-petitions-signature-view/<int:petition_id>/',
        views.LivePetitionsSignatureView,
        name="LivePetitionSignature_URL"),
    
    # Commendations Live View URL (Both Auth and Unauth)
    path('live-commendations',
        views.LiveCommendationsView,
        name="LiveCommendations_URL"),
    
    # Commendations Live Detail View URL (Both Auth and Unauth)
    path('live-commendation-deatil-view/<int:commendation_id>/',
        views.LiveCommendationsDetailView,
        name="LiveCommendationsDetails_URL"),
    
    # Commendation Live Detail View Comment URL (Both Auth and Unauth)
    path('live-commendation-signature-view/<int:commendation_id>/',
        views.LiveCommendationSignatureView,
        name="LiveCommendationSignature_URL"),
    
    
    # ****************************************************************
    # Delete Commendation by a global admin
    # ****************************************************************
    path("commendation/delete-commendation/<int:obj_id>", views.DeleteCommendation, name="DeleteCommendation"),
    
    # ****************************************************************
    # Edit Commendation Details by a global admin
    path('commendation/edit/<int:obj_id>', views.EditCommendation, name="EditCommendation"),
    # ****************************************************************
    # ------------------------------------ Web Specific Pages --------------------------------------
    
    # ****************************************************************
    # About Us
    # ****************************************************************
    path('about-us', 
        views.About,
        name="About"),


    # ****************************************************************
    # Our Teams
    # ****************************************************************
    path('our-team',views.TeamView,name="team"),
    
    
    # ****************************************************************
    # Get Help
    # ****************************************************************
    path('Get-Help', views.Help, name="Help"),
    
    
    # ****************************************************************
    # FAQ
    # ****************************************************************
    path('FAQs', views.FAQ, name="FAQ"),
    
    # ****************************************************************
    # Privacy Policy
    # ****************************************************************
    path('Privacy-Policy', views.Policy, name="Policy"),
    
    # ****************************************************************
    # Terms & Conditions
    # ****************************************************************
    path('Terms-&-Conditions', views.Terms, name="Term"),

    # ****************************************************************
    # Contact Us
    # ****************************************************************
    path('Contact-Us', views.Contact, name="Contact"),
    
    # ****************************************************************
    # Partner 
    # ****************************************************************
    path('partner', views.Partner, name="Partner"),
    
    
    # ****************************************************************
    # Create FAQ
    # ****************************************************************
    path("create-faq", views.CreateFAQ, name="CreateFAQ"),
    
    # ****************************************************************
    # Add Team Members
    # ****************************************************************
    path("add-team-members", views.addTeam, name="AddTeams"),

    # ****************************************************************
    # Add Banner to the website
    # ****************************************************************
    path("add-banner", views.addBanner, name="AddBanner"),
    # ************************************* Web Specific Pages **************************************
]