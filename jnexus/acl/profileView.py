from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users
from .serializers import UsersSerializer, SocialMediaAccountSerializer ,CreateUsersSerializer 

class UserList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    def get_user(self, username):
        try:
            return Users.objects.get(username=username)
        except Users.DoesNotExist:
            return None

    def get(self, request, username):
        user = self.get_user(username)
        if user:
            serializer = UsersSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, username):
        user = self.get_user(username)
        if user:
            serializer = UsersSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, username):
        user = self.get_user(username)
        if user:
            serializer = UsersSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, username):
        user = self.get_user(username)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class SocialMediaAccountList(APIView):
    def get_user(self, username):
        try:
            return Users.objects.get(username=username)
        except Users.DoesNotExist:
            return None

    def post(self, request, username):
        user = self.get_user(username)
        if user:
            serializer = SocialMediaAccountSerializer(data=request.data)
            if serializer.is_valid():
                social_media_accounts = user.social_media_accounts
                social_media_accounts.append(serializer.validated_data)
                user.social_media_accounts = social_media_accounts
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

class SocialMediaAccountDetail(APIView):
    def get_user(self, username):
        try:
            return Users.objects.get(username=username)
        except Users.DoesNotExist:
            return None

    def get_social_media_account(self, user, index):
        try:
            return user.social_media_accounts[index]
        except (IndexError, TypeError):
            return None

    def get(self, request, username, index):
        user = self.get_user(username)
        if user:
            social_media_account = self.get_social_media_account(user, index)
            if social_media_account:
                serializer = SocialMediaAccountSerializer(social_media_account)
                return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, username, index):
        user = self.get_user(username)
        if user:
            social_media_account = self.get_social_media_account(user, index)
            if social_media_account:
                serializer = SocialMediaAccountSerializer(social_media_account, data=request.data)
                if serializer.is_valid():
                    user.social_media_accounts[index] = serializer.validated_data
                    user.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, username, index):
        user = self.get_user(username)
        if user:
            social_media_account = self.get_social_media_account(user, index)
            if social_media_account:
                serializer = SocialMediaAccountSerializer(social_media_account, data=request.data, partial=True)
                if serializer.is_valid():
                    user.social_media_accounts[index] = serializer.validated_data
                    user.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, username, index):
        user = self.get_user(username)
        if user:
            social_media_account = self.get_social_media_account(user, index)
            if social_media_account:
                del user.social_media_accounts[index]
                user.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
