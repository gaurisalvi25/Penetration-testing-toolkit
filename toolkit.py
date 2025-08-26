import argparse
from scanner import port_scan
from bruteforcer import brute_force

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Port scanner
    scan_parser = subparsers.add_parser("scan", help="Run port scanner")
    scan_parser.add_argument("target", help="Target IP or domain")
    scan_parser.add_argument("--ports", nargs="+", type=int, required=True, help="Ports to scan")

    # Brute-forcer
    brute_parser = subparsers.add_parser("bruteforce", help="Run brute force attack")
    brute_parser.add_argument("url", help="Target login URL")
    brute_parser.add_argument("username", help="Username to attack")
    brute_parser.add_argument("wordlist", help="Password wordlist file")

    args = parser.parse_args()

    if args.command == "scan":
        port_scan(args.target, args.ports)

    elif args.command == "bruteforce":
        brute_force(args.url, args.username, args.wordlist)

if __name__ == "__main__":
    main()

