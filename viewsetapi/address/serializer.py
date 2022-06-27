from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Parent,Children

class ParentSerializer(ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class ChildrenSerializer(ModelSerializer):
    parent_name = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=Parent.objects.all()
    )
    class Meta:
        model = Children
        fields = '__all__'
        