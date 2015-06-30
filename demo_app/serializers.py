from rest_framework import serializers

from demo_app.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id','title', 'description', 'completed')