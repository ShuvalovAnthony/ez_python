from ipaddress import *
k = 0
net = ip_network("176.114.52.96/255.255.255.248")

adresses = []

for ip in net:
    ip2 = bin(int(ip))[2:]
    adresses.append(ip2)


for ip2 in adresses[1:-1]:
    if ip2.count("1") % 2 != 0:
        k += 1
print(k)