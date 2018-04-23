from django.db import models
from datetime import date

class Project(models.Model):
    client_name = models.CharField(max_length = 200)
    description = models.TextField()
    project_type = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)
    team_lead = models.CharField(max_length = 200)
    date_started = models.DateField(blank=True, null=True)
    date_due = models.DateField()
    tools_needed = models.TextField()
    date_completed = models.DateField(blank=True, null=True)


    def completed(self):
        self.date_completed = date.today()
        self.status = "completed"
        self.save()

    def started(self):
        self.date_started = date.today()
        self.status = "Ongoing"
        self.save()

    def __str__(self):
        return self.client_name
