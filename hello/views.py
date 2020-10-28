import re
from re import match  #importing regex module
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import locale
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView


class HomeListView(ListView):
    """"renders the home page with the items in the database """
    model = LogMessage
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

# Create your views here.
def home(request):
    return render(request,"hello/home.html")
    #ResponseStr = "Hello SolmazStr!"
    #return HttpResponse(ResponseStr)

def about(request):
    return render(request,"hello/about.html")

def contact(request):
    return render(request,"hello/contact.html")

def hello_there(request,name):
    locale.setlocale(locale.LC_ALL,'tr')
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+",name);

    if match_object:
        clean_name=match_object.group(0)
    else:
        clean_name="Friend"
    content = "Hello there, " + clean_name + " It's " + formatted_now
    print("offf")
    return HttpResponse(content)


def hello_withtemplate(request,name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form}) 