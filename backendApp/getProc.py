import os, platform, subprocess, re

def get_processor_name():
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        infoArrStr = all_info.decode("utf-8")
        print(infoArrStr, "infoArrStr")
        return infoArrStr
    return ""