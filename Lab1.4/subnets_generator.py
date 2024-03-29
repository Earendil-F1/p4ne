from ipaddress import IPv4Network
from random import randint

IPADDR_FIRST_OCTET_START = 11
IPADDR_FIRST_OCTET_END = 223
NETS_NUMBER = 100

def prefix_generator():
    addr = '%s.%s.%s.%s' % (randint(IPADDR_FIRST_OCTET_START, IPADDR_FIRST_OCTET_END),
                             randint(0, 255),
                             randint(0, 255),
                             0)
    mask = randint(8, 24)
    return (IPv4Network ((addr, mask), strict=False)) # Automatically converts host bits to 0s

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        prefix = ''
        while True:
            prefix = IPv4Network(prefix_generator())
            if (not prefix.is_private):
                break
        super().__init__(prefix)
    def key_value(self):
        # Should return one value to sort prefixes by mask (ascending), then by network address (ascending)
        return (self.prefixlen * (10**10)) + int(self.network_address) # int('255.255.255.255') = 4294967295

spoof_nets = list()
for i in range(0, NETS_NUMBER):
    cur_len = len(spoof_nets)
    while (cur_len == len(spoof_nets)):
        next_net = IPv4RandomNetwork()
        for j in range(0, cur_len):
            if (next_net.overlaps(spoof_nets[j])):
                break
        else:
            spoof_nets.append(next_net)


spoof_nets = sorted(spoof_nets, key=IPv4RandomNetwork.key_value)
for i in range(0, NETS_NUMBER):
    print (spoof_nets[i])