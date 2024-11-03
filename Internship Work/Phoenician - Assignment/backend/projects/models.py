from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, related_name='details', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    items = models.JSONField()  # Store the nested items data as JSON

    def __str__(self):
        return f"{self.project.name} - {self.title}"
