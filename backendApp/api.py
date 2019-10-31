from rest_framework import serializers, viewsets
from .models import PersonalRequests
import os, platform, subprocess, re

def get_processor_name():
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        cpu_info = subprocess.check_output(command, shell=True).strip().decode("utf-8")
        print(cpu_info, "all_info")
        return cpu_info
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command = "sysctl -n machdep.cpu.brand_string"
        cpu_info = subprocess.check_output(command, shell=True).strip().decode("utf-8")

        print(cpu_info, "cpu_info")
        
        return cpu_info
    return "Command not avaiilable on your OS"

def get_date():
    if platform.system() == "Linux":
        command = "date"
        date = subprocess.check_output(command, shell=True).strip().decode("utf-8")
        return date
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="date"
        date = subprocess.check_output(command, shell=True).strip().decode("utf-8")
        print(date, "date")
        return date
    return "Command not avaiilable on your OS"

class PersonalRequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalRequests
        fields = ('created_at', 'last_modified', 'comment')
    
    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        date = get_date()
        cpuinfo = get_processor_name()
        print(cpuinfo, "cpu info", date, "date")
        user = self.context['request'].user
        requestMade = PersonalRequests.objects.create(user=user, **validated_data)
        return requestMade 

class PersonalRequestsViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalRequestsSerializer
    queryset = PersonalRequests.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalRequests.objects.none()
        else:
            return PersonalRequests.objects.filter(user=user)
