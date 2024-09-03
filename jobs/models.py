from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    company_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.company_name
    
class JobPosition(models.Model):
    position = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    salary = models.DecimalField(max_digits=15, decimal_places=0)
    remote = models.BooleanField()
    full_time = models.BooleanField()
    part_time = models.BooleanField()
    company = models.ForeignKey(Organization, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.position}: {self.expiration_date}"


class JobApplication(models.Model):
    requested_position = models.ForeignKey(to="jobs.JobPosition", on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)


class JobRequest(models.Model):
    requested_job = models.ForeignKey(to="jobs.JobPosition", on_delete=models.CASCADE)
    job_seeker_sender = models.ForeignKey(to="job_seeker.JobSeeker", on_delete=models.CASCADE)
