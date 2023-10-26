from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, SecurityIncidentForm, SecurityGroupForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import SecurityIncident, SecurityGroup
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.contrib.auth.models import User 
from django.views.generic import DetailView

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use AuthenticationForm
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a dashboard or the desired page.
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
    # Retrieve data for the dashboard
    total_incidents = SecurityIncident.objects.count()
    total_users = User.objects.count()  # Use the default User model
    total_groups = SecurityGroup.objects.count()
    
    # Get the latest security incident title
    latest_incident = SecurityIncident.objects.order_by('-timestamp').first().title if total_incidents > 0 else "N/A"
    
    # Get the latest security group name
    latest_group = SecurityGroup.objects.order_by('-id').first().name if total_groups > 0 else "N/A"
    
    context = {
        'total_incidents': total_incidents,
        'total_users': total_users,
        'total_groups': total_groups,
        'latest_incident': latest_incident,
        'latest_group': latest_group,
        # Add more context variables here
    }

    return render(request, 'dashboard/dashboard.html', context)

class SecurityIncidentReportView(TemplateView):
    template_name = 'reports/security_incident_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve data for the report
        total_incidents = SecurityIncident.objects.count()
        total_users = User.objects.count()  # Use the default User model
        total_groups = SecurityGroup.objects.count()
        latest_incident = SecurityIncident.objects.order_by('-timestamp').first().title if total_incidents > 0 else "N/A"
        latest_group = SecurityGroup.objects.order_by('-id').first().name if total_groups > 0 else "N/A"
        
        context['total_incidents'] = total_incidents
        context['total_users'] = total_users
        context['total_groups'] = total_groups
        context['latest_incident'] = latest_incident
        context['latest_group'] = latest_group
        
        # Add more data as needed for reporting
        return context

class SecurityGroupListView(ListView):
    model = SecurityGroup
    template_name = 'security_groups/group_list.html'
    context_object_name = 'groups'

class SecurityGroupCreateView(CreateView):
    model = SecurityGroup
    template_name = 'security_groups/group_form.html'
    form_class = SecurityGroupForm
    success_url = '/groups/'

class SecurityGroupUpdateView(UpdateView):
    model = SecurityGroup
    template_name = 'security_groups/group_form.html'
    form_class = SecurityGroupForm
    success_url = '/groups/'

class SecurityGroupDeleteView(DeleteView):
    model = SecurityGroup
    template_name = 'security_groups/group_confirm_delete.html'
    success_url = '/groups/'

@login_required
def report_incident(request):
    if request.method == 'POST':
        form = SecurityIncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.save()
            return redirect('incident_list')
    else:
        form = SecurityIncidentForm()
    return render(request, 'incident/report_incident.html', {'form': form})

@login_required
def incident_list(request):
    incidents = SecurityIncident.objects.all()
    return render(request, 'incident/incident_list.html', {'incidents': incidents})

class SecurityIncidentDetailView(DetailView):
    model = SecurityIncident
    template_name = 'incident/incident_detail.html'  # Create this template

class SecurityGroupDetailView(DetailView):
    model = SecurityGroup
    template_name = 'security_groups/group_detail.html'  


def user_logout(request):
    logout(request)
    return redirect('home')