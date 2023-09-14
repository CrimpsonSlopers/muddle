from rest_framework import serializers

from .models import StreamSession, Video, Viewer

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    viewer = ViewerSerializer()

    class Meta:
        model = Video
        fields = '__all__'
        

class StreamSessionSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = StreamSession
        fields = '__all__'


class CREATEVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


