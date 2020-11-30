import re
import os
import sys

def getIP():
    print("Enter target file name:")
    filename = input()

    if os.path.exists(filename):
        f = open(filename)
        str = f.read()
        f.close()
    else:
        print("Its not found!!!")
        sys.exit(1)

    IpList = list()
    reg01 = "((((([0-1]?[0-9]{0,2})|(2[0-4][0-9])|(25[0-4]))\.){3})(([0-1]?[0-9]{0,2})|(2[0-4][0-9])|(25[0-4])))"

    result = re.sub('\s', '', str)

    allip = re.findall(reg01, result)

    for x in range(0, len(allip), 6):
        IpList.append(allip[x][0])

    return IpList
