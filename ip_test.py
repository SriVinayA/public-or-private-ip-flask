from IPy import IP
import ipaddress


try:
    k = ipaddress.ip_address('127.0.0.1')
    print(k)
except:
  print("INVALID IP")


def get_ip_details(ip_input):

    ip = IP(ip_input)
    ip_details = ip.iptype()
    #print(ip_details)
    return ip_details

ip_d = get_ip_details("129.215.0.72")
print(ip_d)




