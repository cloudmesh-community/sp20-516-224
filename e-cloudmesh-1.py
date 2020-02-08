# cloudmesh-1.py Divyanshu Mishra SP20-516-224
# Develop a program that demonstrates the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE


if __name__ == "__main__":

    HEADING('This is HEADING')
    HEADING('This is HEADING',c='%')

    banner('This is banner in RED color',color="RED")
    banner('Another flavor of banner',c="$",prefix="$",color="GREEN")

    #m={"key": "value"}
    dict = {'name': 'DM',
            'class': '516',
            'subject': 'cloud'}

    VERBOSE(dict.keys())
    VERBOSE(dict.values())

