#Develop a program that demonstrates the use of cloudmesh.common.Shell.

from cloudmesh.common import Shell

if __name__ == "__main__":
    result = Shell.execute("dir")

    print(result)