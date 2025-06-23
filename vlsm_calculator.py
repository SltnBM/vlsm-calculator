from netaddr import IPNetwork

def calculate_vlsm(network, hosts_required):
    hosts_required.sort(reverse=True)
    current_network = IPNetwork(network)
    subnets = []

    for hosts in hosts_required:
        prefix = 32 - (hosts + 2 - 1).bit_length()
        subnet = IPNetwork(f"{current_network.network}/{prefix}")
        subnets.append(subnet)
        next_network = subnet.broadcast + 1
        current_network = IPNetwork(f"{next_network}/{prefix}")

    return subnets

def print_vlsm_table(subnets):
    print(f"\n{'Subnet':<10}{'Network':<20}{'Broadcast':<20}{'Usable Hosts':<15}{'Subnet Mask'}")
    for i, subnet in enumerate(subnets, 1):
        usable_hosts = subnet.size - 2
        print(f"{f'Subnet {i}':<10}{str(subnet.network):<20}{str(subnet.broadcast):<20}{usable_hosts:<15}{subnet.netmask}")

if __name__ == "__main__":
    network_input = input("Enter network address (e.g., 192.168.1.0/24): ").strip()
    hosts_input = input("Enter required hosts per subnet (comma-separated, e.g., 50,30,10): ").strip()

    try:
        hosts_list = [int(h.strip()) for h in hosts_input.split(",") if h.strip().isdigit()]
        if not hosts_list:
            raise ValueError("No valid host numbers provided.")

        subnets = calculate_vlsm(network_input, hosts_list)
        print_vlsm_table(subnets)

    except Exception as e:
        print(f"Error: {e}")
