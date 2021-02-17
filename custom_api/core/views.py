from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post

# Create your views here.


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'name':'John Wick',
        'Known for': 'BoogeyMan',
        'age':32,
        'profession':'Professional Killer',
        'skills': 'killing in a brutal way',
        'weak points': 'None',

        }
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)


# def test_view(request):
#     data = {
#         'name':'John Wick',
#         'age':23,
#         'profession':'Serial Killer'

#     }
#     return JsonResponse(data)
