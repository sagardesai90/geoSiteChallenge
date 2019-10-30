import os, platform, subprocess, re

def get_processor_name():
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip()
        info_arr_str = all_info.decode("utf-8")
        print(info_arr_str, "info_arr_str")
        return info_arr_str
    return ""

def get_date():
    if platform.system() == "Linux":
        command = "date"
        date_res = subprocess.check_output(command, shell=True).strip()
        date_res_str = date_res("utf-8")
        return date_res_str
    return "Command not avaiilable on your OS"