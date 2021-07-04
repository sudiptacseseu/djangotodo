from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, "Item has been added to the list!")
            return render(request, 'home.html', {'all_items': all_items})
            # return HttpResponseRedirect('/')
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    return render(request, 'about.html', {})


def delete(request, id):
    item = List.objects.get(pk=id)
    item.delete()
    messages.success(request, "Item has been deleted successfully!")
    return redirect('home')


def crossoff(request, id):
    item = List.objects.get(pk=id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, id):
    item = List.objects.get(pk=id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, id):
    if request.method == "POST":
        todo_item = List.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item has been edited to the list!")
            return redirect('home')
    else:
        todo_item = List.objects.get(pk=id)
        return render(request, 'edit.html', {'todo_item': todo_item})
