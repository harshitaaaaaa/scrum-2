from django.shortcuts import render
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Project, Team


class ProjectListView(LoginRequiredMixin,   ListView):
    """
        Lists of Projects in a single view of a Specific Logged IN USER
    """
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = ['-title']
    paginate_by = 5

    def test_func(self):
        return True


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/project_create.html'


class ProjectDetailView(LoginRequiredMixin,  DetailView):
    """
        Details of the Project would have links to Detail Data
    """
    model = Project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'


class ProjectUpdateView(LoginRequiredMixin,  UpdateView):
    model = Project
    template_name = 'project/project_update.html'


class TeamListView(LoginRequiredMixin,  ListView):
    model = Team
    template_name = 'proeject/team_list.html'


class TeamCreateView(LoginRequiredMixin,  CreateView):
    model = Team
    template_name = 'project/team_create.html'


class TeamDetailView(LoginRequiredMixin,  DetailView):
    """
       Details of specific team in the website
    """
    model = Team
    template_name = 'project/team_detail.html'


class TeamUpdateView(LoginRequiredMixin,  UpdateView):
    """
        Update The Team Details 
    """
    model = Team
    template_name = 'project/team_update.html'


class TeamListAllView(LoginRequiredMixin,  ListView):
    """
    Lists all Teams in the whole website for Instructor's Mostly
    """
    model = Team
    template_name = 'project/team_listall.html'


class ProjectListAllView(LoginRequiredMixin,  ListView):
    """
    This view would list all teams in the whole website (mostly for )

    """
    model = Project
    template_name = 'project/project_listall.html'
