from django.conf.urls import patterns, url

from .views import MainView

urlpatterns = patterns('home.views',

    #Home
    url(r'^', MainView.as_view()),
    
)
