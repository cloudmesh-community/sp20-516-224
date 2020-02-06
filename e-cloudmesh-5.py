#Develop a program that demonstrates the use of cloudmesh.common.StopWatch.
from cloudmesh.common import banner
from cloudmesh.common.StopWatch import StopWatch
from time import sleep

c = 0
StopWatch.start("test")
for i in range(100000):
    True
StopWatch.stop("test")
result = StopWatch.get("test",6)

print(f"time to execute for loop million times: {result}")
#print(StopWatch.get("test",6))
#StopWatch.benchmark()