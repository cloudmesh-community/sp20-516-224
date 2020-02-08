# cloudmesh-2.py Divyanshu Mishra SP20-516-224
# testing git push
# Develop a program that demonstrates the use of dotdict.

from cloudmesh.common.dotdict import dotdict

if __name__=="__main__":
    student = {'name':'Divy',
               'cls':'cloud',
               'hcid':224}

    student=dotdict(student)
    print(f"Student Name: {student.name}")
    print(f"Student Class: {student.cls}")
    print(f"Student hcid: {student.hcid}")