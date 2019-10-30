from rest_framework import serializers, viewsets
from .models import RequestsMade
import os, platform, subprocess, re

class RequestsMadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestsMade
        fields = ('created_at', 'last_modified', 'comment')
    
    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        requestMade = RequestsMade.objects.create(user=user, **validated_data)
        return requestMade 


def get_processor_name():
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        infoArrStr = all_info.decode("utf-8")
        print(infoArrStr, "infoArrStr")
        return infoArrStr
    return ""

class RequestsMadeViewSet(viewsets.ModelViewSet):
    serializer_class = RequestsMadeSerializer
    queryset = RequestsMade.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return RequestsMade.objects.none()
        else:
            return RequestsMade.objects.filter(user=user)
