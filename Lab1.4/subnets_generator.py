from ipaddress import IPv4Network
from random import randint

IPADDR_FIRST_OCTET_START = 11
IPADDR_FIRST_OCTET_END = 223
NETS_NUMBER = 100

def prefix_generator():
    pref =  '%s.%s.%s.%s' % (randint(IPADDR_FIRST_OCTET_START, IPADDR_FIRST_OCTET_END),
                             randint(0, 255),
                             randint(0, 255),
                             0)
    mask = randint(8, 24)
    return (IPv4Network ((pref, mask), strict=False)) # Automatically converts host bits to 0s

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        prefix = ''
        while True:
            tmppref = IPv4Network(prefix_generator())
            if (not tmppref.is_private):
                prefix = tmppref
                break
        super().__init__(prefix)
    def key_value(self):
        # Should return one value to sort prefixes by mask (ascending) then by network address (ascending)
        return (self.prefixlen * (10**10)) + int(self.network_address) # int('255.255.255.255) = 4294967295

spoof_nets = list()
for i in range(0, NETS_NUMBER):
    spoof_nets.append(IPv4RandomNetwork())

spoof_nets = sorted(spoof_nets, key=IPv4RandomNetwork.key_value)
for i in range(0, NETS_NUMBER):
    print (spoof_nets[i])