# Task 1 — Basic Network Scanning with Nmap

## Objective
Use Nmap to identify hosts, open ports, services, and possible exposure on a system or lab network that you own or are authorised to test.

## Ethics and scope
**Target:** `127.0.0.1` (your own computer) or a lab VM you control  
**Time window:** Fill in date/time of your scan  
**Authorisation:** Local system / authorised lab only

Never scan university, public, company, or third-party systems without explicit permission.

## Install
On Ubuntu/Kali:
```bash
sudo apt update
sudo apt install nmap
nmap --version
```

## Run a basic local scan
```bash
nmap 127.0.0.1 -oN nmap_scan_results.txt
```

To identify service versions on your own lab target:
```bash
nmap -sV <YOUR_AUTHORISED_LAB_IP> -oN nmap_scan_results.txt
```
Replace the placeholder only with a lab IP you are authorised to scan. OS detection (`-O`) may require elevated privileges and may not work in every environment.

## How to read the result
- **PORT:** port number and protocol.
- **STATE:** `open` means an application is listening; `closed` means reachable but not listening; `filtered` means a firewall or network device prevents Nmap from determining the state.
- **SERVICE:** likely service associated with the port.
- **VERSION:** version information when Nmap can identify it. This may be incomplete or inaccurate.

An open port is not automatically a vulnerability. Verify whether the service is needed, updated, and correctly configured.

## Findings table — fill from your real scan
| Port/Protocol | Service/Version | Why it may matter | Recommended action |
|---|---|---|---|
| Fill from scan | Fill from scan | Explain the exposure without assuming it is vulnerable | Disable if unnecessary; otherwise patch and restrict access |

## Evidence checklist
- [ ] Screenshot showing the command and actual terminal output
- [ ] Save actual output as `nmap_scan_results.txt`
- [ ] Add target, date/time, and scope to this README
- [ ] Explain at least one observed port/service, or state that no open ports were found
- [ ] Commit report and screenshot to GitHub

## References
- Nmap Reference Guide: https://nmap.org/book/man.html
- Nmap documentation: https://nmap.org/docs.html
