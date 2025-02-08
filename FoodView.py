##### food_view.py #####
import tkinter as tk
from tkinter import messagebox
from FoodController import FoodController
from FoodModel import FoodDatabase

class FoodApp:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Food Expiry Checker")
        
        tk.Label(root, text="Enter Food ID:").pack()
        self.food_id_entry = tk.Entry(root)
        self.food_id_entry.pack()
        
        tk.Button(root, text="Check", command=self.check_food).pack()
        tk.Button(root, text="Show Summary", command=self.show_summary).pack()
        
    def check_food(self):
        food_id = self.food_id_entry.get()
        if not self.controller.validate_food_id(food_id):
            messagebox.showerror("Error", "Invalid Food ID! Must be 6 digits and not start with 0.")
            return
        
        food = self.controller.model.get_food_by_id(food_id)
        if not food:
            messagebox.showerror("Error", "Food ID not found!")
            return
        
        expired = self.controller.check_expiry(food)
        status = "Expired" if expired else "Still Good"
        messagebox.showinfo("Food Check", f"Food Type: {food['type']}\nExpiry Date: {food['exp_date']}\nStatus: {status}")
        
    def show_summary(self):
        summary, expired, valid = self.controller.get_summary()
        messagebox.showinfo("Summary", f"Checked Items:\n{summary}\nExpired: {expired}\nStill Good: {valid}")
