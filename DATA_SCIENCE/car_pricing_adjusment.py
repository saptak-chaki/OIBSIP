import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    print("==========================================")
    print("      Car Price Prediction Model          ")
    print("==========================================")
    
    try:
        # Get the exact directory of this script to avoid path/folder errors
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'car_prediction_data.csv')
        
        df = pd.read_csv(file_path)
        
        print("\n📁 Car Dataset Head:")
        print(df.head())
        
        # Preprocessing
        df_encoded = pd.get_dummies(df, drop_first=True)
        
        if 'Selling_Price' in df_encoded.columns:
            X = df_encoded.drop('Selling_Price', axis=1)
            y = df_encoded['Selling_Price']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            
            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            
            print(f"\n📊 Model R2 Score    : {r2:.4f}")
            print(f"📉 Mean Squared Error: {mse:.4f}")
            print("==========================================")
        else:
            print("❌ 'Selling_Price' column not found in the dataset!")
            
    except FileNotFoundError:
        print("❌ Error: 'car data.csv' not found in the folder!")
        print("Please make sure 'car data.csv' is placed in the exact same folder as this script.")

if __name__ == "__main__":
    main()