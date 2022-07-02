from rest_framework import serializers
from .models import Job, JobSkill, Candidate, CandidateSkill

class JobSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSkill
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    skills = JobSkillSerializer(many=True, read_only=True)
  
    class Meta:
        model = Job
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True}
        }


class CandidateSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = CandidateSkill
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    candidate_skills = CandidateSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ('first_name','last_name', 'candidate_skills')


