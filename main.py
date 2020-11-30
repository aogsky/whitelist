from db import InsertData
from filterIP import getIP

IpList = getIP()
InsertData(IpList)
