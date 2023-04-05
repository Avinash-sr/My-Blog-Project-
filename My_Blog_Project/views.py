from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))