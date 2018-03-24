from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('account/', views.AccountListView.as_view(), name='account'),
	path('events/', views.EventListView.as_view(), name='events'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),

]