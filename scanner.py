import scapy.all as scapy
import argparse

def get_args():
    """This function allows us to pass arguments along with the script"""
    parser =  argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Addresses')
    option = parser.parse_args()

    #Sprawdzamy czy argument został podany
    if not option.target:
        parser.error('Please specify an IP address or addresses, use --help for me info')
    return option


def scan(ip):
    """Function that receives arguments and scans the host/hosts"""
    arp_req_frame = scapy.ARP(pdst = ip)
    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") 
    braodcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(braodcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []

    for i in range(0,len(answered_list)):
        client_dict = {"ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
        result.append(client_dict)
    
    return result

def display_result(result):
        print("-----------------------------------\nIP Address\tMAC Address\n-----------------------------------")
        for i in result:
             print("{}\t{}".format(i["ip"], i["mac"]))


option = get_args()
scanned_output = scan(option.target)
display_result(scanned_output)
        