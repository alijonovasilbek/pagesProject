from  django.urls import  path
from  .views import HomePageView,AboutPageView,LoginPageView

urlpatterns=[
    path('login/',LoginPageView.as_view(),name='login'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('',HomePageView.as_view(),name='home'),
]

