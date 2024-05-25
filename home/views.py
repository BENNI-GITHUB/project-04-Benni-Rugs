from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribeForm

def index(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed!')
            return redirect('home')
    else:
        form = SubscribeForm()
    return render(request, 'home/index.html', {'form': form})

