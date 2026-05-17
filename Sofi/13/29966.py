from ipaddress import *
k = 0
net = ip_network("146.180.173.153/255.192.0.0", strict=False)
for ip in net:
    ip2 = bin(int(ip))[2:]
    print(ip2)
    break
