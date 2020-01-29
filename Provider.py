import os
import subprocess

from cloudmesh.common.util import banner


class Provider:

    def __init__(self, name):
        self.name = name

    def launch(self):
        banner("launch")
        os.system(f"multipass launch --name {self.name}")
        # command = f"multipass launch --name {self.name}"
        # p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # text = p.stdout.read()
        # err = p.stderr.read()
        # print(f"message {text} and error - {err}")
        # print()

    def start(self):
        banner("start")
        os.system("multipass start {self.name}")

    def list(self):
        banner("list")
        os.system("multipass list")

    def find(self):
        banner("find")
        os.system("multipass find")

    def shell(self):
        print("shell")
        os.system(f"multipass shell {self.name}")

    def run(self, command):
        # please add self.name so the command gets started on the named vm
        banner(f"run {self.name} {command}")
        # improve next line
        os.system(f"multipass exec {self.name} -- {command}")


if __name__ == "__main__":
    p = Provider("cloudmesh")
    #p.launch()
    #p.shell()
    #p.find()
    p.run("uname -r")
    p.list()