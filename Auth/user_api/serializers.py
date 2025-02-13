from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)  # Ajoutez le champ email

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')  # Ajoutez email aux champs sérialisés
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user