from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView

from app36.models import ModelEmployee


class EmployeeDetails(ListView):
    model = ModelEmployee
    template_name = "index.html"
    context_object_name = "amp"

class EmployeeDelete(DeleteView):
    model = ModelEmployee
    success_url = "/ampdeleted/"

class EmployeeUpdate(UpdateView):
    model = ModelEmployee
    template_name = "update.html"
    fields = ['name','salary']
    success_url = "/ampupdated/"

