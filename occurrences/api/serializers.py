from django.contrib.auth import get_user_model
from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

from occurrences.choices import STATUS_CHOICES
from occurrences.models import Category, Occurrence

User = get_user_model()


class OccurrenceSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), read_only=False, required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), read_only=False)
    location = PointField()
    description = serializers.CharField(required=False, trim_whitespace=True, allow_blank=True)
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default="to_validate")

    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'category', 'created', 'description', 'location', 'status', 'updated')

    def __init__(self, *args, **kwargs):
        super(OccurrenceSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method == 'PUT':
            self.fields['category'].required = False
            self.fields['location'].required = False
        if self.context['request'].method == 'POST' and not self.context['request'].user.is_superuser:
            self.fields['status'] = serializers.ChoiceField(
                choices=(('to_validate', 'Occurrence Waiting for Validation'),), default="to_validate")

    def save(self, **kwargs):
        self.validated_data['author'] = kwargs.get('author', None)
        return Occurrence.objects.create(**self.validated_data)

    def update(self, instance, validated_data):
        if self.context['request'].user.is_superuser:
            instance.status = validated_data.get('status', instance.status)
        instance.category = validated_data.get('category', instance.category)
        instance.location = validated_data.get('location', instance.location)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
