from ast import main
import random
from sqlite3 import Timestamp
import threading
import time
from netaddr import IPNetwork
import matplotlib.pyplot as plt
import networkx as nx

# UTILS


def make_packets(sender_device, receiver_device, message):
    message = {'Data': message, 'H3': [
        sender_device.ip, receiver_device.ip], 'H2': [sender_device.address]}
    return message


def make_frames(receiver_device_mac, message):
    message['H2'].append(receiver_device_mac.address)
    return message


def arp_request(device, message):
    ret = 0
    for i in device.connected_to:
        ret = i.respond_arp(message, device)
        if ret != 0:
            message['H2'].append(ret.address)
    print("\n")
    return message


def send_message(d1, message, ack_msg=False):
    print("\u001b[34m")
    print(message)
    print("\u001b[30m")
    print(d1)
    for i in d1.connected_to:
        i.respond_send(message, d1, ack_msg)


def swap_address(array):
    temp = array[0]
    array[0] = array[1]
    array[1] = temp
    return array


def generate_ack(message):
    message['Data'] = 'ACK'
    message['H3'] = swap_address(message['H3'])
    message['H2'] = swap_address(message['H2'])
    return message


def check_subnet(ip1, ip2):

    subnet = "255.255.0.0"
    if IPNetwork("{}/{}".format(ip1, subnet)) == IPNetwork("{}/{}".format(ip2, subnet)):
        return True
    return False
# UTILS


def generate_mac_address():
    """Grants A MAC Address To Each Of The Device"""
    mac = [str(random.randint(0xB, 0x63)) for x in range(3)]
    return ("11:11:11:"+":".join(mac))


def make_frames(receiver_device_mac, message):
    message['H2'].append(receiver_device_mac.address)
    return message


def arp_request(device, message):
    ret = 0
    for i in device.connected_to:
        ret = i.respond_arp(message, device)
        if ret != 0:
            message['H2'].append(ret.address)
    print("\n")
    return message


def send_message(d1, message, ack_msg=False):
    print("\u001b[34m")
    print(message)
    print("\u001b[30m")
    print(d1)
    for i in d1.connected_to:
        i.respond_send(message, d1, ack_msg)


def swap_address(array):
    temp = array[0]
    array[0] = array[1]
    array[1] = temp
    return array


def generate_ack(message):
    message['Data'] = 'ACK'
    message['H3'] = swap_address(message['H3'])
    message['H2'] = swap_address(message['H2'])
    return message


def check_subnet(ip1, ip2):

    subnet = "255.255.0.0"
    if IPNetwork("{}/{}".format(ip1, subnet)) == IPNetwork("{}/{}".format(ip2, subnet)):
        return True
    return False


def make_frames(receiver_device_mac, message):
    message['H2'].append(receiver_device_mac.address)
    return message


def arp_request(device, message):
    ret = 0
    for i in device.connected_to:
        ret = i.respond_arp(message, device)
        if ret != 0:
            message['H2'].append(ret.address)
    print("\n")
    return message


def send_message(d1, message, ack_msg=False):
    print("\u001b[34m")
    print(message)
    print("\u001b[30m")
    print(d1)
    for i in d1.connected_to:
        i.respond_send(message, d1, ack_msg)


def swap_address(array):
    temp = array[0]
    array[0] = array[1]
    array[1] = temp
    return array


def generate_ack(message):
    message['Data'] = 'ACK'
    message['H3'] = swap_address(message['H3'])
    message['H2'] = swap_address(message['H2'])
    return message


def check_subnet(ip1, ip2):
    subnet = "255.255.0.0"
    if IPNetwork("{}/{}".format(ip1, subnet)) == IPNetwork("{}/{}".format(ip2, subnet)):
        return True
    return False


def generate_ip_address():
    """Grants A IP Address To Each Of The Device"""
    return ("192.168."+str(random.randint(0, 255))+"."+str(random.randint(0, 255)))


class devices:
    def __init__(self, id, MACaddress, ip, port=80, active=True):
        self.id = id
        self.MACaddress = MACaddress
        self.ip = ip
        self.port = port
        self.active = active
        self.connected_to = []
        self.arp_table = {}

    def make_inactive(self):
        self.active = False

    def make_active(self):
        self.active = True

    def respond_arp(self, message, sender):
        if message['H3'][1] == self.ip:
            print("\u001b[32m Device {} : Sent its MAC Address as its the intended destinaition  \u001b[0m".format(
                self.id))
            self.arp_table[message['H3'][0]] = message['H2'][0]
            return self
        else:
            print("\u001b[31m Device {} : ARP Request Rejected  as its not the intended destination\u001b[0m".format(
                self.id))
            return 0

    def respond_send(self, message, sender, ack_msg=False):
        if message["H2"][1] == self.MACaddress:
            print("Devive with MAC : {} Recieved Data From Source : {} ".format(
                message["H2"][1], message['H2'][0]))
            if not ack_msg:
                print("Sending ACK!")
                send_message(generate_ack(message), True)
        else:
            print("Device {} Dropped The Packet".format(self.id))


class hubs(devices):
    def __init__(self, id, port=80, active=True):
        self.id = id
        self.active = active
        self.connected_to = []
        self.port = port

    def respond_arp(self, message, sender):
        ret = 0
        for i in self.connected_to:
            dev = 0
            if i == sender:
                continue
            dev = i.respond_arp(message, self)
            if dev != 0:
                ret = dev
        return ret

    def respond_send(self, message, sender, ack_msg=False):
        for i in self.connected_to:
            if i == sender:
                continue
            i.respond_send(message, self, ack_msg)


class Bridge(devices):
    def __init__(self, id, address, ports=[80, 8080], active=True):
        self.mac_table = {}
        self.mac_table[ports[0]] = []
        self.mac_table[ports[1]] = []
        self.ports = ports
        self.address = address
        self.id = id
        self.active = active
        self.connected_to = []

    def respond_arp(self, message, sender):
        ret = 0
        for i in self.connected_to:
            dev = 0
            dev = i.respond_arp(message, self)
            if dev != 0:
                ret = dev
                self.mac_table[ret.port].append(ret.address)
        return ret


def make_packets(sender_device, receiver_device, message):
    message = {'Data': message, 'H3': [
        sender_device.ip, receiver_device.ip], 'H2': [sender_device.MACaddress]}
    return message


def make_frames(receiver_device_mac, message):
    message['H2'].append(receiver_device_mac.address)
    return message


def arp_request(device, message):
    ret = 0
    for i in device.connected_to:
        ret = i.respond_arp(message, device)
        if ret != 0:
            message['H2'].append(ret.address)
    print("\n")
    return message


def send_message(d1, message, ack_msg=False):
    print("\u001b[34m")
    print(message)
    print("\u001b[30m")
    print(d1)
    for i in d1.connected_to:
        i.respond_send(message, d1, ack_msg)


def swap_address(array):
    temp = array[0]
    array[0] = array[1]
    array[1] = temp
    return array


def generate_ack(message):
    message['Data'] = 'ACK'
    message['H3'] = swap_address(message['H3'])
    message['H2'] = swap_address(message['H2'])
    return message


def check_subnet(ip1, ip2):

    subnet = "255.255.0.0"
    if IPNetwork("{}/{}".format(ip1, subnet)) == IPNetwork("{}/{}".format(ip2, subnet)):
        return True
    return False


def arp_request(device, message):
    ret = 0
    for i in device.connected_to:
        ret = i.respond_arp(message, device)
        if ret != 0:
            message['H2'].append(ret.MACaddress)
    print("\n")
    return message


def send_message(d1, message, ack_msg=False):
    print("\u001b[34m")
    print(message)
    print("\u001b[30m")
    print(d1)
    for i in d1.connected_to:
        i.respond_send(message, d1, ack_msg)


def swap_address(array):
    temp = array[0]
    array[0] = array[1]
    array[1] = temp
    return array


def generate_ack(message):
    message['Data'] = 'ACK'
    message['H3'] = swap_address(message['H3'])
    message['H2'] = swap_address(message['H2'])
    return message


def check_subnet(ip1, ip2):

    subnet = "255.255.0.0"
    if IPNetwork("{}/{}".format(ip1, subnet)) == IPNetwork("{}/{}".format(ip2, subnet)):
        return True
    return False


def respond_send(self, message, sender, ack_msg=False):
    if message['H2'][0] not in self.mac_table[sender.port]:
        self.mac_table[sender.port].append(message['H2'][0])
    if message['H2'][1] in self.mac_table[sender.port]:
        return
    elif message['H2'][1] not in self.mac_table[sender.port]:

        for i in self.connected_to:
            if i.port != sender.port:
                i.respond_send(message, self, ack_msg)
    else:
        message, reciever = arp_request(self, message)
        self.mac_table[reciever.port].append(message['H2'][1])


class Switch(Bridge):
    def __init__(self, id, address, ports=[80, 8080, 8090, 8000, 8070], active=True):
        self.id = id
        self.mac_table = {}
        self.address = address
        self.ports = ports
        for i in ports:
            self.mac_table[i] = []
        self.connected_to = []
        self.active = active

    def respond_send(self, message, sender, ack_msg=False):
        if message['H2'][0] not in self.mac_table[sender.port]:
            self.mac_table[sender.port].append(message['H2'][0])
        if message['H2'][1] in self.mac_table[sender.port]:
            return
        elif message['H2'][1] not in self.mac_table[sender.port]:

            forward_port = 0
            for key in self.mac_table.keys():
                if message['H2'][1] in self.mac_table[key]:
                    forward_port = key
                    break
            for i in self.connected_to:
                if i.port == forward_port:
                    i.respond_send(message, self, ack_msg)
        else:
            message, reciever = arp_request(self, message)
            self.mac_table[reciever.port].append(message['H2'][1])


class Router():
    def __init__(self, id, num_interface, active=True):
        self.id = id
        self.num_interface = num_interface
        self.interface = [0]*num_interface
        self.active = active
        self.connected_to_interface = [0] * num_interface
        self.router_table = {}
        self.arp_table = {}

    def make_active(self):
        self.active = True

    def make_inactive(self):
        self.active = False

    def init_rip(self):
        for i in range(len(self.interface)):
            if self.interface[i] == 0:
                continue
            self.router_table[self.interface[i][0].network] = [
                0, self.interface[i][0].netmask, i, '-']

    def respond_arp(self, message, device):
        if message['H3'][1].network == message['H3'][0].network:
            print("Router {} rejected the ARP Request".format(self.id))
            return 0
        return 0

    def arp_request(self, message, interface):
        """ARP Request Method To Get MAC Address Using IP Address Of Receiver"""
        ret = 0
        print("ARP Request Sent By Device {}".format(self.id))
        i = self.connected_to_interface[interface]
        ret = i.respond_arp(message, self)
        message['H2'].append(ret.address)
        print(message)
        return message

    def check_longest_mask(self, mask, val):
        minimum = val
        for key, value in self.router_table.items():
            if key == mask:
                if value[2] < val[2]:
                    minimum = value
        return minimum

    def respond_send(self, message, sender, ack_msg=False):
        print("Message At Router {}".format(self.id))
        if message['H3'][1].network == message['H3'][0].network:
            print("Packet Rejected By Router {}".format(self.id))
            self.arp_table[message['H3'][0]] = message['H2'][0]
            self.arp_table[message['H3'][1]] = message['H2'][1]
            return
        elif message['H3'][1].network not in self.router_table.keys():
            print("No Hop Available")
            return
        else:
            for i in self.router_table:
                if message['H3'][1].network == i:
                    if self.router_table[i][-1] == '-' and message['H3'][1] not in self.arp_table.keys():
                        message = self.arp_request(
                            message, self.router_table[i][2])
                        self.arp_table[message['H3'][1]] = message['H2'][1]
                        self.arp_table[message['H3'][0]] = message['H2'][0]
                        return self.connected_to_interface[self.router_table[i][2]].respond_send(message, self, ack_msg)
                    return self.connected_to_interface[self.router_table[i][-1]].respond_send(message, self, ack_msg)

    def find_interface(self, device):
        for i in range(len(self.connected_to_interface)):
            if self.connected_to_interface[i] == device:
                return i
        return -1

    def make_RIP_table(self, list_of_routers):
        for _ in range(len(list_of_routers)):
            for j in list_of_routers:
                if j == self:
                    continue

                for k, v in j.router_table.items():
                    if (k not in self.router_table.keys()) or (k in self.router_table.keys() and self.router_table[k][-1] == -1):
                        if self.find_interface(j) != -1:
                            self.router_table[k] = [
                                v[0]+1, v[1], v[2], self.find_interface(j)]
                    else:
                        if self.router_table[k][0] > v[0]+1:
                            self.router_table[k] = [
                                v[0]+1, v[1], v[2], self.find_interface(j)]

    def config_interface_ip(self, int_id, ip):
        self.interface[int_id] = [ip, "Random MAC Address"]


class HTTP:
    def __init__(self, id):
        self.id = id
        self.port = 80

    def use(self):
        print("Using HTTP Application")


class SSH:
    def __init__(self):
        self.id = id
        self.port = 22

    def use(self):
        print("Using SSH Application")


class Network:
    """Basic Interface Class Where All Devices And Initialized To Form A Network Engine."""

    def __init__(self):
        """Default Constructor"""
        self.num_devices = 0
        self.num_hubs = 0
        self.num_bridges = 0
        self.num_switches = 0
        self.num_routers = 0
        self.__devices = []
        self.total_devices = 0
        self.connections = []

    def add_device(self, device):
        """Method To Add End Devices To Interface"""
        self.num_devices += 1
        self.__devices.append(device)
        self.total_devices += 1
        self.connections.append([])

    def add_hub(self, hub):
        """Method To Add Hubs To Interface"""
        self.num_hubs += 1
        self.__devices.append(hub)
        self.total_devices += 1
        self.connections.append([])

    def add_bridge(self, bridge):
        """Method To Add Bridge To Interface"""
        self.num_bridges += 1
        self.__devices.append(bridge)
        self.total_devices += 1
        self.connections.append([])

    def add_switch(self, swtich):
        """Method To Add Switch To Interface"""
        self.num_switches += 1
        self.__devices.append(swtich)
        self.total_devices += 1
        self.connections.append([])

    def add_router(self, router):
        """Method To Add Router To Interface"""
        self.num_routers += 1
        self.__devices.append(router)
        self.total_devices += 1
        self.connections.append([])

    def check_valid_device(self, d1, d2):
        """Checks If Device Id Exists."""
        if d1 >= self.total_devices or d2 >= self.total_devices:
            raise Exception(
                "Device Dosent Exist! Please Enter Valid Device Numbers.")

    def check_device_status(self, d1, d2):
        """Checks If Both Devices Are Active"""
        if not ((self.__devices[d1].active) and (self.__devices[d2].active)):
            raise Exception("Device Not Active. Please Check Device Status")

    def check_connection(self, d1, d2):
        """Checks If Connection Between Devices Exists Or Not"""
        # Check if it is possible to send message via any connection.
        for i in self.connections[d1]:
            if type(i) == devices.hubs:
                i.broadcast(d1, d2)
                break
        if self.__devices[d2] in self.connections[d1]:
            return
        else:
            raise Exception("No Connection Between Two Devices!")

    def make_connection(self, d1, d2, interface=-1):
        """Method To Make Connection Between Two Devices. Takes Devices ID as inputs."""
        try:
            self.check_valid_device(d1, d2)
            self.connections[d1].append(self.__devices[d2])
            self.connections[d2].append(self.__devices[d1])
            if type(self.__devices[d1]) == Router:
                self.__devices[d1].connected_to_interface[interface] = self.__devices[d2]
            else:
                self.__devices[d1].connected_to.append(self.__devices[d2])
            if type(self.__devices[d2]) == Router:
                self.__devices[d2].connected_to_interface[interface] = self.__devices[d1]
            else:
                self.__devices[d2].connected_to.append(self.__devices[d1])
        except Exception as e:
            print("Invalid Input! Please Check And Enter Again!")
            print(e)

    def send_msg(self, sender_device, receiver_device, text, window_size, sequence=-1):
        """Method To Send Message. Take Sender And Receiver Id along with message to send and window size to be used.
        Uses Stop And Wait ARQ. """
        global token
        while token != sender_device:
            print(
                "Device {} is currently using the token. Waiting For Access".format(token))
            time.sleep(0.5)
        print("Device {} has the token.".format(sender_device))
        seq = 0
        for m in text.split():
            message = make_packets(
                self.__devices[sender_device], self.__devices[receiver_device], m)
            if(self.__devices[sender_device].ip.network != self.__devices[receiver_device].ip.network):
                message['Seq'] = 1
                print("Sending Packet To Default Gateway {}".format(
                    self.__devices[sender_device]))
                for i in self.__devices[sender_device].connected_to:
                    if type(i) == Switch or type(i) == hubs:
                        for j in i.connected_to:
                            if type(j) == Router:
                                return j.respond_send(message, self.__devices[sender_device])
                    elif type(i) == Router:
                        return i.respond_send(message, self.__devices[sender_device])
            # Make Check If Device Is In Same Network Or Not:  TODO: SUBNET FOR ROUTERS!
            if self.__devices[receiver_device].ip in self.__devices[sender_device].arp_table.keys():
                message['H2'].append(
                    self.__devices[sender_device].arp_table[self.__devices[receiver_device].ip.ip])
            else:
                message = arp_request(self.__devices[sender_device], message)
                self.__devices[sender_device].arp_table[self.__devices[receiver_device]
                                                        .ip.ip] = self.__devices[receiver_device].MACaddress
            try:
                if len(message['H2']) == 1:
                    raise Exception("NO Connection Exists!")
                if sequence == -1:
                    message['Seq'] = (seq) % window_size
                    seq = (seq+1) % window_size
                else:
                    message['Seq'] = sequence % window_size
                self.check_valid_device(sender_device, receiver_device)
                self.check_device_status(sender_device, receiver_device)
                send_message(self.__devices[sender_device], message)
            except Exception as e:
                print(e)

    def selective_repeat(self, sender_device, receiver_device, text, window_size):
        """Sends Message Using Selective Repeat ARQ"""
        i = 0
        message = text.split()
        while(i < len(message)):
            if i < len(message):
                self.send_msg(sender_device, receiver_device,
                              message[i], window_size, i)
                i += 1
            if i < len(message):
                threading.Thread(target=self.send_msg, args=(
                    sender_device, receiver_device, message[i], window_size, i)).start()
                i += 1
            if i < len(message):
                threading.Thread(target=self.send_msg, args=(
                    sender_device, receiver_device, message[i], window_size, i)).start()
                i += 1
            if i < len(message):
                threading.Thread(target=self.send_msg, args=(
                    sender_device, receiver_device, message[i], window_size, i)).start()
                i += 1

    def make_active(self, number):
        """Make Device Active."""
        self.__devices[number].active = True

    def make_inactive(self, number):
        """Make Device InActive."""
        self.__devices[number].active = False

    def collision_domain_util(self, dev, visited):
        """Util Function To Calculate Collision Domain."""
        visited[dev.id] = 1
        cd = 0
        if type(dev) == Switch or type(dev) == Bridge:
            for i in dev.connected_to:
                if not visited[i.id]:
                    visited[i.id] = 1
                    cd += 1
            for i in dev.connected_to:
                if not visited[i.id]:
                    cd += self.collision_domain_util(i, visited)
            return cd
        elif type(dev) == devices.hubs:
            to_add = True
            for i in dev.connected_to:
                if visited[i.id] == 1:
                    to_add = False
                if visited[i.id] == 0:
                    visited[i.id] = 1
                    cd += self.collision_domain_util(i, visited)
            if to_add:
                cd += 1
            return cd
        else:
            return 0

    def get_collision_domain(self):
        """Function To Check Collision Domain In the Network"""
        switches = [i for i in self.__devices if type(i) == Switch]
        bridges = [i for i in self.__devices if type(i) == Bridge]
        hubs = [i for i in self.__devices if type(i) == devices.hubs]
        visited = [0] * self.total_devices
        cd = 0
        for i in switches:
            if not visited[i.id]:
                cd += self.collision_domain_util(i, visited)
        for i in bridges:
            if not visited[i.id]:
                cd += self.collision_domain_util(i, visited)
        for i in hubs:
            if not visited[i.id]:
                cd += self.collision_domain_util(i, visited)
        return cd

    # def visualise_network(self):
    #     """Method TO Visualize Connection In Form Of A Connected Graph."""
    #     G = nx.Graph()
    #     labels = {}
    #     node_colors = []
    #     for i in range(self.total_devices):
    #         G.add_node(i)
    #     for i in range(self.num_devices):
    #         node_colors.append("blue")
    #         labels[i] = "Device-"+str(i)
    #     for i in range(self.num_hubs):
    #         node_colors.append("red")
    #         labels[i+self.num_devices] = "Hub-"+str(i)
    #     for i in range(self.num_bridges):
    #         node_colors.append("yellow")
    #         labels[i+self.num_devices+self.num_hubs] = "Bridge-"+str(i)
    #     for i in range(self.num_switches):
    #         node_colors.append("green")
    #         labels[i+self.num_devices+self.num_hubs +
    #                self.num_bridges] = "Switch-"+str(i)
    #     for i in range(self.num_routers):
    #         node_colors.append("orange")
    #         labels[i+self.num_devices+self.num_hubs +
    #                self.num_bridges+self.num_switches] = "Router-"+str(i)
    #     for i in range(len(self.connections)):
    #         for j in self.connections[i]:
    #             G.add_edge(i, j.id)
    #
    #     nx.draw_networkx(G, labels=labels, node_size=4000,
    #             node_color=node_colors, alpha=0.7)
    #
    #     plt.axis('off')
    #     plt.show()


""""Code For Token Passing. Switches Token After Every 0.5 secs"""
token = 0


def get_token(num_devices):
    global token
    while True:
        token = (token+1) % num_devices
        time.sleep(0.5)


def main():
    N1 = Network()
    N1.add_device(devices(N1.total_devices, generate_mac_address(),
                          IPNetwork('10.0.0.2/8'), IPNetwork('10.0.0.1/8'), HTTP(690)))
    N1.add_device(devices(N1.total_devices, generate_mac_address(),
                          IPNetwork('10.0.0.3/8'), IPNetwork('10.0.0.1/8'), HTTP(100)))
    N1.add_device(devices(N1.total_devices, generate_mac_address(),
                          IPNetwork('40.0.0.2/8'), IPNetwork('40.0.0.1/8'), HTTP(8081)))
    N1.add_device(devices(N1.total_devices, generate_mac_address(),
                          IPNetwork('40.0.0.3/8'), IPNetwork('40.0.0.1/8'), HTTP(3000)))

    N1.add_hub(hubs(N1.total_devices, 1))
    r1 = Router(N1.total_devices, 3)
    r1.config_interface_ip(0, IPNetwork('10.0.0.1/8'))
    r1.config_interface_ip(1, IPNetwork('20.0.0.2/8'))
    r1.config_interface_ip(2, IPNetwork('50.0.0.2/8'))
    r1.init_rip()
    N1.add_router(r1)
    r2 = Router(N1.total_devices, 3)
    r2.config_interface_ip(1, IPNetwork('40.0.0.1/8'))
    r2.config_interface_ip(0, IPNetwork('30.0.0.2/8'))
    r2.config_interface_ip(2, IPNetwork('50.0.0.1/8'))
    r2.init_rip()
    N1.add_router(r2)
    r3 = Router(N1.total_devices, 2)
    r3.config_interface_ip(1, IPNetwork('20.0.0.1/8'))
    r3.config_interface_ip(0, IPNetwork('30.0.0.1/8'))
    r3.init_rip()
    s1 = Switch(N1.total_devices, IPNetwork('30.0.0.1/8'))
    N1.add_switch(s1)
    N1.add_router(r3)
    N1.make_connection(0, 3)
    N1.make_connection(1, 4)
    N1.make_connection(4, 5)
    N1.make_connection(3, 5, 0)
    N1.make_connection(4, 6, 1)
    N1.make_connection(5, 7, 1)
    N1.make_connection(7, 2, 1)
    N1.make_connection(6, 8, 0)
    N1.make_connection(5, 8, 1)
    N1.make_connection(7, 8, 0)
    rs = [r1, r2, r3]
    for m in range(len(rs)):
        for n in rs:
            n.make_RIP_table(rs)
    for n in rs:
        print(n.router_table)

    N1.send_msg(0, 2, "Device0ToDevice1", 2)
    # N1.visualise_network()


if __name__ == "__main__":
    main()
