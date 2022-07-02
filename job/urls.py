from django.urls import path

from job.views import find_candidates

urlpatterns = [
    path('finder',find_candidates, name='find_candidates'),
]