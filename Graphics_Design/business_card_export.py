def create_vcard():
    card_content = """
    ==========================================
    NAME: Alex Rivers
    TITLE: Lead UI/UX Engineer & Co-Founder
    COMPANY: NexusFit
    ------------------------------------------
    PHONE: +1 (555) 234-5678
    EMAIL: alex.rivers@nexusfit.io
    WEBSITE: www.nexusfit.io
    SOCIALS: @nexusfit_official
    ==========================================
    """
    
    filename = "business_card_details.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(card_content.strip())
        
    print(f"✅ Business Card details successfully exported to '{filename}'!")

if __name__ == "__main__":
    create_vcard()