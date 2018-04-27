from django.forms import ModelForm, CharField, Select, DateField, DateInput
from .models import Project

items = [
        ('Ongoing','Ongoing'), 
        ('Pending','Pending',),
        ('Completed','Completed',),
        ('Awaiting Payment', 'Awaiting Payment')]


class ProjectForm(ModelForm):
    status = CharField(
        max_length=50,
        widget=Select(choices=items, attrs={'class': 'status'})
        )
    date_started = DateField(
        required=False,
        widget=DateInput(attrs={'type': 'date'})
        )
    date_due = DateField(
        required=False,
        widget=DateInput(attrs={'type': 'date'})
        )


    class Meta:
        model = Project
        fields = ('client_name', 'project_type', 'status', 'team_lead', 'description', 'tools_needed', 'date_started', 'date_due')
