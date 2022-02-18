from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .models import PastedText
from .forms import PastedTextForm
from datetime import datetime, timezone

# Create your views here.


def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    pastedtexts = PastedText.objects.all()
    for pastedtext in pastedtexts:
        diff = (datetime.now(timezone.utc) -
                pastedtext.created_at).total_seconds()

        if diff > 24*3600:
            pastedtext.delete()
    pastedtexts = PastedText.objects.filter(
        created_by=request.user).order_by('created_at')
    return render(request, 'home.html', {'pastedtexts': pastedtexts}) #dictionary
 

def pastetext(request):

    if request.user.is_anonymous:
        return redirect('/login')
    form = PastedTextForm()
    if request.method == 'POST':
        text = request.POST.get('text')
        password = request.POST.get('password')
        new_pastedtext = PastedText(
            text=text, password=password, created_by=request.user)
        new_pastedtext.save()
        return redirect(f'/showtext/{new_pastedtext.id}')
    return render(request, 'pastetext.html', {'form': form})


def showtext(request, pk):
    pastedtexts = PastedText.objects.all()
    for pastedtext in pastedtexts:
        diff = (datetime.now(timezone.utc) -
                pastedtext.created_at).total_seconds()
        if diff > 24*3600:
            pastedtext.delete()
    if request.method == 'POST':  #recipent side
        password = request.POST.get('password')
        pastedtext = PastedText.objects.get(pk=pk)
        if pastedtext.password == password:
            return render(request, 'output.html', {'pastedtext': pastedtext})
        return render(request, 'recipent.html', {'pk': pk})

    pastedtext = PastedText.objects.get(pk=pk)
    if (request.user) == (pastedtext.created_by):
        return render(request, 'output.html', {'pastedtext': pastedtext})

    return render(request, 'recipent.html', {'pk': pk})


def deletetext(request, pk):
    pastedtext = PastedText.objects.get(pk=pk)
    if request.user == pastedtext.created_by:
        pastedtext.delete()
    return redirect('/')


def renewexpiry(request, pk):
    pastedtext = PastedText.objects.get(pk=pk)
    if request.user == pastedtext.created_by:
        from datetime import datetime
        pastedtext.created_at = datetime.now()
        pastedtext.save()
    return redirect('/')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
    return render(request, 'login.html')


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already in use')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(
                username=username, password=password)
            return redirect('/login')
    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')
