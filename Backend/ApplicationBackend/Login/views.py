from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serialiser import UserAccountCreateSerialiser


#@method_decorator(csrf_exempt, name='dispatch')
class CreateUserAccount(APIView):

    def post(self,request):
        seriaizer = UserAccountCreateSerialiser(data = request.data)

        response_data = {
            "errors" : "null",
            "data" : "null"
        }

        if seriaizer.is_valid():
            user = seriaizer.save()
            refresh = RefreshToken.for_user(user)
            response_data['data'] = {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
            response_status = status.HTTP_201_CREATED
            return Response(response_data,status=response_status)

        response_data['errors'] = seriaizer.errors
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

def create_user_form(request):
    return render(request, 'Login/create_user.html')