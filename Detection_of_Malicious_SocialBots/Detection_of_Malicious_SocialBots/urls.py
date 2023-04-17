"""Detection_of_Malicious_SocialBots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as clientview
from Detection_of_Malicious_SocialBots import settings
from Tweet_Server import views as Researchview
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', clientview.login, name="login"),
    url(r'^Register1/$', clientview.Register1, name="Register1"),
    url(r'^CreateTweet/$', clientview.CreateTweet, name="CreateTweet"),
    url(r'^Review/(?P<pk>\d+)/$', clientview.Review, name="Review"),
    url(r'^ViewAllTweets/$', clientview.ViewAllTweets, name="ViewAllTweets"),
    url(r'^Viewreviews/$', clientview.Viewreviews, name="Viewreviews"),
    url(r'^ratings/(?P<pk>\d+)/$', clientview.ratings, name="ratings"),
    url(r'^dislikes/(?P<pk>\d+)/$', clientview.dislikes, name="dislikes"),

    url(r'^ViewYourProfile/$', clientview.ViewYourProfile, name="ViewYourProfile"),

    url(r'^tweetserverlogin/$',Researchview.tweetserverlogin, name="tweetserverlogin"),
    url(r'viewallusers/$',Researchview.viewallusers,name="viewallusers"),

    url(r'^charts/(?P<chart_type>\w+)', Researchview.charts,name="charts"),
    url(r'^dislikeschart/(?P<dislike_chart>\w+)', Researchview.dislikeschart,name="dislikeschart"),
    url(r'^View_All_User_Tweets/$', Researchview.View_All_User_Tweets, name='View_All_User_Tweets'),
    url(r'^View_MalaciousSocialBots_Analysis/$', Researchview.View_MalaciousSocialBots_Analysis, name='View_MalaciousSocialBots_Analysis'),
     url(r'^View_MalaciousSocialBots_reviews/$', Researchview.View_MalaciousSocialBots_reviews, name="View_MalaciousSocialBots_reviews"),
    url(r'^View_Tweet_Bots_Analysis/$', Researchview.View_Tweet_Bots_Analysis,name="View_Tweet_Bots_Analysis"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
