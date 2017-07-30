#!/usr/bin/env python

# Class for routers

class Router:

    def __init__(self, rtname='Router'):
        self.rtname = rtname
        self.mgmtintf = self.create_intf('Management0')

    def get_rtname(self):
        return self.rtname

    def create_intf(self, intfname):
        return RouterInterface(intfname)

class RouterInterface:

    def __init__(self, intfname, intfstatus='shutdown'):
        self.intfname = intfname
        self.intfstatus = intfstatus
        self.ipv4addr = ''
        self.netmask = ''


    def add_ipv4_addr(self, ipv4addr, ipv4netmask):
        self.ipv4addr = ipv4addr
        self.netmask = ipv4netmask

class RouterRoutingTable:
    pass

    def add_route(self):
        pass

    def del_route(self):
        pass

    def get_route(self):
        pass


rt1 = Router()
rt2 = Router('Router-2')

print dir(rt1)
print dir(rt2)

rt2.mgmtintf.add_ipv4_addr('192.168.1.10','255.255.255.0')
print rt2.mgmtintf.ipv4addr
print rt2.mgmtintf.intfstatus


