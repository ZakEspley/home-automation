class Device(object):
    def __init__(self, deviceID, name, state=None, localip=None, mac=None, fw_name=None,
        fw_version=None, nodes=[], implementation=None, implementation_no=None,
        stats=None, base_topic="homie"):

        self.deviceID = deviceID
        self.name = name
        self.state = state
        self.localip = localip
        self.mac = mac
        self.fw_name = fw_name
        self.fw_version = fw_version
        self. nodes = nodes
        self.implementation = implementation
        self.implementation_no = implementation_no
        if stats is None:
            self.stats = Stats(self)
        else:
            self.stats = stats
        self.base_topic = base_topic
    
        self.device_topic = self.base_topic + "/" + str(deviceID)


class Stats(object):
    def __init__(self, parent, interval=60, uptime=0, signal=None, cputemp=None, cpuload=None, battery=None, 
        freeheap=None, supply=None):

        self.parent = parent
        self.interval = interval
        self.uptime = uptime
        self.signal = signal
        self.cputemp = cputemp
        self.cpuload = cpuload
        self.battery = battery
        self.freeheap = freeheap
        self.supply = supply

class Node(object):
    def __init__(self, parent, nodeID, name, node_type=None, properties=[], array=None):

        self.parent = parent
        self.nodeID = nodeID
        self.name = name
        self.type = node_type
        self.properties= properties
        self.array = array
    
    def __iter__(self):
        return self.properties
    
class Property(object):
    def __init__(self, parent, propertyID, name, settable=True, retained=True, unit=None, 
        datatype=None, property_format=None):

        self.parent = parent
        self.propertyID = propertyID
        self.name = name
        self.settable = settable
        self.retained = retained
        self.unit = unit
        self.datatype = datatype
        self.format = property_format

class Implementation(object):
    def __init__(self, parent, name=None, version=None, ota=None):
        self.parent =  parent
        self.name = name
        self.version = version
        self.ota = ota


class Firmware(object):
    def __init__(self, parent, name, version=None, checksum=None):
        self.parent = parent
        self.name = name
        self.version = version
        self.checksum = checksum

from paho.mqtt.client import Client

class Manager(Client):
    def __init__(self,ip_address, port=1883, keepalive=60, base_topic="homie", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ip_address = ip_address
        self.connect(ip_address, port, keepalive)
        self.subscribe("#")

    def on_message(self, userdata, msg):
        

    

