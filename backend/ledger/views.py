from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountSerializer, AllAccountsSerializer, TransactionSerializer, AccountTransactionsSerializer
from .models import Account, Transaction
from django.db import models
from decimal import Decimal

# Create your views here.
# this a view to get all accounts by the current user
class AccountCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format='json'):
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        print('at least were getting through here\n\n\n')
        if serializer.is_valid():

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
    def get(self, request, account_id, format='json'):
        '''
        get balance of a single account
        '''
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error' : "Account couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
        if request.user.id != account.account_owner.id:
            return Response({'error' : "You don't have permission to access this account"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = AllAccountsSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, account_id, format='json'):
        '''
        update balance of a single account
        '''
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error' : "Account couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
        if request.user.id != account.account_owner.id:
            return Response({'error' : "You don't have permission to access this account"}, status=status.HTTP_401_UNAUTHORIZED)

        if request.data['transaction_type'] == "DEBIT" and account.current_balance < request.data['amount']:
            return Response({'error' : "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)


        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            if request.data['transaction_type'] == "DEBIT":
                account.current_balance -= Decimal(request.data['amount'])
            if request.data['transaction_type'] == "CREDIT":
                account.current_balance += Decimal(request.data['amount'])
            account.save()
            serializer.save(account_id=account)
            # gets id and account id of the transaction
            transaction = Transaction.objects.last()
            return Response(dict(serializer.data, **{"id" : transaction.id, "account_number" : transaction.account_id.account_number}), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### this is for getting acccount transactions
class AccountTransactions(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, account_id, format='json'):
        '''
        get transactions of a single account
        '''
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error' : "Account couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
        if request.user.id != account.account_owner.id:
            return Response({'error' : "You don't have permission to access this account"}, status=status.HTTP_401_UNAUTHORIZED)
        transactions = Transaction.objects.filter(account_id=account_id)
        serializer = AccountTransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

### this is for getting all transactions by the current user
class AllTransactions(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format='json'):
        '''
        get all transactions by the current user
        '''
        accounts = Account.objects.filter(account_owner=request.user)
        transactions = Transaction.objects.filter(account_id__in=accounts)
        serializer = AccountTransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
