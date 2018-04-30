from django.urls import path
from . import views
from django.urls import include
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name='index'),
	path('account/', views.AccountListView.as_view(), name='account'),
	path('events/', views.EventListView.as_view(), name='events'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
	path('contact/', TemplateView.as_view(template_name='ZooMaps/contact.html'), name='contact'),
    path('user/', include('django.contrib.auth.urls')),
    path('event/create', views.EventCreate.as_view(), name='create-event'),
    path('event/<int:pk>/rate', views.rate_event, name='rate-event'),
    path('event/<int:pk>/message', views.message_event, name='message-event'),
    path('event/<int:pk>/attend', views.attend_event, name='attend-event'),
    path('event/<int:pk>/unattend', views.unattend_event, name='unattend-event'),
    path('account/messages', views.MessageListView.as_view(), name='messages'),
    path('account/ratings', views.RatingListView.as_view(), name='ratings'),
	path('account/future', views.MyFutureEventListView.as_view(), name='my-future-events'),
	path('account/past', views.MyPastEventListView.as_view(), name='my-past-events'),
	path('account/current', views.MyCurrentEventListView.as_view(), name='my-current-events'),
    path('event/<int:pk>/messages', views.EventDetailMessageView.as_view(), name='event-messages'),
    path('event/<int:pk>/ratings', views.EventDetailRatingView.as_view(), name='event-ratings'),
    path('events/future', views.FutureEventListView.as_view(), name='future-events'),
    path('events/ongoing', views.OngoingEventListView.as_view(), name='ongoing-events'),
    path('events/best_rated', views.BestRatedEventListView.as_view(), name='best-rated-events'),
    path('logon/', views.logOn, name='log-on'),
]
