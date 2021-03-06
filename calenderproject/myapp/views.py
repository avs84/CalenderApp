from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from .forms import EntryForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    entries = Entry.objects.all().order_by('date')
    return render(request, 'myapp/index.html', {'entries': entries})

@login_required
def calendar(request):
    entries = Entry.objects.all().filter(author=request.user).order_by('date')
    return render(request, 'myapp/calendar.html', {'entries': entries})

@login_required
def details(request, pk):
    try:
        entry = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'myapp/details.html', {'entry': entry})

@login_required
def add(request):

    if request.method == "POST":
        form = EntryForm(request.POST)

        if form.is_valid():

            name= form.cleaned_data['name']
            date= form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date=date,
                description=description,
                author=request.user
            ).save()

            return HttpResponseRedirect('/calendar')
    else:
        form = EntryForm()

    return render(request, 'myapp/form.html', {'form': form})

@login_required
def delete(request, pk):
    print ("PK:")

    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calendar')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

