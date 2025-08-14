from utils.db_utils import init_db, insert_menu_from_csv
from ui.main_ui import BillingApp
import tkinter as tk

def main():
    init_db()
    insert_menu_from_csv()

    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
