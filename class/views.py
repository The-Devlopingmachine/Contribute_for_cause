from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

# Alright let's just get to the meat of it by creating class based list views
class generic(LoginRequiredMixin,TemplateView):
    template_name = "class/base.html"

class Entrieslistview(LoginRequiredMixin,ListView):
    template_name = "class/home.html"
    model = Entry
    queryset = Entry.objects.all().order_by('-published_date')
    context_object_name = 'entries_list'

class Tablelistview(LoginRequiredMixin,ListView):
    templat_name = "class/table.html"
    model = Entry

def Entry_detail(request, pk):
    entry = Entry.objects.get(pk=pk)

    return render(request, "class/entry_detail.html", {"entry": entry})

def selected_students(request, pk):
    entry = Entry.objects.get(pk=pk)

    return render(request, "class/selected_students.html", {"entry": entry})
