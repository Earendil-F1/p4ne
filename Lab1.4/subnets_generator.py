from ipaddress import IPv4Network
import random

IPADDR_FIRST_OCTET_START = 11
IPADDR_FIRST_OCTET_END = 223
NETS_NUMBER = 100

def prefix_generator():
    oc = list()
    oc.append(random.randint(IPADDR_FIRST_OCTET_START, IPADDR_FIRST_OCTET_END))
    for i in range (1,3):
        oc.append(random.randint(0, 255))
    oc.append(0)
    pref =  '%s.%s.%s.%s' % (oc[0], oc[1], oc[2], oc[3])
    mask = random.randint(8, 24)
    return (IPv4Network ((pref, mask), strict=False)) # Automatically converts host bits to 0s

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        prefix = ''
        while True:
            tmppref = IPv4Network(prefix_generator())
            if (not tmppref.is_private):
                prefix = tmppref
                break
        IPv4Network.__init__(self, prefix)
    def key_value(self):
        # Should return one value to sort prefixes by mask (ascending) then by network address (ascending)
        return (self.prefixlen * (10**10)) + int(self.network_address) # int('255.255.255.255) = 4294967295

spoof_nets = list()
for i in range(0, NETS_NUMBER):
    spoof_nets.append(IPv4RandomNetwork())

spoof_nets = sorted(spoof_nets, key=IPv4RandomNetwork.key_value)
for i in range(0, NETS_NUMBER):
    print (spoof_nets[i])