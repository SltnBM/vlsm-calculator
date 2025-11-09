# 📐 VLSM Calculator - Subnet Planner CLI
A simple command-line tool to calculate subnet allocations using Variable Length Subnet Masking (VLSM).  
Built for educational and practical use in subnet planning.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Requirements](https://img.shields.io/badge/requirements.txt-up%20to%20date-brightgreen)

---

## ✨ Features
- Calculates optimal subnet divisions based on required host counts
- Detailed output including Network Address, Broadcast Address, Subnet Mask, Wildcard Mask, and Usable IP Range
- Interactive CLI input for network and host requirements
- Supports command-line arguments
- Continuous input mode with validation and graceful exit
- Lightweight, beginner-friendly, and easy to use
- Optional export of results to Excel (.xlsx)

---

## 📋 Requirements
1. Python 3.6 or higher
2. [`netaddr`](https://pypi.org/project/netaddr/)
3. [`rich`](https://pypi.org/project/rich/)
4. [`openpyxl`](https://pypi.org/project/openpyxl/)

Install dependencies:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install netaddr rich openpyxl
```

---

## 🚀 How to Use
1. Make sure you have Python installed (Python 3.6 or higher). Download it from [python.org](https://www.python.org/downloads/).
2. Clone the repository
```bash
git clone https://github.com/SltnBM/vlsm-calculator.git
```
Alternatively, you can Download ZIP if preferred.

3. Navigate to the project directory
```bash
cd vlsm-calculator
```
4. Run the script
```bash
python vlsm_calculator.py
```

---

## 💻 Usage
### Option 1: With CLI arguments
```bash
python vlsm_calculator.py -n <network> -H <hosts> [<hosts> ...]
```
Example:
```bash
python vlsm_calculator.py -n 192.168.1.0/24 -H 50 30 10
```

### Option 2: Interactive mode
If no arguments are provided, the script will ask for input:
```bash
python vlsm_calculator.py
```
Example (Interactive mode)
```plaintext
Enter network address (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter number of required subnets: 3
Enter required hosts for subnet 1: 50
Enter required hosts for subnet 2: 30
Enter required hosts for subnet 3: 10
```

### Example output
```plaintext
=== VLSM SUBNET CALCULATOR (type 'exit' to quit) ===

Enter network address (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter number of required subnets: 3
Enter required hosts for subnet 1: 50
Enter required hosts for subnet 2: 30
Enter required hosts for subnet 3: 10
                                                                                         VLSM Subnet Calculation                                                                                          
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Name        ┃     Hosts Needed ┃      Hosts Available ┃     Unused Hosts ┃ Network Address      ┃ Broadcast         ┃ Usable Range                         ┃ Slash   ┃ Mask                ┃ Wildcard  ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Subnet 1    │               50 │                   62 │               12 │ 192.168.1.0          │ 192.168.1.63      │ 192.168.1.1 - 192.168.1.62           │ /26     │ 255.255.255.192     │ 0.0.0.63  │
│ Subnet 2    │               30 │                   30 │                0 │ 192.168.1.64         │ 192.168.1.95      │ 192.168.1.65 - 192.168.1.94          │ /27     │ 255.255.255.224     │ 0.0.0.31  │
│ Subnet 3    │               10 │                   14 │                4 │ 192.168.1.96         │ 192.168.1.111     │ 192.168.1.97 - 192.168.1.110         │ /28     │ 255.255.255.240     │ 0.0.0.15  │
└─────────────┴──────────────────┴──────────────────────┴──────────────────┴──────────────────────┴───────────────────┴──────────────────────────────────────┴─────────┴─────────────────────┴───────────┘

Tip: Having trouble with the table layout? Try resizing your terminal and run it again.

Do you want to export the result to Excel? (y/n): y
✔ Exported to vlsm_result.xlsx
```

---

## 🤝 Contributing
Contributions are welcome. Feel free to open issues or submit pull requests for improvements.

---

## 📬 Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sultan%20Badra-blue?logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/sultan-badra)

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
