from rest_framework import serializers
from .models import Staff, StudentApp, StudentReg, Department


class StudentAppSerializers(serializers.ModelSerializer):

    class Meta:
        model = StudentApp
        fields = "__all__"

    def create(self, validated_data):
        return StudentApp.objects.create(**validated_data)


class StudentRegSerializers(serializers.ModelSerializer):

    class Meta:
        model = StudentReg
        fields = "__all__"

        def create(self, validated_data):
            return StudentReg.objects.create(**validated_data)

class StaffSerializers(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)


class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validated_data):
        return Department.objects.create(**validated_data)