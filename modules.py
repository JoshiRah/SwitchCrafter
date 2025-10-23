# error messages

errorCode060 = '>>> wrong or missing parameter for this method'
errorCode999 = '>>> fatal error. Just burn your pc'

# sets

models = ['HPE Aruba 6000 Series', 'Dell EMC N1500 Series']
version = ['12 Port', '24 Port', '48 Port']

# the one and only class

class Switch():
    def __init__(self, model=None, ports=None, hostname=None, username=None, password=None, vidData=None, vidVoice=None, vidManagement=None, vidIot=None, vidGuests=None, nameData=None, nameVoice=None, nameManagement=None, nameIot=None, nameGuests=None, managementVlan=None, ipAddr=None, netMask=None, defGW=None, dnsServer=None, domainName=None, community=None, contact=None, location=None, remoteServer=None, ntpServer=None):
        self.model = model
        self.ports = ports
        self.hostname = hostname
        self.uname = username
        self.passwd = password
        self.vidDT = vidData
        self.vidVC = vidVoice
        self.vidMG = vidManagement
        self.vidIO = vidIot
        self.vidGU = vidGuests
        self.nameDT = nameData
        self.nameVC = nameVoice
        self.nameMG = nameManagement
        self.nameIO = nameIot
        self.nameGU = nameGuests
        self.vlan = managementVlan
        self.ip = ipAddr
        self.mask = netMask
        self.gw = defGW
        self.dns = dnsServer
        self.domain = domainName
        self.comm = community
        self.cont = contact
        self.loc = location
        self.rs = remoteServer
        self.ntp = ntpServer

    def CheckDataIntegrity(self):
        while True:
            try:
                return all(value not in (None, '', []) for value in self.__dict__.values())
                break
            except:
                print(errorCode999)

    def BuildHostname(self):
         validHostname = f'hostname {self.hostname}\n'
         return validHostname

    def BuildLocalAdmin(self):
        if self.model == models[0]:
            validUser = f'username {self.uname} password plaintext {self.passwd}\n'
            return validUser
        elif self.model == models[1]:
            validUser = f'user {self.uname} password {self.passwd} privilege 15\n'
            return validUser
        else:
            return errorCode060

    def CreateVLAN(self):
        validVLAN = f'vlan {self.vidDT}\nname {self.nameDT}\nvlan {self.vidVC}\nname {self.nameVC}\nvlan {self.vidMG}\nname {self.nameMG}\nvlan {self.vidIO}\nname {self.nameIO}\nvlan {self.vidGU}\nname {self.nameGU}\nexit\n'
        return validVLAN

    def CreateInterface(self):
        if self.model == models[0]:
            validInterface = f'interface vlan {self.vlan}\nip address {self.ip} {self.mask}\nexit\nip route 0.0.0.0/0 {self.gw}\n'
            return validInterface
        if self.model == models[1]:
            validInterface = f'interface vlan {self.vlan}\nip address {self.ip} {self.mask}\nexit\nip default-gateway {self.gw}\n'
            return validInterface
        else:
            return errorCode060

    def CreateDNS(self):
        if self.model == models[0]:
            validDNS = f'ip dns server-address {self.dns}\nip dns domain-name {self.domain}\n'
            return validDNS
        elif self.model == models[1]:
            validDNS = f'ip name-server {self.dns}\nip domain-name {self.domain}\n'
            return validDNS
        else:
            return errorCode060

    def CreateSyslog(self):
        if self.model == models[0]:
            validLogging = f'logging {self.rs} severity info\n'
            return validLogging
        elif self.model == models[1]:
            validLogging = f'logging {self.rs}\nlevel informational\nexit\n'
            return validLogging
        else:
            return errorCode060

    def CreateSNMP(self):
        if self.model == models[0]:
            validSNMP = f'snmp-server vrf default\nsnmp-server community {self.comm}\nsnmp-server system-contact {self.cont}\nsnmp-server system-location {self.loc}\n'
            return validSNMP
        elif self.model == models[1]:
            validSNMP = f'snmp-server community {self.comm}\nsnmp-server contact {self.cont}\nsnmp-server {self.loc}\n'
            return validSNMP
        else:
            return errorCode060

    def CreateNTP(self):
        if self.model == models[0]:
            validNTP = f'ntp server {self.ntp}\nclock timezone europe/berlin\n'
            return validNTP
        elif self.model == models[1]:
            validNTP = f'sntp server {self.ntp}\nclock timezone +2\n'
            return validNTP
        else:
            return 'modell fehlt'

    def CreateUplinks(self):
        if self.model == models[0] and self.ports == version[0]:
            validUplinks = f'interface 1/1/13-1/1/16\nvlan trunk allowed all\nvlan trunk native 1\ndescription Network\nspanning-tree port-type admin-network\nno shutdown\nexit\n' # Set interfaces 13 - 16 into vlan trunk mode with native trunk on vlan 1, set the description to Network and port-type into network
            return validUplinks
        elif self.model == models[0] and self.ports == version[1]:
            validUplinks = f'interface 1/1/23-1/1/28\nvlan trunk allowed all\nvlan trunk native 1\ndescription Network\nspanning-tree port-type admin-network\nno shutdown\nexit\n' # Set interfaces 23 - 28 into vlan trunk mode with native trunk on vlan 1, set the description to Network and port-type into network
            return validUplinks
        elif self.model == models[0] and self.ports == version[2]:
            validUplinks = f'interface 1/1/47-1/1/52\nvlan trunk allowed all\nvlan trunk native 1\ndescription Network\nspanning-tree port-type admin-network\nno shutdown\nexit\n' # Set interfaces 47 - 52 into vlan trunk mode with native trunk on vlan 1, set the description to Network and port-type into network
            return validUplinks
        elif self.model == models[1] and self.ports == version[1]:
            validUplinks = (f'interface range gi1/0/23-24\nswitchport trunk allowed vlan all\nswitchport trunk native vlan 1\nswitchport mode trunk\ndescription Network\nno shutdown\nexit\n' # Set interfaces gi23 - gi24 into vlan trunk mode with native trunk on vlan 1, set the description to Network and spanning-tree into network
                            f'interface range te1/0/1-4\nswitchport trunk allowed vlan all\nswitchport trunk native vlan 1\nswitchport mode trunk\ndescription Network\nno shutdown\nexit\n') # Set interfaces te1 - te4 into vlan trunk mode with native trunk on vlan 1, set the description to Network and spanning tree into network
            return validUplinks
        elif self.model == models[1] and self.ports == version[2]:
            validUplinks = (f'interface range gi1/0/47-48\nswitchport trunk allowed vlan all\nswitchport trunk native vlan 1\nswitchport mode trunk\ndescription Network\nno shutdown\nexit\n' # Set interfaces gi23 - gi24 into vlan trunk mode with native trunk on vlan 1, set the description to Network and spanning-tree into network
                            f'interface range te1/0/1-4\nswitchport trunk allowed vlan all\nswitchport trunk native vlan 1\nswitchport mode trunk\ndescription Network\nno shutdown\nexit\n') # Set interfaces te1 - te4 into vlan trunk mode with native trunk on vlan 1, set the description to Network and spanning tree into network
            return validUplinks
        else:
            return errorCode060

    def CreateAccess(self):
        if self.model == models[0] and self.ports == version[0]:
            validUplinks = f'interface 1/1/1-1/1/12\nvlan trunk allowed all\nvlan trunk native {self.vidDT}\ndescription Edge\nspanning-tree port-type admin-edge\nno shutdown\nexit\n' # Set interfaces 13 - 16 into vlan trunk mode with native trunk on vlan 100, set the description to Edge and port-type into edge
            return validUplinks
        elif self.model == models[0] and self.ports == version[1]:
            validUplinks = f'interface 1/1/1-1/1/22\nvlan trunk allowed all\nvlan trunk native {self.vidDT}\ndescription Edge\nspanning-tree port-type admin-edge\nno shutdown\nexit\n' # Set interfaces 23 - 28 into vlan trunk mode with native trunk on vlan 100, set the description to Edge and port-type into edge
            return validUplinks
        elif self.model == models[0] and self.ports == version[2]:
            validUplinks = f'interface 1/1/1-1/1/46\nvlan trunk allowed all\nvlan trunk native {self.vidDT}\ndescription Edge\nspanning-tree port-type admin-edge\nno shutdown\nexit\n' # Set interfaces 47 - 52 into vlan trunk mode with native trunk on vlan 100, set the description to Edge and port-type into edge
            return validUplinks
        elif self.model == models[1] and self.ports == version[1]:
            validUplinks = (f'interface range gi1/0/1-22\nswitchport general pvid {self.vidDT}\nswitchport allowed vlan add {self.vidDT} untagged\nswitchport general allowed vlan add 100-999 tagged\n'
                            f'switchport general allowed vlan remove 1\nswitchport mode general\ndescription Edge\nspanning-tree portfast bpdufilter default\nno shutdown\nexit\n') # Set interfaces gi1 - gi22 into vlan general mode with native trunk on vlan data, set the description to Network and spanning-tree into edge
            return validUplinks
        elif self.model == models[1] and self.ports == version[2]:
            validUplinks = (f'interface range gi1/0/1-46\nswitchport general pvid {self.vidDT}\nswitchport allowed vlan add {self.vidDT} untagged\nswitchport general allowed vlan add 100-999 tagged\n'
                            f'switchport general allowed vlan remove 1\nswitchport mode general\ndescription Edge\nspanning-tree portfast bpdufilter default\nno shutdown\nexit\n') # Set interfaces gi1 - gi22 into vlan general mode with native trunk on vlan data, set the description to Network and spanning-tree into edge
            return validUplinks
        else:
            return errorCode060

