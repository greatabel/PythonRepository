import ipaddress
net  = ipaddress.ip_network('192.168.0.21')
print('net:',net)
for a in net:
    print(a)