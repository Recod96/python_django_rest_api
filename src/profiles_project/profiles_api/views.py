from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializers_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'uses HTTP methodes as function (get,post,put,patch,delete)',
            'it is similar to a trafitional django view',
            'Gives you the control over your logic',
            'it wapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Creatte a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)
      
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request):
  
         return Response({'method':'put'})
    
    def patch(self,request):
  
         return Response({'method':'patch'})

    def delete(self,request):
  
         return Response({'method':'delete'})
       
    

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list,create,retrieve...)',
            'Automatically maps to URLs usinng Routers',
            'Provides more fucntionality with less code'
        ]

        return Response({'message':'Hello !','a_viewset':a_viewset})