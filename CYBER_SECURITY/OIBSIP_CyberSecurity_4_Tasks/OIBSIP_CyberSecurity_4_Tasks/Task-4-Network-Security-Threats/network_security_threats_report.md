# Research Report: Common Network Security Threats

**Track:** Cyber Security  
**Task:** 4 — Research Report: Common Network Security Threats  
**Author:** [Your Name]  
**Date:** [Submission Date]

## 1. Introduction

Computer networks connect users, applications, cloud services, and business systems. If network communication or infrastructure is not properly protected, attackers may interrupt services, impersonate trusted systems, or redirect users to malicious destinations. A successful incident can cause downtime, financial loss, data exposure, reputational damage, and recovery costs. Network security therefore depends on layered controls: secure configuration, monitoring, authentication, encryption, timely patching, and a tested incident-response plan.

## 2. Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS)

### How it works
A DoS attack attempts to make a service unavailable by exhausting a resource such as bandwidth, CPU, memory, or connection capacity. A DDoS attack uses many sources—often compromised devices in a botnet—to generate traffic or requests at a scale that is difficult to block using a single source-based rule.

### Real-world example
In October 2016, the Mirai botnet was used in a major DDoS attack against DNS provider Dyn. The disruption affected access to multiple well-known internet services. This incident demonstrated how insecure Internet of Things devices can be recruited into botnets and how attacks against a shared provider can affect many downstream users.

### Impact
- Websites, APIs, and business applications may become unavailable.
- Customers may be unable to use services or complete transactions.
- Incident response and traffic-mitigation costs can be substantial.
- An outage at a shared provider can have a wide collateral impact.

### Mitigation strategies
1. **Use DDoS protection and upstream filtering:** work with an ISP, CDN, or specialist mitigation provider to absorb and filter large-scale traffic.
2. **Apply rate limits and resilient architecture:** set sensible request limits, use load balancing, caching, autoscaling where appropriate, and capacity planning.
3. **Monitor and rehearse response:** alert on traffic anomalies, maintain an incident runbook, and test failover and escalation procedures.

## 3. Man-in-the-Middle (MITM) Attacks

### How it works
A MITM attack occurs when an attacker positions themselves between two communicating parties and attempts to observe, relay, or alter their traffic. Risk increases when users connect through untrusted networks, ignore certificate warnings, or use protocols that do not authenticate and encrypt communication.

### Real-world example
Public reporting has documented attackers using rogue Wi-Fi access points and malicious proxies to intercept poorly protected sessions. In these scenarios, users may believe they are connected directly to a legitimate service while an intermediary observes or manipulates traffic. This is a recurring attack pattern rather than one single incident.

### Impact
- Credentials, session tokens, or personal information may be exposed.
- Traffic may be altered, leading users to fraudulent content.
- Business communications may lose confidentiality and integrity.
- Stolen session tokens can enable account impersonation.

### Mitigation strategies
1. **Enforce HTTPS/TLS:** use valid certificates, modern TLS configurations, and HSTS where appropriate; never instruct users to ignore certificate warnings.
2. **Use trusted networks and secure remote access:** use a trusted VPN when required, disable automatic connection to unknown Wi-Fi, and verify network names.
3. **Strengthen session security:** use secure, HttpOnly, and SameSite cookie attributes where suitable; rotate sessions after authentication and protect accounts with MFA.

## 4. IP Spoofing

### How it works
IP spoofing means forging the source IP address in packet headers so that traffic appears to come from another address. Spoofing can help obscure an attack's origin or exploit systems that trust traffic based only on source IP. It is also used in some reflection/amplification attacks, where replies are sent to a forged victim address.

### Real-world example
Reflection-based DDoS attacks, including those abusing exposed UDP services, can use spoofed source addresses so that responses are directed at a victim. The victim receives large volumes of reply traffic even though they did not initiate the requests.

### Impact
- Victims may be overwhelmed by reflected traffic.
- Logs can mislead responders about the apparent source of traffic.
- Weak IP-based trust controls may be bypassed.
- Spoofing can complicate attribution and incident investigation.

### Mitigation strategies
1. **Ingress and egress filtering:** configure network equipment to drop packets with source addresses that should not appear on that interface, following BCP 38-style practices.
2. **Do not rely on source IP as the only authentication:** use cryptographic authentication, strong access controls, and MFA for sensitive services.
3. **Reduce reflection opportunities:** secure or restrict exposed UDP services and use DDoS mitigation for internet-facing systems.

## 5. DNS Poisoning / DNS Spoofing

### How it works
DNS poisoning or spoofing aims to cause a resolver or client to use an incorrect DNS answer. A victim may be directed to an attacker-controlled address even when they enter a legitimate domain name. Possible causes include compromised DNS infrastructure, malicious local configuration, or weaknesses in resolver security.

### Real-world example
The 2018 MyEtherWallet incident was publicly reported as involving BGP/DNS-related redirection that sent users toward a fraudulent destination, where some users were exposed to a phishing-style theft of cryptocurrency. It illustrates why DNS and routing integrity matter, although DNS poisoning and BGP hijacking are distinct techniques.

### Impact
- Users can be redirected to phishing pages or malicious servers.
- Services may become unavailable if records are altered incorrectly.
- Email delivery and trust in domain identity may be affected.
- Users may disclose credentials or approve fraudulent transactions.

### Mitigation strategies
1. **Secure DNS administration:** protect registrar and DNS-provider accounts with MFA, least privilege, strong recovery procedures, and change alerts.
2. **Use DNSSEC where supported:** DNSSEC validation helps resolvers verify the authenticity and integrity of signed DNS data; it does not encrypt DNS queries.
3. **Monitor and verify changes:** maintain known-good DNS records, alert on unexpected changes, and use trusted resolvers and secure endpoint configuration.

## 6. Comparison Table

| Threat | Typical attack vector | Who is at risk? | Difficulty to execute | Ease of mitigation |
|---|---|---|---|---|
| DoS/DDoS | Resource exhaustion; botnet or reflected traffic | Public services, providers, organisations | Medium to high at impactful scale; varies by method | Medium; large attacks often need upstream support |
| MITM | Untrusted network, rogue access point, compromised intermediary | Users and services with weak transport/session security | Medium; depends on access and protections | Medium; TLS and secure session design reduce risk |
| IP spoofing | Forged source address in IP packets | Internet-facing services and networks relying on IP trust | Low for packet forging; impact depends on network conditions | Medium; filtering and stronger authentication help |
| DNS poisoning/spoofing | Resolver, DNS account, endpoint, or routing compromise | Domain owners and users resolving affected names | Medium to high; depends on the weakness exploited | Medium; layered DNS and account protections are needed |

Difficulty and mitigation ratings are qualitative and depend on the environment, attacker capability, and existing controls.

## 7. Conclusion: Three takeaways for network administrators

1. **Use defence in depth:** combine filtering, secure DNS, encryption, strong authentication, patching, and least privilege rather than relying on one control.
2. **Monitor and prepare:** collect useful logs, alert on unusual network activity, maintain an incident-response plan, and practise recovery.
3. **Review trust assumptions:** do not trust a source IP, DNS answer, Wi-Fi network, or user-supplied message without appropriate verification.

## 8. References

1. CISA, *Understanding and Responding to Distributed Denial-of-Service Attacks*: https://www.cisa.gov/news-events/news/understanding-and-responding-distributed-denial-service-attacks
2. NIST, *Guide to IPsec VPNs (SP 800-77 Rev. 1)*: https://csrc.nist.gov/pubs/sp/800/77/r1/final
3. ICANN, *DNSSEC*: https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en
4. US-CERT/CISA resources: https://www.cisa.gov/resources-tools
5. Krebs on Security, reporting on the 2016 Dyn/Mirai DDoS incident: https://krebsonsecurity.com/
6. US-CERT/CISA, *Securing Network Infrastructure Devices*: https://www.cisa.gov/resources-tools

*Submission note: Review the references and add access dates if required by your institute. This report is educational and describes defensive controls.*
