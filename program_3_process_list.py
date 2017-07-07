'''
Created on Jul 7, 2017

@author: girish

MORE INFO:
http://timgolden.me.uk/python/wmi/cookbook.html
'''

import wmi
c = wmi.WMI ()

for process in c.Win32_Process ():
    print(process.ProcessId, process.Name)
