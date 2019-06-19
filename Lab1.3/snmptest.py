from pysnmp.hlapi import * # Импортировать только High-level API

ipaddr = '10.31.70.107'
port = 161
community = 'public'
MIB_value = '1.3.6.1.2.1.2.2.1.2'

snmp_object_sysDescr = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной
snmp_object_interfaces = ObjectIdentity(MIB_value) # По значению MIB-переменной

res_sysDescr = getCmd(SnmpEngine(),
                CommunityData(community, mpModel=0),
                UdpTransportTarget((ipaddr, port)),
                ContextData(),
                ObjectType(snmp_object_sysDescr))

res_interfaces = nextCmd(SnmpEngine(),
                CommunityData(community, mpModel=0),
                UdpTransportTarget((ipaddr, port)),
                ContextData(),
                ObjectType(snmp_object_interfaces),
                lexicographicMode=False)

print('>> Below is a switch\'s system description:')
for i in res_sysDescr:
    print ((str(i[3][0])).split(' = ')[1])

print ('\r\n\r\n>> Below is a list of switch\'s interfaces:')
for i in res_interfaces:
    print ((str(i[3][0])).split(' = ')[1])
