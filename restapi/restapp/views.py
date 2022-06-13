from django.shortcuts import render
from yaml import serialize
# from rest_framework import viewsets
from . serializers import StudentSrializers
from . models import Students
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.



@csrf_exempt

@api_view(['GET', 'PUT' , 'POST' , 'DELETE'])
def Student_Create(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentSrializers(students , many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSrializers(data = pythondata)
        if serializer.is_valid():
            serializer.save()
        res = {'msg':'Data Created'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data , content_type ='application/json',status=status.HTTP_201_CREATED)
    # json_data = JSONRenderer().render(serializer.errors)
    # return HttpResponse(json_data , content_type ='application/json')

    if request.method =="PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Students.objects.get(id = id)
        serializer = StudentSrializers(stu ,data = pythondata ,partial = True)

        if serializer.is_valid():
            serializer.save()
        res = {'msg':'Data Updated'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data , content_type ='application/json',status = status.HTTP_200_OK)
        

    if request.method =="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Students.objects.get(id = id)
        stu.delete()

        # if serializer.is_valid():
        #     serializer.save()
        res = {'msg':'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data , content_type ='application/json',status = status.HTTP_200_OK)
        
















    

# @api_view(['GET','POST'])
# def Student_Data_View(request):
#     if request.method == 'GET':
#         students = Students.objects.all()
#         serializer = StudentSrializers(students , many=True)
       
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSrializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors)































@api_view(['GET' , 'PUT' ,'DELETE'])
def Student_Data_Update(request , pk):

    try:
        student = Students.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        courseSerializer = StudentSrializers(student) 
        return Response(courseSerializer.data)

    elif request.method == 'PUT':
        srializer = StudentSrializers(student , data = request.data)
        if srializer.is_valid():
            srializer.save()
            return Response(srializer.data)
        return Response(srializer.errors)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # if request.method =='GET':
    #     students = Students.objects.all()
    #     srializer= StudentSrializers(students , many = True)
    #     return JsonResponse(srializer.data ,safe=False)

    # return JsonResponse({'masg':'sdj'},safe=False)

