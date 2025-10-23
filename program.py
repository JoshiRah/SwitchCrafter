import modules
import tkinter as tk
from tkinter import messagebox, Label, Frame
from tkinter import ttk
import os


def SaveUserInput():
    instance = modules.Switch(givenModel.get(),givenVersion.get(),givenHostname.get(),givenUsername.get(),givenPassword.get(),givenVidData.get(),givenVidVoice.get(),givenVidMgmt.get(),givenVidIot.get(),givenVidGuests.get(),givenNameData.get(),givenNameVoice.get(),givenNameMgmt.get(),givenNameIot.get(),givenNameGuests.get(),givenIfVid.get(),givenIfIp.get(),givenNetMask.get(),givenGateway.get(),givenDNS.get(),givenDomain.get(),givenCommunity.get(),givenContact.get(),givenLocation.get(),givenSyslog.get(),givenNtp.get())

    def WriteConfiguration():
        if instance.CheckDataIntegrity() == True:
            with open('Export.txt', 'w', encoding='UTF-8') as output:
                output.write(instance.BuildHostname())
                output.write(instance.BuildLocalAdmin())
                output.write(instance.CreateVLAN())
                output.write(instance.CreateInterface())
                output.write(instance.CreateDNS())
                output.write(instance.CreateSyslog())
                output.write(instance.CreateSNMP())
                output.write(instance.CreateNTP())
                output.write(instance.CreateUplinks())
                output.write(instance.CreateAccess())
                output.close()
        else:
            errorWindow = tk.Tk()
            errorWindow.title('Missing data detected! | Switch configuration generator')
            errorWindow.geometry('500x300')
            tk.Label(errorWindow, text='Missing data detected. Please preview your data once again!').grid(row=1,column=1)
            errorWindow.mainloop()

    # new window with name popUp
    popUp = tk.Tk()
    popUp.title('Preview Configuration | Switch configuration generator')
    popUp.geometry('1000x800')

    # fill out the window with preview content
    tk.Label(popUp, text=f'Preview your current configuration set:').grid(row=0,column=0)
    tk.Label(popUp, text=f'').grid(row=1,column=0)
    tk.Label(popUp, text=f'Model:').grid(row=2,column=0)
    tk.Label(popUp, text=instance.model).grid(row=2,column=1)
    tk.Label(popUp, text=f'Version:').grid(row=3,column=0)
    tk.Label(popUp, text=instance.ports).grid(row=3,column=1)
    tk.Label(popUp, text=f'').grid(row=4,column=0)
    tk.Label(popUp, text=f'Hostname:').grid(row=5,column=0)
    tk.Label(popUp, text=instance.hostname).grid(row=5,column=1)
    tk.Label(popUp, text=f'').grid(row=6,column=0)
    tk.Label(popUp, text=f'Username:').grid(row=7,column=0)
    tk.Label(popUp, text=instance.uname).grid(row=7,column=1)
    tk.Label(popUp, text=f'Password:').grid(row=7,column=3)
    tk.Label(popUp, text=instance.passwd).grid(row=7,column=5)
    tk.Label(popUp, text=f'').grid(row=8,column=0)
    tk.Label(popUp, text=f'').grid(row=9,column=0)
    tk.Label(popUp, text=f'DATA-VLAN:').grid(row=10,column=0)
    tk.Label(popUp, text=instance.vidDT).grid(row=10,column=1)
    tk.Label(popUp, text=f'DATA-Name:').grid(row=10,column=3)
    tk.Label(popUp, text=instance.nameDT).grid(row=10,column=5)
    tk.Label(popUp, text=f'VOICE-VLAN:').grid(row=11,column=0)
    tk.Label(popUp, text=instance.vidVC).grid(row=11,column=1)
    tk.Label(popUp, text=f'VOICE-Name:').grid(row=11,column=3)
    tk.Label(popUp, text=instance.nameVC).grid(row=11,column=5)
    tk.Label(popUp, text=f'MGMT-VLAN:').grid(row=12,column=0)
    tk.Label(popUp, text=instance.vidMG).grid(row=12,column=1)
    tk.Label(popUp, text=f'MGMT-Name:').grid(row=12,column=3)
    tk.Label(popUp, text=instance.nameMG).grid(row=12,column=5)
    tk.Label(popUp, text=f'IOT-VLAN:').grid(row=13,column=0)
    tk.Label(popUp, text=instance.vidIO).grid(row=13,column=1)
    tk.Label(popUp, text=f'IOT-Name:').grid(row=13,column=3)
    tk.Label(popUp, text=instance.nameIO).grid(row=13,column=5)
    tk.Label(popUp, text='').grid(row=14,column=0)
    tk.Label(popUp, text=f'Interface-VLAN:').grid(row=15,column=0)
    tk.Label(popUp, text=instance.vlan).grid(row=15,column=1)
    tk.Label(popUp, text='').grid(row=16,column=0)
    tk.Label(popUp, text=f'Interface-IP:').grid(row=17,column=0)
    tk.Label(popUp, text=instance.ip).grid(row=17,column=1)
    tk.Label(popUp, text=f'Subnetmask:').grid(row=17,column=3)
    tk.Label(popUp, text=instance.mask).grid(row=17,column=5)
    tk.Label(popUp, text=f'Default Gateway:').grid(row=17,column=7)
    tk.Label(popUp, text=instance.gw).grid(row=17,column=9)
    tk.Label(popUp, text='').grid(row=18,column=0)
    tk.Label(popUp, text=f'DNS-Server:').grid(row=19,column=0)
    tk.Label(popUp, text=instance.dns).grid(row=19,column=1)
    tk.Label(popUp, text=f'Domain name:').grid(row=19,column=3)
    tk.Label(popUp, text=instance.domain).grid(row=19,column=5)
    tk.Label(popUp, text='').grid(row=20,column=0)
    tk.Label(popUp, text=f'SNMP-Community:').grid(row=21,column=0)
    tk.Label(popUp, text=instance.comm).grid(row=21,column=1)
    tk.Label(popUp, text=f'SNMP-Contact:').grid(row=21,column=3)
    tk.Label(popUp, text=instance.cont).grid(row=21,column=5)
    tk.Label(popUp, text=f'SNMP-Location:').grid(row=21,column=7)
    tk.Label(popUp, text=instance.loc).grid(row=21,column=9)
    tk.Label(popUp, text='').grid(row=22,column=0)
    tk.Label(popUp, text=f'Remote-Logging:').grid(row=23,column=0)
    tk.Label(popUp, text=instance.rs).grid(row=23,column=1)
    tk.Label(popUp, text=f'NTP-Server:').grid(row=23,column=3)
    tk.Label(popUp, text=instance.ntp).grid(row=23,column=5)
    tk.Label(popUp, text='').grid(row=24,column=0)
    tk.Label(popUp, text='').grid(row=25,column=0)

    button1 = tk.Button(popUp, text="Write configuration to file", command=WriteConfiguration)
    button1.grid(row=26, column=10)

    popUp.mainloop()

# main window
root = tk.Tk()
root.title('Switch configuration generator | JoshiRah (c) 2025')
root.geometry('1200x800')

# placeholder
tk.Label(root, text='').grid(row=3,column=0)
tk.Label(root, text='').grid(row=5,column=0)
tk.Label(root, text='').grid(row=7,column=0)
tk.Label(root, text='').grid(row=13,column=0)
tk.Label(root, text='').grid(row=15, column=0)
tk.Label(root, text='').grid(row=17, column=0)
tk.Label(root, text='').grid(row=19, column=0)
tk.Label(root, text='').grid(row=21, column=0)
tk.Label(root, text='').grid(row=23, column=0)
tk.Label(root, text='').grid(row=24, column=0)

# model
tk.Label(root, text='Model:').grid(row=1, column=0)
givenModel = ttk.Combobox(root, values=modules.models)
givenModel.set('Select a model')
givenModel.grid(row=1, column=1)

# count of ports
tk.Label(root, text='Version:').grid(row=2,column=0)
givenVersion = ttk.Combobox(root, values=modules.version)
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
button = tk.Button(root, text="Save values", command=SaveUserInput)
button.grid(row=25, column=8)

# start main loop
root.mainloop()