from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from job.models import Candidate, CandidateSkill, Job, JobSkill
from job.serializers import CandidateSerializer
# Create your views here.


@api_view(['GET'])
def find_candidates(request):

    if request.method == 'GET':

        job_slug = request.GET.get('job_slug', None)

        if job_slug == None:
            return Response({'detail': 'Job name not provided'}, status.HTTP_400_BAD_REQUEST)

        job = get_object_or_404(Job, slug=job_slug)
        job_skills = JobSkill.objects.filter(job=job).values_list('skill_name', flat=True)

        candidate_id = CandidateSkill.objects.filter(skill_name__in=job_skills).values_list('candidate', flat=True)
        
        relevant_candidates = []

        for id in set(candidate_id):
            candidate_skills =[]
            included_skills= CandidateSkill.objects.filter(candidate_id=id).values_list('skill_name', flat=True)

            for skill in included_skills:
                candidate_skills.append(skill)
            
            common_skills = list(set(job_skills) & set(candidate_skills))
    
            if (len(common_skills)>2):
                relevant_candidates.append(id)    


        candidate_queryset = Candidate.objects.filter(id__in=relevant_candidates)
        candidate_serializer = CandidateSerializer(candidate_queryset, many=True)
        
           
        return Response(candidate_serializer.data)
