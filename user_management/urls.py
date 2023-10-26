from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('groups/', views.SecurityGroupListView.as_view(), name='security_group_list'),
    path('report/', views.report_incident, name='report_incident'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/security_incident/', views.SecurityIncidentReportView.as_view(), name='security_incident_report'),
    path('groups/create/', views.SecurityGroupCreateView.as_view(), name='security_group_create'),
    path('groups/<int:pk>/update/', views.SecurityGroupUpdateView.as_view(), name='security_group_update'),
    path('groups/<int:pk>/delete/', views.SecurityGroupDeleteView.as_view(), name='security_group_delete'),
    path('incident/<int:pk>/', views.SecurityIncidentDetailView.as_view(), name='incident_detail'),
    path('group/<int:pk>/', views.SecurityGroupDetailView.as_view(), name='group_detail'),
]
