from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field fro trsting our APiview"""

    name = serializers.CharField(max_length=10)

    