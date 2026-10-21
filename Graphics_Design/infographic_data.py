import matplotlib.pyplot as plt

def generate_infographic_chart():
    # Data points for Renewable Energy Infographic
    sectors = ['Solar Energy', 'Wind Power', 'Hydropower', 'Bioenergy']
    growth_percentages = [45, 32, 18, 12]
    
    colors = ['#FFD700', '#64FFDA', '#4169E1', '#32CD32']
    
    plt.figure(figsize=(8, 5))
    bars = plt.barh(sectors, growth_percentages, color=colors)
    
    plt.title('Global Renewable Energy Growth Rate (%)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Growth Percentage (%)', fontsize=12)
    plt.ylabel('Energy Sector', fontsize=12)
    
    # Adding values on bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}%', 
                 va='center', ha='left', fontsize=10, fontweight='bold')
        
    plt.xlim(0, 55)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Generating Infographic Data Chart...")
    generate_infographic_chart()