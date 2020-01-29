# Multipass Installation on Windows Machine

### Prerequisite

Windows 10 Pro or EDU v1903 or above

### Installation Instruction

* Go to <https://multipass.run> and download windows installer.
* Run installer with default settings.
* Ensure that Virtualization support is enabled in BIOS. If not, enable it.
* Open PowerShell in admin mode by pressing windows+X and selecting 
  Window PowerShell(Admin) Option.
* Enable Hyper-v Hypervisor by using following command in PowerShell.     
        
        Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor
* Restart machine.
* After reboot, run command to check multipass installation. 

        multipass launch --name ubuntu-lts
* Successful installation must launch image.