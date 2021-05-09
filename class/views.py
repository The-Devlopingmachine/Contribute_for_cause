from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from .models import Entry
# Create your views here.

# Alright let's just get to the meat of it by creating class based list views
class generic(TemplateView):
    template_name = "class/base.html"

class Entrieslistview(ListView):
    template_name = "class/home.html"
    model = Entry
    context_object_name = 'entries_list'

def Entry_detail(request, pk):
    entry = Entry.objects.get(pk=pk)

    return render(request, "class/entry_detail.html", {"entry": entry})

def selected_students(request, pk):
    entry = Entry.objects.get(pk=pk)

    return render(request, "class/selected_students.html", {"entry": entry})
