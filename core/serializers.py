from rest_framework import serializers
from .models import Proposal


class ProposalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'title']

class ProposalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['title', 'description']
        
class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        field = ['id', 'title', 'description', 'photo']
        