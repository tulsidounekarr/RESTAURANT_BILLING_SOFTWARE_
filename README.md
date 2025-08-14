# 🍴 Restaurant Billing Software

A Python-based billing system for restaurants that supports Dine-In and Takeaway orders.
It handles menu management, order entry, tax/discounts, bill generation, and reporting with database support.

✨ Features
📋 Menu Management

Upload & manage menu items (Name, Category, Price, GST).

# 🛒 Order Entry

Choose Dine-In or Takeaway.

Add/remove items dynamically.

Live running total displayed.

💰 Order Management & Calculation

Auto-calculate Subtotal + GST (5%).

Apply optional discounts.

Accept Cash / Card / UPI payments.

# 🧾 Bill Generation

Generate itemized bills with tax & discount breakdown.

Export bills to PDF (fpdf2), CSV, or JSON.

# 🗄 Data Storage

Save transactions in SQLite3 Database.

Stores items, GST, discounts, payment method, and timestamps.

# 📊 Reports

Daily / Weekly / Monthly sales summary.

Track most sold items.

Export reports as CSV.

# 📦 Requirements

Python 3.x

Required Libraries:

pip install streamlit pandas fpdf2

# ⚡ How to Run
1️⃣ Initialize Database
python app.py init
python app.py load_menu

2️⃣ (Optional) Seed with Test Orders
python app.py seed

3️⃣ Run the Application

👉 For Streamlit (Web UI):

streamlit run ui/main_ui.py


👉 For Tkinter (Desktop UI):

python ui/main_ui.py

# 📂 Project Structure
resturant_billing/
│── app.py                  # CLI helper (DB setup, menu load, test seed)
│
├── db/
│   └── restaurant.db        # SQLite database
│
├── data/
│   ├── menu.csv             # Menu file
│   ├── sample_bills.json    # Example bills
│   └── sales_report.csv     # Example sales report
│
├── ui/
│   └── main_ui.py           # Tkinter or Streamlit UI
│
├── utils/
│   ├── calculator.py        # Billing & tax calculations
│   └── db_utils.py          # Database helpers
│
└── README.md                # Documentation

# 🧪 Test Cases

Includes 5 sample test bills:
✔ Multiple items (combo order)
✔ GST only
✔ GST + Discount applied
✔ UPI vs Cash Payment
✔ Edge case: No item selected

# 📸 Sample Bill Export

Order ID: 101
Mode: Dine-In

Items:

Paneer Butter Masala × 2 → ₹480

Butter Naan × 4 → ₹200

Subtotal: ₹680
GST (5%): ₹34
Discount: ₹0
Total: ₹714
Payment: UPI

# 👨‍💻 Author

- GitHub: [@tulsidounekarr](https://github.com/tulsidounekarr)
  
# 📄 License

This project is open-source and available under the [MIT License](LICENSE).
