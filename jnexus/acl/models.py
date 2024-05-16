# Create your models here.
from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Hashed password for security
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    headline = models.CharField(max_length=255)
    summary = models.TextField()
    profile_picture = models.URLField()
    cover_photo = models.URLField()
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    current_position = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100)
    social_media_accounts = models.JSONField(default=list)
    # Education relationship is defined as a ForeignKey to support multiple education entries per user
    # Experience relationship is defined as a ForeignKey to support multiple experience entries per user

class Resource(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    permissions = models.CharField(max_length=10, choices=[('read', 'Read'), ('write', 'Write')])

class Experience(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Education(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Skill(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    endorsements = models.IntegerField(default=0)

class Connection(models.Model):
    user = models.ForeignKey(Users, related_name='initiated_connections', on_delete=models.CASCADE)
    contact = models.ForeignKey(Users, related_name='received_connections', on_delete=models.CASCADE)
    date_connected = models.DateTimeField(auto_now_add=True)

class Recommendation(models.Model):
    user = models.ForeignKey(Users, related_name='received_recommendations', on_delete=models.CASCADE)
    author = models.ForeignKey(Users, related_name='authored_recommendations', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Endorsement(models.Model):
    user = models.ForeignKey(Users, related_name='received_endorsements', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    endorser = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
