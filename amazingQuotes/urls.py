from django.urls import path
from . import views
from blog.views import PostViews

app_name = 'home'
urlpatterns = [
    path('', views.home_view, name='mainPage'),
    path('about', views.about_us, name='about'),
    path('blog', PostViews.post_view, name='blog'),
    path('post/<id>', PostViews.post_detail, name='single_post'),
    path('contact-us', views.contact, name='contact'),
    path('events', views.events, name='events'),
    path('event/<id>', views.event, name='event'),
    path('ourproducts', views.products, name='products'),
    path('ourproduct/<id>', views.product, name='product'),
    path('coachinglist', views.coaching_list, name='coachinglist'),
    path('coaching/<id>', views.coaching, name='coaching')
]