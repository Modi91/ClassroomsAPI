from classes.models import Classroom

from rest_framework import serializers


class ClassroomListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher']

class ClassroomDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'



class ClassroomUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ['teacher']

		