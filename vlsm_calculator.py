from netaddr import IPNetwork
from rich import print
from rich.table import Table

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
    table = Table(title="[bold green]VLSM Subnet Calculation[/]")

    table.add_column("Name", style="bold yellow")
    table.add_column("Hosts Needed", justify="right")
    table.add_column("Hosts Available", justify="right")
    table.add_column("Unused Hosts", justify="right")
    table.add_column("Network Address", style="green")
    table.add_column("Broadcast", style="green")
    table.add_column("Usable Range", style="green")
    table.add_column("Slash", style="blue")
    table.add_column("Mask", style="magenta")
    table.add_column("Wildcard", style="red")

    for s in subnets:
        table.add_row(
            s["Name"],
            str(s["Hosts Needed"]),
            str(s["Hosts Available"]),
            str(s["Unused Hosts"]),
            s["Network Address"],
            s["Broadcast"],
            s["Usable Range"],
            s["Slash"],
            s["Mask"],
            s["Wildcard"]
        )

    print(table)

if __name__ == "__main__":
    print("\n[bold cyan]=== VLSM SUBNET CALCULATOR (type 'exit' to quit) ===[/]")

    while True:
        try:
            while True:
                try:
                    network_input = input("\nEnter network address (e.g., 192.168.1.0/24): ").strip().replace(" ", "")
                    if network_input.lower() == "exit":
                        print("[bold red]Exiting. Goodbye![/]")
                        exit()
                    network = IPNetwork(network_input)
                    break
                except Exception:
                    print("[bold red]Invalid network format. Please try again.[/]")

            while True:
                try:
                    num_subnets = int(input("Enter number of required subnets: ").strip())
                    if num_subnets > 0:
                        break
                    else:
                        print("[bold red]Number must be greater than 0.[/]")
                except ValueError:
                    print("[bold red]Please enter a valid number.[/]")

            hosts_list = []
            for i in range(num_subnets):
                while True:
                    try:
                        host = int(input(f"Enter required hosts for subnet {i+1}: ").strip())
                        if host > 0:
                            hosts_list.append(host)
                            break
                        else:
                            print("[bold red]Number must be greater than 0.[/]")
                    except ValueError:
                        print("[bold red]Please enter a valid number.[/]")

            subnets = calculate_vlsm(network, hosts_list)
            print_vlsm_table(subnets)

        except KeyboardInterrupt:
            print("\n[bold red]Exiting. Goodbye![/]")
            break
