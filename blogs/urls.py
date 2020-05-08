from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    
    # Blog List View URL
    url(r'^$',
        views.BlogList,
        name='list'
    ),
    
    # ****************************************************************
    # Blog Details
    # ****************************************************************
    url(r'^detail/(?P<slug>[-\w]+)$', views.BlogDetail, name='detail'),
    
    # Blog Search View URL
    url(r'^search/',
        views.search,
        name='search'
    ),
    
    # BLog Post Form View URL
    url(r'^create-a-blog/',
        views.blogFormView,
        name='blog'
    ),
    
    # Blog Comment Reply View URL
    url(r'^reply/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.ReplyPage,
        name='reply'
    ),
    
    # Self Blogs 
    url(r'^self-blogs/$', views.self_Blogs, name="self_blogs_url"),
    
    # Editing BLog
    path('edit-blog/<int:blog_id>', views.blogFormViewEditing, name="blog_editing"),
    
    
    # ****************************************************************
    # Assign a blog by a global admin
    # ****************************************************************
    path("assign-a-blog", views.AssignBlog, name="Assign"),
    
    
    # ****************************************************************
    # Approve Current Publish Project
    # ****************************************************************
    path("approve-blog/<int:blog_id>/", views.Approve, name="Approve"),
    
    
        
    # ****************************************************************
    # Disapprove Current Publish Project
    # ****************************************************************
    path("disapprove-blog/<int:blog_id>/", views.Disapprove, name="Disapprove"),


]