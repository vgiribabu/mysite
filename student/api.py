from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import StaffSerializers, StudentAppSerializers, StudentRegSerializers, DepartmentSerializers
from.models import StudentApp, StudentReg, Staff, Department

# from rest_framework.authtoken.models import Token


class StudentAppView(APIView):
    def get(self, request):
        # import pdb;pdb.set_trace()
        users = StudentApp.objects.all()
        # token = Token.object.get(users=student).key
        # data['token'] = token
        serializer = StudentAppSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializers = StudentAppSerializers(data=request.data)
        if serializers.is_valid():
            return Response(serializers.validated_data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRegView(APIView):
    def get(self, request, format=None):
        users = StudentReg.objects.all()
        serializer = StudentRegSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentRegSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffView(APIView):
    def get(self, request, format=None):
        users = Staff.objects.all()
        serializer = StaffSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
