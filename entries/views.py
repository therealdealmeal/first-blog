from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

class HomeView(LoginRequiredMixin, ListView):
	model = Entry
	template_name = 'entries/index.html'
	context_object_name = "blog_entries"
	ordering = ['-entry_date']
	paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
	model = Entry
	template_name = 'entries/entry_detail.html'
