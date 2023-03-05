from rest_framework import serializers
from .models import Account, Transaction

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

class TransactionSerializer(serializers.ModelSerializer):
    note = serializers.CharField(max_length=50)


    class Meta:
        model = Transaction
        fields = ('transaction_type','amount','note')

    '''
    {
      "account_id": 1,
      "transaction_type": "DEBIT",
      "note": "monthly job salary",
      "amount": 7750
    }
    '''
    def validate_note(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Note cannot be empty")
        if len(value) > 500:
            raise serializers.ValidationError("Note cannot be more than 50 characters")
        return value

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount cannot be negative")
        if (len(str(value).split('.')[1]) > 2):
            raise serializers.ValidationError("Amount cannot have more than 2 decimal places")
        return value

    def validate_transaction_type(self, value):
        if value not in ['DEBIT','CREDIT']:
            raise serializers.ValidationError("Transaction type must be either DEBIT or CREDIT")
        return value

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
