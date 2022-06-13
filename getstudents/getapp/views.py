from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.
import json
import requests
import io
from rest_framework.parsers import JSONParser
def index(request):
	if request.method == "GET":		
		r = requests.get("http://127.0.0.1:7000/api/students")
	
		python_data = json.loads(r.text)
		dict_list = python_data
		mydic ={'list':dict_list}

		return render(request , 'index.html' , mydic )












def add_student(request):
	if request.method == 'POST':		
		URL = "http://127.0.0.1:7000/api/students"
		name = request.POST.get('name')
		
		age = request.POST.get('age')
		
		marks = request.POST.get('marks')
		
		data = {
			'name': name,
			'age': age,
			'marks': marks
		}
		json_data = json.dumps(data)
		
		res = requests.post(url=URL,data = json_data)
		data = res.json()
	
		messages.success(request,"Student Added")
	return redirect('index')










def edit_student(request):
	if request.method == "POST":			
		URL = f"http://127.0.0.1:7000/api/students"
		id = request.POST.get('id')
		name = request.POST.get('name')
		age = request.POST.get('age')
		marks = request.POST.get('marks')
		data = {
			'id' : id,
			'name' : name,
			'age': age,
			'marks': marks
		}
		json_data = json.dumps(data)
		res = requests.put(url = URL , data = json_data)
		data = res.json()
		messages.success(request,"Save Changes")
	return redirect('index')














def delete_student(request):	
	if request.method =="POST":	
		URL = f"http://127.0.0.1:7000/api/students"
		id = request.POST.get('id')
		data = {
			'id' : id,
		}
		json_data = json.dumps(data)
		res = requests.delete(url = URL , data = json_data)
		data = res.json()
		messages.success(request,"Data Is Deleted")
		return redirect("index")
	

