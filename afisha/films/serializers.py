from rest_framework import serializers
from .models import Film


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film



class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        # fields = ['id', 'name', 'kp_rating', 'created_at', 'updated_at']
        # fields = '__all__'
        # exclude = ['is_active', 'updated_at']
        fields = 'id name kp_rating created_at'.split()


