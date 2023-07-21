from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, through='TeamMembership')


class TeamMembership(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Folder(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', blank=True)


class Item(models.Model):
    title = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    extra_properties = models.JSONField(default=dict)
    notes = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ItemHistory(models.Model):
    ACTION_CHOICES = (
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
