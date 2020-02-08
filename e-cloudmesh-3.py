# cloudmesh-2.py Divyanshu Mishra SP20-516-224.
# Develop a program that demonstrates the use of FlatDict.
from cloudmesh.common import FlatDict, dotdict

student = {'name': {
                    'first': 'Divy',
                    'last': 'Mish'},
            'cls': {
                    'id':516,
                    'name':'cloud'},
            'hcid' : '516'}

flat = FlatDict(student, sep=".")
dot = dotdict(flat)

print(flat)
print(flat['name.first'])
print(flat['cls.id'])
#print(dot.cls.id)