from netaddr import IPNetwork
from rich import print
from rich.table import Table
import argparse
import sys

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
    table = Table(title="[bold green]VLSM Subnet Calculation[/]", expand=True)

    table.add_column("Name", style="bold yellow", no_wrap=True)
    table.add_column("Hosts Needed", justify="right", no_wrap=True)
    table.add_column("Hosts Available", justify="right", no_wrap=True)
    table.add_column("Unused Hosts", justify="right", no_wrap=True)
    table.add_column("Network Address", style="green", no_wrap=True)
    table.add_column("Broadcast", style="green", no_wrap=True)
    table.add_column("Usable Range", style="green", overflow="fold", min_width=25)
    table.add_column("Slash", style="blue", no_wrap=True)
    table.add_column("Mask", style="magenta", no_wrap=True)
    table.add_column("Wildcard", style="red", no_wrap=True)

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
    print("\n[bold red]Tip:[/] Having trouble with the table layout? Try resizing your terminal and run it again.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VLSM Subnet Calculator")
    parser.add_argument("-n", "--network", type=str, help="Network address in CIDR (e.g., 192.168.1.0/24)")
    parser.add_argument("-H", "--hosts", type=int, nargs="+", metavar="N", help="List of required hosts per subnet (e.g., -H 50 30 10)")
    args = parser.parse_args()

    print("\n[bold cyan]=== VLSM SUBNET CALCULATOR (type 'exit' to quit) ===[/]")

    if args.network and args.hosts:
        try:
            network = IPNetwork(args.network)
            subnets = calculate_vlsm(network, args.hosts)
            print_vlsm_table(subnets)
            sys.exit(0)
        except Exception as e:
            print(f"[bold red]Invalid network:[/] {e}")
            sys.exit(1)

    while True:
        try:
            while True:
                try:
                    network_input = input("\nEnter network address (e.g., 192.168.1.0/24): ").strip().replace(" ", "")
                    if network_input.lower() == "exit":
                        print("[bold red]Exiting. Goodbye![/]")
                        sys.exit(0)
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