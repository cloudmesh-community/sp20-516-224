import os
import platform as p

class Hypervisor:

     win_edu = "Windows 10 Education"
     win_pro = "Windows 10 Pro"

  # def hyperv(status : bool):
     # """
     # Switches on and off Hyper-V

     # :param status: if true switches on the hypervisor
     # """
     # if not windows:
        # return
     version = os.system("wmic os get caption")
     print (version[0])
     
     if win_edu in version:
        Console.error("Your version is not supported. You run {version}")
     else:
        print("good")
     # returns 
        # Caption
        # Microsoft Windows 10 Education
    
 
     # if version of windows is wrong
        # Console.error("Your version is not supported. You run {version}")

     # if status:
        # swichth hyperv on
     # else
        # switch hyperv off

  # def is_hyperv() -> bool:
     # define a docstring
     # returns tru if hyperv is switched on else false

  # def hyperv_supported() -> bool:
     # define a docstring
     # returns true if hyperv is suported on your OS

  # def reboot():
     # reboots the machine

# Usage:

# Hypervisor.hyperv(True)
