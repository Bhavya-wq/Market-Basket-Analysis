import os
import pandas as pd

print("=== STEP 5 STARTED ===")

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "Data", "online_retail.xlsx")

# Load Excel file
df = pd.read_excel(data_path)

print("Original shape:", df.shape)

# Keep only required columns
df = df[['InvoiceNo', 'Description', 'Quantity']]

# Remove missing values
df.dropna(inplace=True)

# Remove cancelled invoices (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Keep only positive quantity
df = df[df['Quantity'] > 0]

print("Shape after cleaning:", df.shape)
print(df.head())

print("=== DATA CLEANING DONE ===")
# Reduce dataset size for performance
df = df.head(20000)
print("Shape after limiting:", df.shape)
print("=== CREATING BASKET MATRIX ===")

basket = (
    df.groupby(['InvoiceNo', 'Description'])['Quantity']
    .sum()
    .unstack()
    .fillna(0)
)

# Convert quantities to 0/1
basket = basket.map(lambda x: 1 if x > 0 else 0)


print("Basket shape:", basket.shape)
print(basket.head())
