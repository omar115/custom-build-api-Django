from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'name':'John Wick',
        'age':23,
        'profession':'Serial Killer'

        }
        return Response(data)


# def test_view(request):
#     data = {
#         'name':'John Wick',
#         'age':23,
#         'profession':'Serial Killer'

#     }
#     return JsonResponse(data)
