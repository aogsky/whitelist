import re
import os
import sys

def get_ip():
    print("Enter target file name:")
    ___filename = input()

    if os.path.exists(___filename):
        __f = open(___filename, encoding='utf-8 ')
        __str = __f.read()
        __f.close()
    else:
        print("Its not found!!!")
        sys.exit(1)

    ip_list = list()
    __reg01 = "((((([0-1]?[0-9]{0,2})|(2[0-4][0-9])|(25[0-4]))\.){3})(([0-1]?[0-9]{0,2})|(2[0-4][0-9])|(25[0-4])))"

    __result = re.sub('\s', '', __str)

    allip = re.findall(__reg01, __result)

    for x in range(0, len(allip), 6):
        ip_list.append(allip[x][0])

    return ip_list

def spilt_ip(ip):
    __reg02 = "\w+"
    element = re.findall(__reg02, ip)

def spilt_ip_list(ip_list):
    elements = list()
    for x in range(len(ip_list)):
        element = re.findall("\w+", ip_list[x])
        elements.append(element)
        elements[x].append(ip_list[x])
    return elements

def main():
    print(get_ip())

if __name__ == '__main__':
    main()