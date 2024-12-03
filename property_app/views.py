# creating views for the property_app
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Property, Unit, Tenant, Lease
from property_app.serializers import PropertySerializer, UnitSerializer,LeaseSerializer,TenantSerializer


def home(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def property_list(request,pk=None):
    if request.method == 'GET':
       if pk is None:
           property_list = Property.objects.all()
           serializer = PropertySerializer(property_list, many=True)
           return Response(serializer.data)
       else:
           try:
               property = Property.objects.get(pk=pk)
               serializer = PropertySerializer(property)
               return Response(serializer.data)
           except Property.DoesNotExist:
               return Response(status=status.HTTP_404_NOT_FOUND)
           else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if pk is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        property.delete()
        return Response(status =status.HTTP_200_OK)






@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def unit_list(request):
    if request.method == 'GET':
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        units = Unit.objects.all()
        units.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tenant_list(request):
    if request.method == 'GET':
        tenant = Tenant.objects.all()
        serializer = TenantSerializer(tenant, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tenant = Tenant.objects.all()
        tenant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def lease_list(request):
    if request.method == 'GET':
        lease = Lease.objects.all()
        serializer = LeaseSerializer(lease, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LeaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lease = Lease.objects.all()
        lease.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Propertyview(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
class Unitview(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
class Tenantview(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]
class Leaseview(generics.ListAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated]

