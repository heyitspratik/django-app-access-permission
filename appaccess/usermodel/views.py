from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            email = request.data['email']
            password = request.data['password']
            dob = request.data['dob']
            user = User.objects.create_user(username=username, email=email, password=password, dob=dob, is_active=True)
            data = {"user_id":user.id,"username":username, "email":email, "dob":dob,"email_verified":user.email_verified}
            return Response(
                    {"status": 1, "message": "Congrats, Account created successfully", "data": data})
        if "username" in serializer.errors:
            return Response({"status": 0, "message": "username - " + serializer.errors['username'][0]})
        if "email" in serializer.errors:
            if serializer.errors['email'][0] == "user with this email address already exists.":
                return Response({"status": 0, "message": "Email is already registered"})
            return Response({"status": 0, "message": "email - " + serializer.errors['email'][0]})
        if "password" in serializer.errors:
            return Response({"status": 0, "message": "passowrd - " + serializer.errors['password'][0]})
        if "dob" in serializer.errors:
            return Response({"status": 0, "message": "dob - " + serializer.errors['dob'][0]})
        return Response(serializer.errors)



class LogInViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def get_user(self, email):
        try:
            user = User.objects.get(email=email)
            return user
        except:
            return 0

    def create(self, request):
        print("here111....")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            password = request.data['password']
            user = self.get_user(email)
            if user:
                print("here2222....")
                if user.is_active:
                    print("here3333....")
                    auth_status = authenticate(email=email, password=password)
                    if auth_status:
                        print("here4444....")
                        data = {"user_id":user.id,"username":user.username, "email":email, "dob":user.dob,"email_verified":user.email_verified}
                        return Response({"status": 1, "message": "You have logged in successfully", "data": data})
                    else:
                        return Response({"status": 0, "message": "Unable to log in, please check your password"})
                else:
                    return Response({"status": 0, "message": "Please verify the link sent to your email to log in"})
            else:
                return Response({"status": 0, "message": "Email is not registered"})

        if "email" in serializer.errors:
            print("my.....")
            return Response({"status": 0, "message": "email - " + serializer.errors['email'][0]})
        if "password" in serializer.errors:
            return Response({"status": 0, "message": "password - " + serializer.errors['password'][0]})
        return Response(serializer.errors)

