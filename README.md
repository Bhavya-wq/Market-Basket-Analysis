# 🛒 Market Basket Analysis for E-Commerce

## 📌 Objective
To analyze real-world e-commerce transaction data and identify frequently purchased product combinations using association rule mining (Apriori algorithm).

## 📊 Dataset
- Online Retail Dataset (Excel format)
- Contains transactional data including InvoiceNo, Product Description, and Quantity

## 🛠️ Tools & Technologies
- Python
- Pandas
- Mlxtend (Apriori Algorithm)
- Matplotlib
- VS Code
- Git & GitHub

## 🔄 Methodology
1. Loaded and cleaned raw transactional data
2. Removed cancelled orders and invalid quantities
3. Converted transactions into a binary basket matrix
4. Applied Apriori algorithm to extract frequent itemsets
5. Generated association rules using support, confidence, and lift
6. Visualized top product associations by lift

## 📈 Results
- Identified strong product associations with high lift values
- Generated association rules saved as Excel for business analysis
- Visualized top 10 rules to highlight cross-selling opportunities

## 💡 Business Value
- Helps improve product recommendations
- Supports cross-selling and product bundling strategies
- Can increase average order value and customer satisfaction

## 📁 Project Structure
Market-Basket-Analysis/
│
├── Data/
│ └── online_retail.xlsx
├── src/
│ └── market_basket.py
├── output/
│ ├── association_rules.xlsx
│ └── top_10_rules_by_lift.png
├── README.md
└── requirements.txt
## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/market_basket.py

