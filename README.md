# CodeAlpha_BasicNetworkSniffer(CyberSecurity-Task 1)

Python script using Scapy to capture network packets.

# Project Overview

This project is part of my CodeAlpha Cyber Security Internship.
The goal is to build a Basic Network Sniffer in Python to capture and analyze network packets.

# Features

Capture network packets in real time.

Display Source and Destination IP addresses.

Identify protocols (TCP, UDP, ICMP).

Show ports (source and destination).

Display payload data (if available).

# Technologies Used

Python 3.x

Scapy
 library

Npcap
 (for Windows packet capture)

# Project Structure
CodeAlpha-BasicNetworkSniffer/
│
├── networksniffer.py      # Python script to capture and analyze packets
├── 2025-09-25-17-52-38_XTkq85of.mp4       # Demonstration video of the sniffer in action
├── images/                # Folder containing screenshots and illustrations
│   └── python and scapy
│   └── list of interfaces
└── README.md              # Main project documentation

# How to Run

1-Install Python 3.x if not already installed.

2-Install required libraries:

pip install scapy


3-Install Npcap (Windows) or libpcap (Linux/Mac) to enable packet capturing.

4-Run the sniffer script:

python networksniffer.py


5-Observe real-time network packets, including IP addresses, ports, protocols, and payload.

# References

Scapy Documentation

Npcap Official Site

Python Network Programming tutorials
