import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_CONNECTION_STRING)
db = client[settings.MONGO_DATABASE_NAME]
users_collection = db.users

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = users_collection.find_one({'email': email, 'password': password})
        if user:
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Username or password wrong'}, status=401)
    return JsonResponse({'message': 'Invalid request'}, status=400)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        
        if users_collection.find_one({'email': email}):
            return JsonResponse({'message': 'User already exists'}, status=400)
        users_collection.insert_one({'name': name, 'email': email, 'phone': phone, 'password': password})
        return JsonResponse({'message': 'Signup successful'}, status=201)
    return JsonResponse({'message': 'Invalid request'}, status=400)

@csrf_exempt
def data(request):
    if request.method == 'GET':
        return JsonResponse({
                'name': 'jinka',
                'status': 'sucesss'
                })
   
