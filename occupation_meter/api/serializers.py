from rest_framework import serializers
from .models import CountRequest


class CountRequestSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CountRequest
        fields = ('id', 'source_endpoint', 'source_bucket', 'source_folder',
                  'source_filename', 'date_created', 'date_modified')
        read_only_fields = ('count', 'date_created', 'date_modified')