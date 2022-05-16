from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


@api_view(['post'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            name = validated_data.get('name')
            major = validated_data.get('major')
            age = validated_data.get('age')
            is_woman = validated_data.get('is_woman')
            Student.objects.create(
                name=name,
                major=major,
                age=age,
                is_woman=is_woman
            )
            return Response(status=200)
        else:
            return Response(status=400)


