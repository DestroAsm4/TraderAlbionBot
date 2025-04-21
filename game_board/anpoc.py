import scapy.all as scapy

from datetime import datetime
from collections import Counter

from scapy.sendrecv import sniff


def analyze_packet(packet):
    src_ip = None
    dst_ip = None
    protocol = None

    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = "IP"
    elif packet.haslayer(scapy.IPv6):
        src_ip = packet[scapy.IPv6].src
        dst_ip = packet[scapy.IPv6].dst
        protocol = "IPv6"

    if packet.haslayer(scapy.TCP):
        protocol += " TCP"
    elif packet.haslayer(scapy.UDP):
        protocol += " UDP"
    elif packet.haslayer(scapy.ICMP):
        protocol += " ICMP"

    return {
        'time': datetime.now(),
        'src_ip': src_ip,
        'dst_ip': dst_ip,
        'protocol': protocol,
        'length': len(packet)
    }


# def is_suspicious(packet_info):
#     if packet_info['protocol'] == "IP TCP" and packet_info['length'] & gt; 1500:
#         return True
#     if packet_info['protocol'] == "IP UDP" and packet_info['length'] & gt; 1000:
#         return True
#     return False
#
#
# def is_alarming(packet_info):
#     if packet_info['protocol'] == "IP TCP" and packet_info['length'] & gt; 1000:
#         return True
#     if packet_info['protocol'] == "IP UDP" and packet_info['length'] & gt; 800:
#         return True
#     return False





def main():
    print("Запуск перехвата сетевых пакетов...")
    captured_packets = []

    def packet_callback(packet):
        packet_info = analyze_packet(packet)
        captured_packets.append(packet_info)

    try:
        scapy.sniff(prn=packet_callback, store=0, timeout=5)
    except Exception as e:
        print(f"Ошибка во время перехвата: {e}")
        return
    for pac in captured_packets:
        if pac['src_ip'] == '5.188.125.14':
            print(pac)

    print("Перехват завершен. Отчет создан.")

# x = b'\x17\x03\x03\x01B\x15\xa7G\xb5n\xdd\xa0=D:\xd2C\x9b\xa3\x88\x1a}\xaa\xbe\x11zt\xe8\xc6Cx\xb0\n\xd7\xad\xd7F\x19\xbd\x0e\xe5\xc5\xaf\x1e\xd4\xd6\x92\x1f\xdcp\x9d\x82\xf1V\xc8Y^\x90Sp\xd0\x9ct\xb9+\xc2\x1b\xd4\xd4\xbe\x87#\xfe\xd4\xfd\xdd\xf4\x0e\xc50I\xbb\x13\xb1\xa6\xd4\xc7\xc1\nxJ\xde\x0f\x13\xeb\\j\x93Lf\xc5\xa4\x842\xfd\x84\xd5\xa7\xff\x1b5\x18\x15e8\xdd2\x02?\xfa\xfa"Qi\xdbxi>~\xd2\xda\xce\xce\x98\xaa/\xca\x06#\xdb\xec\xb2\x8ef^>\x08X,\xce;\xc2\x1c\xbc\x12\xd8\xda\x89t\xf9\x01\xa6D\xbd-\x89\rY_(\xe4\x93\xec\xf8\xe1\x16\xfe\x80\xe9\x0f\xaek\xcd\xf0\x0b\xecsiI\xab>u8\x89)\x01\xeb\xd9\x8e.\xe8\ts\x84s8\xce \x13\x0c\xe8\x82\x14\x9f4\xc0T\xc8A\x8d?\xb3l2\x9c\x94\xdfb\x84\x83\x10,\x97\xa6\x949\xf8\xd5\xf3\xe5b\xaf\xc6 \r\xdd\xaes\x0eb\x9d\xaaF.`\xb4P\xff0\x16\x85\x98-Of\x15n\xc0*\x84H\xcd^0\xb9B\r\x17\xa9PS\xd4\xe5\xbf6\x9e\x8bs1\x01!\xbaE\xc5\x80\x8d\x1f\x9f\xf4\xe4\xc3\xfd\xdf\x9d\x93.I\xb1\xbb\x7f\xa9\xd0\xa7\xcee\xf0\x8a\x04\x97\x96u\x0b|\xb7\x9b\xc4('
if __name__ == "__main__":
    # x = b'\x01'
    # x = b'x01B\x15\xa7G\xb5n\xdd'
    # print(x.decode('ascii'))
    pkts = sniff(prn=lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    # pkts = sniff(prn=lambda x: x.))
    # input_bytes = b"\2D"
    # output_numbers = list(input_bytes)
    # result = []
    # for w in output_numbers:
    #     # print(w)
    #     data = ascii(w)
    #     print(data)
        # print('{:b}'.format(w.decode('utf-8')))
        # result.append(ascii(w))
    # print(result)
    # main()