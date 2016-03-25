from distutils.core import setup
import py2exe

setup(windows=['clock.pyw'])
# setup(windows=['gui.py'], options={"py2exe":{"includes":["sip"]}})