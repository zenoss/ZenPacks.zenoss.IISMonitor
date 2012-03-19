######################################################################
#
# Copyright 2009 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

import Globals
import os
from Products.CMFCore.DirectoryView import registerDirectory

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

import logging
log = logging.getLogger("zen.IISMonitor")

from Products.ZenModel.ZenPack import ZenPackBase
class ZenPack(ZenPackBase):
    """
    ZenPacks.zenoss.IISMonitor ZenPack loader.
    """

    # Windows services for which we want to enable for monitoring by default.
    defaultWinServices = ('IISADMIN',)

    def install(self, app):
        ZenPackBase.install(self, app)
        self.enableDefaultServiceMonitoring(app.zport.dmd)

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        self.enableDefaultServiceMonitoring(app.zport.dmd)

    def enableDefaultServiceMonitoring(self, dmd):
        findWinService = dmd.Services.WinService.find
        for sc in [ findWinService(s) for s in self.defaultWinServices ]:
            if sc is None: continue
            if sc.hasProperty('zMonitor'): continue
            log.info('Enabling monitoring for %s', sc.description)
            sc._setProperty('zMonitor', True)
            for i in sc.instances():
                i.index_object()

