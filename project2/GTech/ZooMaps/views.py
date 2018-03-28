from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

from .models import User, Event, Tag, CommentEvent, MessageEvent

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_user=User.objects.all().count()
    num_event=Event.objects.all().count()
    num_tag=Tag.objects.all().count()
    num_comment=CommentEvent.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_user':num_user,'num_event':num_event,'num_tag':num_tag,'num_comment':num_comment},
    )
    
from django.views import generic
from itertools import chain
from datetime import datetime, timedelta

class AccountListView(generic.ListView):
    model = User
    template_name = 'ZooMaps/account.html'
    def get_queryset(self):
    	return list(chain(User.objects.filter(username='GTech'), Event.objects.filter(attendees__in = User.objects.filter(username='GTech'), endDate__gte = (datetime.now()))))
 
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
    	
class EventListView(generic.ListView):
    model = Event
    paginate_by=4
    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	query = self.request.GET.get('q', None)
    	if query:
    		list_events= Event.objects.filter(name__contains=query)
    		paginator = Paginator(list_events, self.paginate_by)
    		page = self.request.GET.get('page')
    		try:
    			events = paginator.page(page)
    		except PageNotAnInteger:
    			events = paginator.page(1)
    		except EmptyPage:
    			events = paginator.page(paginator.num_pages)
    		context['event_list'] =events
    	else:
    		list_events = Event.objects.all()
    		paginator = Paginator(list_events, self.paginate_by)
    		page = self.request.GET.get('page')
    		try:
    			events = paginator.page(page)
    		except PageNotAnInteger:
    			events = paginator.page(1)
    		except EmptyPage:
    			events = paginator.page(paginator.num_pages)
    		context['event_list'] =events
    	return context
    
class EventDetailView(generic.DetailView):
	model = Event
	paginate_by = 1
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['event'] = self.object
		context['rating_list'] = CommentEvent.objects.filter(event=self.object)
		context['message_list'] = MessageEvent.objects.filter(event=self.object)
		return context

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    initial={'startDate': datetime.now(), 'endDate': datetime.now()+ timedelta(hours=4)}

