from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)

from classes.models import Classroom
from .serializers import (
	ClassroomListSerializer,
 	ClassroomDetailSerializer,
 	ClassroomUpdateSerializer,
 	)
# Create your views here.

class ClassesListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer
		
class ClassesDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = "classroom_id"



class ClassesUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = "classroom_id"




class ClassesCreateView(CreateAPIView):
	serializer_class = ClassroomUpdateSerializer


	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)



class ClassesDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = "classroom_id"