from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
	path('', views.index, name='index'),
	path('account/', views.AccountListView.as_view(), name='account'),
	path('events/', views.EventListView.as_view(), name='events'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
	path('form/', include('django.contrib.flatpages.urls'),name='form'),
]