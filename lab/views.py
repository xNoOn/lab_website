from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class LabListView(LoginRequiredMixin, TemplateView):
    template_name = 'lab/lab_home.html'


class DiagramsListView(LoginRequiredMixin, TemplateView):
    template_name = 'lab/diagrams_home.html'
