import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print("==========================================")
    print("      Unemployment Analysis with Python    ")
    print("==========================================")
    
    try:
        # Get the exact folder where this python script is saved
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'Unemployment in India.csv')
        
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        
        print("\n📁 Dataset Head:")
        print(df.head())
        
        print("\n📊 Summary Statistics:")
        print(df.describe())
        
        # Plotting
        plt.figure(figsize=(8, 5))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title("Missing Values Check")
        plt.savefig(os.path.join(script_dir, 'output_plot.png'))
        plt.close()
        
        print("\n✅ Analysis completed and plot saved as 'output_plot.png'!")
        print("==========================================")
        
    except FileNotFoundError:
        print("❌ Error: 'Unemployment in India.csv' not found in the folder!")
        print("Please make sure the CSV file is in the exact same folder as this script.")

if __name__ == "__main__":
    main()