from django.urls import path
from . import views
from django.urls import include
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.index, name='index'),
	path('account/', views.AccountListView.as_view(), name='account'),
	path('events/', views.EventListView.as_view(), name='events'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
	path('form/', TemplateView.as_view(template_name='ZooMaps/form.html'), name='form'),
	path('contact/', TemplateView.as_view(template_name='ZooMaps/contact.html'), name='contact'),
]

urlpatterns += [   
    path('event/create', views.EventCreate.as_view(), name='create-event'),
    path('message/create', views.MessageCreate.as_view(), name='create-message'),
    path('rating/create', views.RatingCreate.as_view(), name='create-rating'),
]

