from django.utils.text import slugify 
from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.skill_name}'


class Candidate(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_skills')
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.candidate.first_name}:{self.skill_name}'