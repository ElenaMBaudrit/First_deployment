from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!

    url(r'^Quotes/register$', views.register),

    url(r'^Quotes/dashboard$', views.dashboard),
    
    url(r'^Quotes/new_user$', views.new_user),
    
    url(r'^Quotes/login$', views.login),

    url(r'^Quotes/logout$', views.logout),

    url(r'^Quotes/posts$', views.posts),

    url(r'^Quotes/create_post$', views.create_post),

    url(r'^Quotes/add_to_list/?P<user_id>\+$', views.add_to_list),

    url(r'^Quotes/remove_from_list$', views.remove_from_list)

]