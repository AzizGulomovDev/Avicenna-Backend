from rest_framework import serializers
from .models import ClassRoom,Davomat
from students.serializer import StudentSerializer
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        depth =1
class DavomatNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
class DavomatSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    sinf = serializers.StringRelatedField()
    class Meta:
        model = Davomat
        fields= '__all__'


