from rest_framework import serializers
from users.models import Sneaker


class SneakerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model= Sneaker

        fields = ('sneakerID',
                  'authorID',
                  'title',
                  'body',
                  'image',
                  'sneakerReleaseDate',
                  'sneakerPublishDate',
                  'color',
                  'content')
        read_only_fields = ('authorID',)
