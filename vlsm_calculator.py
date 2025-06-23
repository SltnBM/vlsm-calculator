from netaddr import IPNetwork

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
    while True:
        try:
            while True:
                try:
                    network_input = input("\nEnter network address (e.g., 192.168.1.0/24 or type 'exit'): ").strip().replace(" ", "")
                    if network_input.lower() == "exit":
                        print("Exiting. Goodbye!")
                        exit()
                    network = IPNetwork(network_input)
                    break
                except Exception:
                    print("Invalid network format. Please try again.")

            while True:
                try:
                    num_subnets = int(input("Enter number of required subnets: ").strip())
                    if num_subnets > 0:
                        break
                    else:
                        print("Number must be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")

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

            subnets = calculate_vlsm(network, hosts_list)
            print_vlsm_table(subnets)

        except KeyboardInterrupt:
            print("\nExiting. Goodbye!")
            break