from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    priority = models.IntegerField(default=1)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class user(models.Model):
    pass