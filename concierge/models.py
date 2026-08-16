from django.db import models

class GenerationJob(models.Model):
    job_id = models.CharField(max_length=100, unique=True)
    model_selection = models.CharField(max_length=100, default='llama3.2')
    stratified_flag = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='Pending')
    stdout_logs = models.TextField(blank=True, null=True)
    stderr_logs = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job {self.job_id} - {self.status}"


class GeneratedTask(models.Model):
    job = models.ForeignKey(GenerationJob, related_name='tasks', on_delete=models.CASCADE)
    task_id = models.CharField(max_length=100)
    task_type = models.CharField(max_length=50, default='standard')
    stratum = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task {self.task_id} ({self.task_type})"


class TravelItinerary(models.Model):
    destination = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    interests = models.TextField()
    itinerary_details = models.TextField(blank=True, null=True)
    lowest_cost_found = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip to {self.destination} ({self.start_date})"