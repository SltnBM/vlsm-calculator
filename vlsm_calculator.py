from netaddr import IPNetwork, AddrFormatError 

def get_valid_network():
    while True:
        network_input = input("Enter network address (e.g., 192.168.1.0/24): ").strip().replace(" ", "")
        try:
            return IPNetwork(network_input)
        except AddrFormatError:
            print("Invalid network format. Example: 192.168.1.0/24")

def calculate_vlsm(network, hosts_required):
    hosts_required.sort(reverse=True)
    current_network = network
    subnets = []

    for hosts_needed in hosts_required:
        prefix = 32 - (hosts_needed + 2 - 1).bit_length()
        subnet = IPNetwork(f"{current_network.network}/{prefix}")
        hosts_available = subnet.size - 2
        unused_hosts = hosts_available - hosts_needed
        usable_range = f"{subnet.network + 1} - {subnet.broadcast - 1}"
        wildcard = subnet.hostmask

        subnets.append({
            "Name": f"Subnet {len(subnets)+1}",
            "Hosts Needed": hosts_needed,
            "Hosts Available": hosts_available,
            "Unused Hosts": unused_hosts,
            "Network Address": str(subnet.network),
            "Broadcast": str(subnet.broadcast),
            "Usable Range": usable_range,
            "Slash": f"/{prefix}",
            "Mask": str(subnet.netmask),
            "Wildcard": str(wildcard)
        })

        next_network = subnet.broadcast + 1
        current_network = IPNetwork(f"{next_network}/{prefix}")

    return subnets

def print_vlsm_table(subnets):
    print("\n{:<10}{:<15}{:<17}{:<15}{:<18}{:<18}{:<33}{:<7}{:<18}{}".format(
        "Name", "Hosts Needed", "Hosts Available", "Unused Hosts", "Network Address",
        "Broadcast Address", "Usable Range", "Slash", "Mask", "Wildcard"
    ))
    for s in subnets:
        print("{:<10}{:<15}{:<17}{:<15}{:<18}{:<18}{:<33}{:<7}{:<18}{}".format(
            s["Name"], s["Hosts Needed"], s["Hosts Available"], s["Unused Hosts"],
            s["Network Address"], s["Broadcast"], s["Usable Range"], s["Slash"],
            s["Mask"], s["Wildcard"]
        ))

if __name__ == "__main__":
    network = get_valid_network()

    try:
        num_subnets = int(input("Enter number of required subnets: ").strip())
        hosts_list = []

        for i in range(num_subnets):
            while True:
                try:
                    host = int(input(f"Enter required hosts for subnet {i+1}: ").strip())
                    if host > 0:
                        hosts_list.append(host)
                        break
                    else:
                        print("Number must be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")

        if not hosts_list:
            raise ValueError("No valid host numbers provided.")

        subnets = calculate_vlsm(network, hosts_list)
        print_vlsm_table(subnets)

    except Exception as e:
        print(f"Error: {e}")
