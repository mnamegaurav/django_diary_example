from django.shortcuts import render,redirect
from .models import Notes
from .forms import TextForm
# Create your views here.

def index(request):
    template_name='diaryapp/index.html'
    notes = Notes.objects.order_by('-time')
    context = { 'notes' : notes}
    return render(request,template_name,context)


def add(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm()
    context = {'form':form}
    template_name='diaryapp/add.html'
    return render(request,template_name,context)
