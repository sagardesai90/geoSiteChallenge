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

get_processor_name()
get_date()