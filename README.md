# 📐 VLSM Calculator
A simple command-line tool to calculate subnet allocations using Variable Length Subnet Masking (VLSM).  
Built for educational and practical use in subnet planning.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)

## ✨ Features
- Calculate optimal subnet divisions from required hosts
- Detailed output: Network Address, Broadcast, Mask, Wildcard, Usable Range
- Interactive CLI input
- Simple and easy to use

## 📋 Requirements
1. 🐍 Python 3.6 or higher
2. 📦 netaddr

Install dependencies:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install netaddr
```

## How to Use
1. Make sure you have Python installed (Python 3.6 or higher). Download it from [python.org](https://www.python.org/downloads/).
2. 📥 Clone the repository
```bash
git clone https://github.com/yourusername/vlsm-calculator.git
```
3. 📂 Navigate to the project directory
```bash
cd vlsm-calculator
```
4. ▶️ Run the script
```bash
python vlsm_calculator.py
```

## 💻 Usage
Interactive mode
```bash
python vlsm_calculator.py
```

Example
```plaintext
Enter network address (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter number of required subnets: 3
Enter required hosts for subnet 1: 50
Enter required hosts for subnet 2: 30
Enter required hosts for subnet 3: 10
```

Example output
```plaintext
Name      Hosts Needed   Hosts Available  Unused Hosts   Network Address   Broadcast Address Usable Range                     Slash  Mask              Wildcard
Subnet 1  50             62               12             192.168.1.0       192.168.1.63      192.168.1.1 - 192.168.1.62       /26    255.255.255.192   0.0.0.63
Subnet 2  30             30               0              192.168.1.64      192.168.1.95      192.168.1.65 - 192.168.1.94      /27    255.255.255.224   0.0.0.31
Subnet 3  10             14               4              192.168.1.96      192.168.1.111     192.168.1.97 - 192.168.1.110     /28    255.255.255.240   0.0.0.15
```

## 🤝 Contributing
Contributions are welcome. Feel free to open issues or submit pull requests for improvements.

## 📬 Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sultan%20Badra-blue?logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/sultan-badra)

## 📜 License
This project is open source and free to use.