from django.contrib import admin

from job.models import Candidate, CandidateSkill, Job, JobSkill

# Register your models here.

admin.site.register(Job)
admin.site.register(JobSkill)
admin.site.register(Candidate)
admin.site.register(CandidateSkill)