import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os

# Menu Dictionary (Item: Price)
MENU = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Sandwich": 100,
    "Cold Drink": 60,
    "Coffee": 90
}

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#fff4e6")

        # Constants
        self.GST_RATE = 0.05  # 5%
        self.DISCOUNT_RATE = 0.10  # 10%

        # App Icon
        if os.path.exists("icon.png"):
            self.root.iconphoto(False, tk.PhotoImage(file="icon.png"))

        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#fff4e6')
        style.configure('TLabelframe', background='#fff4e6', font=('Arial', 12, 'bold'))
        style.configure('TLabelframe.Label', background='#fff4e6', font=('Arial', 12, 'bold'))
        style.configure('TLabel', background='#fff4e6', font=('Arial', 11))
        style.configure('TButton', font=('Arial', 11, 'bold'), padding=6)

        self.total = 0.0

        # Frames
        self.top_frame = ttk.LabelFrame(self.root, text="Menu", padding=10)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        self.middle_frame = ttk.LabelFrame(self.root, text="Cart", padding=10)
        self.middle_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.bottom_frame = ttk.LabelFrame(self.root, text="Billing Info", padding=10)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        # Menu Section
        ttk.Label(self.top_frame, text="Select Item:").grid(row=0, column=0, padx=5, pady=5)
        self.item_var = tk.StringVar()
        self.item_combo = ttk.Combobox(self.top_frame, textvariable=self.item_var, values=list(MENU.keys()), state="readonly")
        self.item_combo.grid(row=0, column=1, padx=5, pady=5)
        self.item_combo.set("Pizza")

        ttk.Label(self.top_frame, text="Qty:").grid(row=0, column=2, padx=5, pady=5)
        self.qty_var = tk.StringVar()
        self.qty_combo = ttk.Combobox(self.top_frame, textvariable=self.qty_var, values=[str(i) for i in range(1, 11)], state="readonly")
        self.qty_combo.grid(row=0, column=3, padx=5, pady=5)
        self.qty_combo.set("1")

        self.add_button = ttk.Button(self.top_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=0, column=4, padx=10, pady=5)

        # Cart Display
        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True)

        self.cart_text = tk.Text(cart_frame, height=15, bg="#fffce7", font=("Arial", 11), wrap="word")
        self.cart_text.pack(side="left", fill="both", expand=True)

        cart_scroll = ttk.Scrollbar(cart_frame, command=self.cart_text.yview)
        cart_scroll.pack(side="right", fill="y")
        self.cart_text.config(yscrollcommand=cart_scroll.set)

        # Billing Info Labels
        self.total_label = ttk.Label(self.bottom_frame, text="Total: ₹0.00")
        self.total_label.pack(side="left", padx=20)

        self.checkout_button = ttk.Button(self.bottom_frame, text="Checkout", command=self.checkout)
        self.checkout_button.pack(side="right", padx=20)

        # Status Bar
        self.status_bar = tk.Label(
            self.root,
            text="Welcome to Restaurant Billing Software",
            bd=1,
            relief=tk.SUNKEN,
            anchor="w",
            bg="#e6b800",
            fg="white",
            font=("Arial", 10, "italic")
        )
        self.status_bar.pack(side="bottom", fill="x")

        # Clock
        self.clock_label = ttk.Label(self.bottom_frame)
        self.clock_label.pack(side="right")
        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"Time: {now}")
        self.root.after(1000, self.update_clock)

    def add_to_cart(self):
        item = self.item_var.get()
        qty_str = self.qty_var.get()

        if item and qty_str:
            qty = int(qty_str)
            price = MENU[item]
            subtotal = price * qty
            self.total += subtotal

            self.cart_text.insert(tk.END, f"{item} x {qty} = ₹{subtotal:.2f}\n")
            self.total_label.config(text=f"Total: ₹{self.total:.2f}")
        else:
            messagebox.showerror("Input Error", "Please select item and quantity.")

    def checkout(self):
        if self.total == 0:
            messagebox.showwarning("Empty Cart", "Your cart is empty.")
            return

        gst_amount = self.total * self.GST_RATE
        discount_amount = self.total * self.DISCOUNT_RATE
        final_amount = self.total + gst_amount - discount_amount

        # Display in cart text
        self.cart_text.insert(tk.END, "\n-----------------------------\n")
        self.cart_text.insert(tk.END, f"Subtotal: ₹{self.total:.2f}\n")
        self.cart_text.insert(tk.END, f"GST (5%): ₹{gst_amount:.2f}\n")
        self.cart_text.insert(tk.END, f"Discount (10%): -₹{discount_amount:.2f}\n")
        self.cart_text.insert(tk.END, f"Total Payable: ₹{final_amount:.2f}\n")
        self.cart_text.insert(tk.END, "-----------------------------\n")
        self.cart_text.insert(tk.END, "Thank you for your order!\n")

        # Update total label
        self.total_label.config(text=f"Total: ₹{final_amount:.2f}")

        # Info popup
        messagebox.showinfo("Bill Summary", f"""
Subtotal: ₹{self.total:.2f}
GST (5%): ₹{gst_amount:.2f}
Discount (10%): -₹{discount_amount:.2f}
------------------------
Total Payable: ₹{final_amount:.2f}
""")

        # Reset total after checkout
        self.total = 0.0


if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
