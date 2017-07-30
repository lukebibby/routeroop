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

    def __init__(self, intfname):
        self.intfname = intfname


rt1 = Router()
rt2 = Router('Router-2')

print dir(rt1)
print dir(rt2)
print rt2.mgmtintf.intfname

