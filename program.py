import modules
import tkinter as tk
from tkinter import messagebox, Label, Frame
from tkinter import ttk

import os

models = ['HP Enterprise Aruba 6000', 'Dell EMC N1500']
version = ['12 Port', '24 Port', '48 Port']
ifVids = ['1', '300', '400']

newSwitch = modules.Switch('dell', 48, 'SW01', 'admin','geheim',100,200,300,400,900,'NET-DATA','NET-VOICE','NET-MGMT','NET-IOT','NET-GUESTS','300','1.1.1.1','255.255.255.0', '1.1.1.2', '1.2.3.4', 'rg-diakonie.de', 'public', 'noc@rg-diakonie.de', 'hier', 'syslog.rg-diakonie.de', 'ntp.rg-diakonie.de')

# main window
root = tk.Tk()
root.title('Switch configuration generator | J. Rahmlow (c) 2025')
root.geometry('800x600')

# placeholder
tk.Label(root, text='').grid(row=3,column=0)
tk.Label(root, text='').grid(row=5,column=0)
tk.Label(root, text='').grid(row=7,column=0)
tk.Label(root, text='').grid(row=13,column=0)
tk.Label(root, text='').grid(row=15, column=0)
tk.Label(root, text='').grid(row=17, column=0)
tk.Label(root, text='').grid(row=19, column=0)
tk.Label(root, text='').grid(row=21, column=0)

# model
tk.Label(root, text='Model:').grid(row=1, column=0)
givenModel = ttk.Combobox(root, values=models)
givenModel.set('Select a model')
givenModel.grid(row=1, column=1)

# count of ports
tk.Label(root, text='Version:').grid(row=2,column=0)
givenVersion = ttk.Combobox(root, values=version)
givenVersion.set('Select a version')
givenVersion.grid(row=2, column=1)

# hostname
tk.Label(root, text='Hostname:').grid(row=4, column=0)
givenHostname = tk.Entry(root)
givenHostname.grid(row=4, column=1)

# username
tk.Label(root, text='Username: ').grid(row=6,column=0)
givenUsername = tk.Entry(root)
givenUsername.grid(row=6, column=1)

# password
tk.Label(root, text='Password: ').grid(row=6, column=3)
givenPassword = tk.Entry(root)
givenPassword.grid(row=6, column=4)

# data vlan
tk.Label(root, text='DATA-Vid:').grid(row=8,column=0)
givenVidData = tk.Entry(root)
givenVidData.grid(row=8, column=1)

tk.Label(root, text='DATA-Name:').grid(row=8,column=3)
givenNameData = tk.Entry(root)
givenNameData.grid(row=8, column=4)

# voice vlan
tk.Label(root, text='VOICE-Vid:').grid(row=9,column=0)
givenVidVoice = tk.Entry(root)
givenVidVoice.grid(row=9, column=1)

tk.Label(root, text='VOICE-Name:').grid(row=9,column=3)
givenNameVoice = tk.Entry(root)
givenNameVoice.grid(row=9, column=4)

# mgmt vlan
tk.Label(root, text='MGMT-Vid:').grid(row=10,column=0)
givenVidMgmt = tk.Entry(root)
givenVidMgmt.grid(row=10, column=1)

tk.Label(root, text='MGMT-Name:').grid(row=10,column=3)
givenNameMgmt = tk.Entry(root)
givenNameMgmt.grid(row=10, column=4)

# iot vlan
tk.Label(root, text='IOT-Vid:').grid(row=11,column=0)
givenVidIot = tk.Entry(root)
givenVidIot.grid(row=11, column=1)

tk.Label(root, text='IOT-Name:').grid(row=11,column=3)
givenNameIot = tk.Entry(root)
givenNameIot.grid(row=11, column=4)

# guests vlan
tk.Label(root, text='GUESTS-Vid:').grid(row=12,column=0)
givenVidGuests = tk.Entry(root)
givenVidGuests.grid(row=12, column=1)

tk.Label(root, text='GUESTS-Name:').grid(row=12,column=3)
givenNameGuests = tk.Entry(root)
givenNameGuests.grid(row=12, column=4)

# management interface settings
tk.Label(root, text='Interface-Vid:').grid(row=14,column=0)
givenIfVid = tk.Entry(root)
givenIfVid.grid(row=14, column=1)

tk.Label(root, text='Interface-IP:').grid(row=16,column=0)
givenIfIp = tk.Entry(root)
givenIfIp.grid(row=16, column=1)

tk.Label(root, text='Netmask:').grid(row=16, column=3)
givenNetMask = tk.Entry(root)
givenNetMask.grid(row=16, column=4)

tk.Label(root, text='Default Gateway:').grid(row=16, column=6)
givenGateway = tk.Entry(root)
givenGateway.grid(row=16, column=7)

tk.Label(root, text='DNS-Server:').grid(row=18, column=0)
givenDNS = tk.Entry(root)
givenDNS.grid(row=18, column=1)

tk.Label(root, text='Domain name:').grid(row=18, column=3)
givenDomain = tk.Entry(root)
givenDomain.grid(row=18, column=4)

tk.Label(root, text='SNMP-Community:').grid(row=20, column=0)
givenCommunity = tk.Entry(root)
givenCommunity.grid(row=20,column=1)

tk.Label(root, text='SNMP-Contact:').grid(row=20, column=3)
givenContact = tk.Entry(root)
givenContact.grid(row=20,column=4)

tk.Label(root, text='SNMP-Location:').grid(row=20,column=6)
givenLocation = tk.Entry(root)
givenLocation.grid(row=20,column=7)

tk.Label(root, text='Remote-Logging:').grid(row=22, column=0)
givenSyslog = tk.Entry(root)
givenSyslog.grid(row=22,column=1)

tk.Label(root, text='NTP-Server:').grid(row=22, column=3)
givenNtp = tk.Entry(root)
givenNtp.grid(row=22, column=4)

# place button
#button = tk.Button(root, text="Save values", command=None)
#button.grid(row=5, column=1)

# start main loop
root.mainloop()