# Task 2 — Basic Firewall Configuration with UFW

## Objective
Use UFW (Uncomplicated Firewall) to apply and verify inbound firewall rules on an Ubuntu/Kali test machine.

## Safety first
Use a local VM or a machine you control. Firewall changes can interrupt network access. If connected remotely through SSH, do not enable or change rules unless you have confirmed SSH access will remain allowed and you have console recovery access.

## Install and inspect
```bash
sudo apt update
sudo apt install ufw
sudo ufw status verbose
```

## Configuration script
Review `ufw_configuration.sh` before running. The provided script allows SSH and HTTPS and denies HTTP, matching the task guide's example. If you are not using SSH, you can remove that rule after understanding the consequences.

Run:
```bash
chmod +x ufw_configuration.sh
sudo ./ufw_configuration.sh
sudo ufw status verbose
```

## What the rules mean
- `allow ssh`: allows incoming SSH (normally TCP port 22).
- `deny http`: blocks incoming HTTP (normally TCP port 80).
- `allow https`: allows incoming HTTPS (normally TCP port 443).
- `allow 53/udp`: permits UDP DNS traffic to this machine; keep only if this machine actually needs to serve DNS. It is included as an optional example and should be removed if not needed.

**Least privilege:** only open ports required for your machine's role. Do not add rules just to increase the number of rules.

## Verification
Record the actual output of:
```bash
sudo ufw status verbose
```
Test from another machine in your own isolated lab, or use a local service and explain the test method. A rule listing alone does not prove end-to-end blocking.

## Evidence checklist
- [ ] Screenshot of `sudo ufw status verbose`
- [ ] Screenshot or notes showing your test method and actual result
- [ ] Explain why each selected rule is needed
- [ ] Commit the script, README, and genuine screenshots

## References
- Ubuntu UFW community documentation: https://help.ubuntu.com/community/UFW
- Ubuntu Server firewall documentation: https://documentation.ubuntu.com/server/how-to/security/firewalls/
