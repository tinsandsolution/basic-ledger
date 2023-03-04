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
        fields = ()
        extra_kwargs = {
            'account_owner': {'write_only': True},
            'account_number': {'write_only': True},
        }

    def create(self, validated_data):
        # print(validated_data,"\n\n\n")
        # password = validated_data.pop('password', None)
        # email = validated_data.get('email')
        # account_owner = validated_data.get('account_owner')

        # if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
        #     raise serializers.ValidationError('User with this email or username already exists')

        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        # if password is not None:
        #     instance.set_password(password)
        instance.save()
        return instance

class AllAccountsSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True
    # )
    # username = serializers.CharField()
    # password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ('id','account_number','account_owner','current_balance')

    def create(self, validated_data):
        # print(validated_data,"\n\n\n")
        # password = validated_data.pop('password', None)
        # email = validated_data.get('email')
        # account_owner = validated_data.get('account_owner')

        # if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
        #     raise serializers.ValidationError('User with this email or username already exists')

        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        # if password is not None:
        #     instance.set_password(password)
        instance.save()
        return instance
