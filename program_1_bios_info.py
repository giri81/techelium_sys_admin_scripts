'''
Created on Jul 7, 2017

@author: girish
for more information refer
https://msdn.microsoft.com/en-us/library/windows/desktop/aa394102(v=vs.85).aspx
https://msdn.microsoft.com/en-us/library/windows/desktop/aa394239(v=vs.85).aspx
'''

import wmi

c = wmi.WMI()    
systeminfo = c.Win32_ComputerSystem()[0]
osinfo = c.Win32_OperatingSystem()[0]

Manufacturer = systeminfo.Manufacturer
Model = systeminfo.Model
operating_system = osinfo.Caption
print("Manufactures ", Manufacturer )
print ("Model ", Model)
print ("OS ", operating_system)