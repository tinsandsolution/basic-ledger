from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True
    # )
    # username = serializers.CharField()
    # password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     email = validated_data.get('email')
    #     username = validated_data.get('username')

    #     if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
    #         raise serializers.ValidationError('User with this email or username already exists')

    #     instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
