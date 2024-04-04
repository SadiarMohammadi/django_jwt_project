from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def hello_api(request):
    data = {
        "message": "Hello Django Rest Framework"
    }
    return Response(data)


class HelloApi2(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "message": "Hello Django Rest Framework - class based view"
        }
        return Response(data)
