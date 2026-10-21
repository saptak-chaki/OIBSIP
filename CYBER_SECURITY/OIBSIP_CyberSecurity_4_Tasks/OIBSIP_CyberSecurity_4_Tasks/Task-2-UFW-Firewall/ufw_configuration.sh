#!/usr/bin/env bash
# OIBSIP Task 2 — UFW sample configuration
# Review before use. Run ONLY on a machine/VM you control.
# Warning: firewall rules can affect connectivity.

set -euo pipefail

sudo ufw allow ssh
sudo ufw deny http
sudo ufw allow https

# OPTIONAL: allow DNS service traffic only if this machine is intentionally
# running a DNS server. Remove/comment out if not needed.
# sudo ufw allow 53/udp

sudo ufw --force enable
sudo ufw status verbose
