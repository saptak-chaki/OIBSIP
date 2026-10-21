# Research Report: Social Engineering Attacks

**Track:** Cyber Security  
**Task:** 5 — Research Report: Social Engineering Attacks  
**Author:** [Your Name]  
**Date:** [Submission Date]

## 1. Introduction

Social engineering is the use of deception, impersonation, urgency, or psychological pressure to persuade people to reveal information, transfer money, grant access, or perform an unsafe action. Rather than relying only on a technical vulnerability, the attacker targets human judgement and normal workplace processes. These attacks can bypass otherwise strong technology if a user is tricked into approving a login, opening a malicious attachment, or changing payment details. Effective prevention combines user awareness, clear verification procedures, multi-factor authentication, technical filtering, and a culture in which people can report suspicious requests without fear.

## 2. Phishing

### Definition and how it works
Phishing is a deceptive message designed to make a recipient click a link, open an attachment, reveal credentials, or approve an action. Messages may imitate a bank, employer, delivery company, cloud service, or colleague. Attackers commonly use urgency, fear, curiosity, or an apparent reward.

### Common types
- **Spear phishing:** tailored to a specific person or organisation.
- **Whaling:** targets senior executives or other high-value decision-makers.
- **Vishing:** uses voice calls or voicemail.
- **Smishing:** uses SMS or messaging applications.

### Documented case study
The 2016 DNC email compromise was widely reported as involving spear-phishing emails, including credential-harvesting activity. It demonstrates how a convincing message and a compromised account can create consequences beyond the initial recipient. Public reporting should be consulted for precise details and attribution.

### Prevention recommendations
1. **Verify before acting:** inspect sender addresses and unexpected links; confirm sensitive requests through a known, separate communication channel.
2. **Use phishing-resistant MFA where possible:** security keys or passkeys offer stronger protection against credential theft than passwords alone.
3. **Filter and protect endpoints:** deploy email filtering, safe attachment/link analysis, patching, and endpoint protection.
4. **Report quickly:** provide a clear report-phishing process and rapidly revoke sessions/reset credentials when compromise is suspected.

## 3. Pretexting

### Definition and method
Pretexting is a form of deception in which an attacker invents a believable story or role to obtain information or persuade a target to perform an action. The attacker may pretend to be IT support, a supplier, a manager, a bank representative, or an auditor. They may collect background details first so the story sounds credible.

### Case study
Business email compromise (BEC) incidents often use pretexting: an attacker impersonates an executive or supplier and asks an employee to change bank details or make an urgent payment. The FBI's Internet Crime Complaint Center has repeatedly warned about BEC-related financial losses. The defining weakness is often a failure to verify the request independently, not a sophisticated software exploit.

### Prevention measures
1. **Out-of-band verification:** call a known number or use a previously established channel before changing payment details or sharing sensitive data.
2. **Dual approval for high-risk actions:** require two authorised people to approve large transfers, vendor changes, or privileged-access requests.
3. **Minimise information exposure:** avoid publishing internal structures and personal details unnecessarily; verify identities before disclosing internal information.

## 4. Baiting

### Definition and examples
Baiting tempts a target with something desirable or useful to trigger an unsafe action. Physical baiting may involve a USB drive labelled “salary details” or “confidential”; digital baiting may involve pirated software, fake downloads, or files promising free content. The bait may lead to malware installation or credential theft.

### Case study
The Stuxnet incident, discovered in 2010, is widely discussed in security literature as malware that spread in part through removable media and targeted industrial control environments. It is not a simple generic “baiting campaign,” but it illustrates why removable media and untrusted files can be risky in sensitive environments.

### Prevention measures
1. **Do not plug in unknown media:** hand found USB devices to IT/security staff; use approved removable-media procedures.
2. **Use application control and endpoint protection:** block unauthorised executables, scan removable media, and keep systems patched.
3. **Download only from trusted sources:** avoid pirated or unofficial installers and verify software publishers/signatures when available.

## 5. Quid Pro Quo (Bonus)

Quid pro quo means offering a benefit or service in exchange for information or access. For example, someone pretending to be technical support might offer to “fix” a computer problem in return for a password or remote access. Prevention includes verifying support staff through official channels, never sharing passwords, using approved remote-support tools, and reporting unexpected offers that require access or confidential information.

## 6. Comparison Table

| Attack type | Primary target | Psychological lever exploited | Best countermeasure |
|---|---|---|---|
| Phishing | Employees, customers, account holders | Urgency, fear, curiosity, trust | Verify links/requests, strong MFA, filtering, rapid reporting |
| Pretexting | Finance, HR, help desk, executives, suppliers | Authority, familiarity, pressure, plausible story | Independent identity verification and dual approval |
| Baiting | Staff or visitors with device/file access | Curiosity, greed, convenience | Removable-media controls and trusted software sources |
| Quid pro quo | Users seeking help or a promised benefit | Reciprocity and desire for assistance | Verify support identity; never disclose passwords |

## 7. Five-point employee security awareness checklist

1. **Recognise warning signs:** mismatched sender domains, unexpected attachments, unusual urgency, secrecy requests, and changes to payment instructions.
2. **Verify independently:** use known phone numbers or established internal channels for financial, credential, or access requests.
3. **Protect credentials:** never share passwords or MFA codes; use a password manager and approved MFA.
4. **Handle files and devices safely:** do not run unexpected attachments or connect unknown USB devices; use approved download sources.
5. **Report promptly:** report suspicious messages and mistakes immediately so the security team can contain the incident.

## 8. Organisational recommendations

Organisations should make reporting simple, run practical awareness exercises, provide role-specific training for finance and help-desk teams, enforce approval workflows for sensitive transactions, and review incidents to improve procedures. Training should focus on learning rather than blaming employees. Technical controls and good process design should support people rather than expecting them to detect every deception unaided.

## 9. References

1. CISA, *Avoiding Social Engineering and Phishing Attacks*: https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks
2. FBI Internet Crime Complaint Center (IC3), *Business Email Compromise*: https://www.ic3.gov/Media/Y2023/PSA230609
3. MITRE ATT&CK, *Phishing (T1566)*: https://attack.mitre.org/techniques/T1566/
4. NIST, *Security Awareness and Training*: https://csrc.nist.gov/projects/security-awareness-training
5. CISA, *Secure Our World*: https://www.cisa.gov/secure-our-world
6. CISA, *Removable Media*: https://www.cisa.gov/

*Submission note: Add access dates and consult the cited sources for current details. Case-study descriptions are summaries, not claims of exhaustive attribution.*
