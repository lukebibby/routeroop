#!/usr/bin/env python

# Class for routers

class Router:

    def __init__(self, rtname='Router'):
        self.rtname = rtname
        self.mgmtintf = self.create_intf('Management0')
        self.routingtbl = RouterRoutingTable()

    def get_rtname(self):
        return self.rtname

    def create_intf(self, intfname):
        return RouterInterface(intfname)

class RouterInterface:

    ipv4addr = ''
    ipv4netmask = ''

    def __init__(self, intfname, intfstatus='shutdown'):
        self.intfname = intfname
        self.intfstatus = intfstatus

    def add_ipv4_addr(self, ipv4addr, ipv4netmask):
        self.ipv4addr = ipv4addr
        self.netmask = ipv4netmask

class RouterRoutingTable:

    routing_tbl = {}

    def __init__(self):
        pass

    def add_route(self, network, netmask, nexthop):
        self.routing_tbl[network] = (network, netmask, nexthop)

    def del_route(self):
        pass

    def get_route(self, network):
        return self.routing_tbl[network]


rt1 = Router()
rt2 = Router('Router-2')

print dir(rt1)
print dir(rt2)

rt2.mgmtintf.add_ipv4_addr('192.168.1.10','255.255.255.0')
rt2.routingtbl.add_route('0.0.0.0', '0.0.0.0', '192.168.1.1')
print(rt2.routingtbl.get_route('0.0.0.0'))
print rt2.mgmtintf.ipv4addr
print rt2.mgmtintf.intfstatus

print dir(rt1)
print dir(rt2)