#!/usr/bin/env python

# Class for routers

class Router:

    def __init__(self, rtname='Router'):
        self.rtname = rtname

    def get_rtname(self):
        return self.rtname


class RouterInterface:

    def __init__(self, intfname):
        self.intfname = intfname


rt1 = Router()
rt2 = Router('Router-2')