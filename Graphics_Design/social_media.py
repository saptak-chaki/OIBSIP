import time

# ANSI Escape Codes for Terminal Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def display_colored_social_media_design():
    print(f"{CYAN}{BOLD}============================================================")
    print("          🎨 SOCIAL MEDIA DESIGN DASHBOARD (NEXUSFIT)       ")
    print(f"============================================================{RESET}\n")
    
    time.sleep(0.5)
    print(f"{YELLOW}{BOLD}[1] SPECIFICATIONS:{RESET}")
    print(f"  {GREEN}• Format{RESET}      : Instagram / Facebook Post")
    print(f"  {GREEN}• Dimensions{RESET}  : 1080 x 1350 px (Portrait)")
    print(f"  {GREEN}• Typography{RESET}  : Montserrat & Inter\n")
    
    time.sleep(0.5)
    print(f"{YELLOW}{BOLD}[2] BRAND COLOR PALETTE:{RESET}")
    print(f"  {MAGENTA}■ Dark Slate Background{RESET} : #0B090A")
    print(f"  {MAGENTA}■ Neon Teal Accent{RESET}      : #00F5D4")
    print(f"  {MAGENTA}■ Pure White Text{RESET}       : #FFFFFF\n")
    
    time.sleep(0.5)
    print(f"{YELLOW}{BOLD}[3] READY-TO-USE CAPTION:{RESET}")
    print(f"  {CYAN}\"Take your fitness and productivity to the next level with NexusFit! 🚀\" {RESET}\n")
    
    print(f"{CYAN}{BOLD}============================================================")
    print(f"{GREEN}{BOLD} ✅ Status: Terminal design module executed successfully! {RESET}")
    print(f"{CYAN}{BOLD}============================================================{RESET}")

if __name__ == "__main__":
    display_colored_social_media_colored = display_colored_social_media_design()