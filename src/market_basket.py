import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


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
print("=== APPLYING APRIORI ===")

frequent_itemsets = apriori(
    basket,
    min_support=0.03,   # you can tune this
    use_colnames=True
)

print("Frequent itemsets shape:", frequent_itemsets.shape)
print(frequent_itemsets.head())
print("=== GENERATING ASSOCIATION RULES ===")

rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1
)

# Sort by strongest relationships
rules = rules.sort_values(by="lift", ascending=False)

print("Rules shape:", rules.shape)
print(rules.head())
# Save rules to Excel
output_path = os.path.join(BASE_DIR, "output", "association_rules.xlsx")
rules.to_excel(output_path, index=False)

print("Association rules saved to:", output_path)
import matplotlib.pyplot as plt
# Load generated rules
rules_df = pd.read_excel(output_path)

print("Rules loaded for visualization:", rules_df.shape)
# Select top 10 rules by lift
top_rules = rules_df.head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_rules['antecedents'].astype(str),
    top_rules['lift']
)

plt.xlabel("Lift")
plt.ylabel("Itemsets (Antecedents)")
plt.title("Top 10 Association Rules by Lift")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()
