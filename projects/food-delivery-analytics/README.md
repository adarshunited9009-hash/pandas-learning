# Food Delivery Analytics

A Pandas practice project analysing a sample food delivery dataset. The project looks at order values, cities, cuisines, restaurant performance, cancellations, payment methods, discounts, customer ratings and delivery times.

## Project structure

```
food-delivery-analytics/
├── data/
│   └── food_orders.csv
├── notebooks/
│   └── analysis.py
├── README.md
└── requirements.txt
```

## Run the project

1. Install Python.
2. Install the required library:

   ```bash
   pip install -r requirements.txt
   ```

3. Keep `food_orders.csv` inside the `data` folder.
4. Run the script from the project root folder:

   ```bash
   python notebooks/analysis.py
   ```

The script uses the relative path `data/food_orders.csv`, so run it from the main project folder.

## Questions explored

- Which cities and cuisines receive the most orders?
- Which restaurants generate the most food sales?
- Which restaurants receive the most orders?
- How do delivery times vary by restaurant?
- How many orders are cancelled, and how does the cancellation rate vary by city?
- Which payment methods are most commonly used?
- How do average order values compare between discounted and non-discounted orders?
- Which restaurants have the highest and lowest average ratings?
- What missing values and duplicate rows are present?

## Findings from this dataset

- The dataset contains 1,000 orders.
- Total food item sales are ₹427,690.36.
- Average food item order value is about ₹427.69.
- There are 916 delivered orders and 84 cancelled orders (8.4%).
- UPI is the most commonly used payment method.
- Average delivery time for the dataset was reported as 32.94 minutes.
- Goodluck Cafe had the highest average restaurant rating, while Nafees had the lowest.
- Average order value was ₹425.34 for discounted orders and ₹431.64 for orders without a discount.
- There are 84 missing delivery times, all associated with cancelled orders.
- There are 256 missing ratings and no duplicate rows.

These are descriptive findings from this dataset. They do not, by themselves, prove that discounts cause changes in customer spending.

## Tools used

- Python
- Pandas
