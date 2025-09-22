# data_generator.py
import pandas as pd
import numpy as np
import os

# Create a DataFrame with 1000 samples
data = pd.DataFrame()
data['rainfall_mm'] = np.random.uniform(300, 800, 1000)
data['electricity_subsidy_%'] = np.random.uniform(50, 100, 1000)
data['msp_price'] = np.random.uniform(2000, 3000, 1000)

# Create logical relationships for target variables
data['yield_tonnes_ha'] = (data['rainfall_mm'] * 0.01) + np.random.normal(0, 0.5, 1000)
data['water_table_drop_m'] = (100 - data['electricity_subsidy_%']) * -0.05 + (data['rainfall_mm'] * -0.01) + np.random.normal(5, 1, 1000)

# Ensure the 'data' directory exists before saving the file
os.makedirs('data', exist_ok=True)

# Save to a CSV file inside the 'data' folder.
data.to_csv('data/mock_data.csv', index=False)
print("✅ Mock data generated successfully!")
