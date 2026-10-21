def show_brand_palette():
    brand_name = "NexusFit"
    palette = {
        "Primary Dark": "#0B090A",
        "Accent Neon Teal": "#00F5D4",
        "Secondary Slate": "#8892B0",
        "Background Light": "#F0F4F8"
    }
    
    print("==========================================")
    print(f"      Brand Color Palette: {brand_name}   ")
    print("==========================================")
    for color_name, hex_code in palette.items():
        print(f"  [+] {color_name:<20} : {hex_code}")
    print("==========================================")
    print("Tip: Use these exact Hex codes in Canva/Figma for consistency.")

if __name__ == "__main__":
    show_brand_palette()