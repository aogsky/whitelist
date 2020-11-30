import re


f = open("/root/text.txt")
#print(type(f))
#print(type(f.read()))
str = f.read()
print(f.tell())
f.close()

#x = re.search("span", str)
#y = re.findall("span", str)

result = re.sub("\s", "", str)

#print(result)
IpList = list()

allip = re.findall("((((([0-1]?[0-9]{0,2})|(2[0-4][0-9])|(25[0-4]))\.){3})(([0-1]?[0-9]{0,2})|(2[0-4][0-9])|(25[0-4])))", result)

print(allip[0])

for x in range(0, 300, 6):
    print(allip[x][0])
    IpList.append(allip[x][0])
print('Operate finished!')


f = open('iplist.txt', 'w')
for x in IpList:
    f.write(x+'\n')
f.close()
