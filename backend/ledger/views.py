from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountSerializer, AllAccountsSerializer
from .models import Account
from django.db import models

# Create your views here.
# this a view to get all accounts by the current user
class AccountCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format='json'):
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        print('at least were getting through here\n\n\n')
        if serializer.is_valid():
            print('valid\n\n\n')

            row_with_highest_account = Account.objects.last()
            print(row_with_highest_account,"\n\n\n")
            account_number = "0000000000000001"
            if row_with_highest_account != None:
                account_number = str(int(row_with_highest_account.account_number) + 1)
                print(int(row_with_highest_account.account_number),"\n\n\n")
                leftover_zeros = 16 - len(account_number)
                account_number = "0" * leftover_zeros + account_number
            account = serializer.save(account_owner=request.user,account_number=account_number)
            if account:
                json = serializer.data
                account = Account.objects.get(account_number=account_number)
                return Response({'account_number' : account.account_number}, status=status.HTTP_201_CREATED)
        return Response({"hey" : "hey"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format='json'):
        '''
        get all accounts by the current user
        '''
        accounts = Account.objects.filter(account_owner=request.user)
        serializer = AllAccountsSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccountManager(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, account_number, format='json'):
        '''
        get balance of a single account
        '''
        account = Account.objects.get(account_number=account_number)
        serializer = AllAccountsSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, account_number, format='json'):
        '''
        update balance of a single account
        '''
        account = Account.objects.get(account_number=account_number)
        serializer = AllAccountsSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
