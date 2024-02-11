from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world ")

def json_response(request):
  return JsonResponse("<p>Hello world</p>")

def http_response(request):
  return HttpResponse("<p>Hello world</p>")

def say_hello(req):
  return HttpResponse("<p>Hello world</p>")

def user_profile(request):
  user_details = {
    'name': 'Usha',
    'email': 'ushahembashir.com',
  }
  return JsonResponse(user_details)

def filter_queries(request, pk):
   filter_details = {
    'id': 1,
    'title': 'ushahembashir.com',
    'description': 'ushahembashir.com',
    'status': 'ushahembashir.com',
    'submitted_by': 'ushahembashir.com',
  }
   return JsonResponse(filter_details)

class QueryView(View):
      data = [
         {'id': 1, 'title': 'And the man died'},
         {'id': 2, 'title': 'And the man died'}
      ]
      def ge(self, data):
        return JsonResponse(self.data)
