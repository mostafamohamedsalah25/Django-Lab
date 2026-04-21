from rest_framework import serializers
from trainee.models import Trainee


class TraineeSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = Trainee
        fields = '__all__'

