from FoodModel import FoodDatabase
from FoodController import FoodController
from FoodView import FoodApp
import tkinter as tk

class FoodAppMain:
    def __init__(self):
        self.model = FoodDatabase()
        self.controller = FoodController(self.model)
        self.root = tk.Tk()
        self.app = FoodApp(self.root, self.controller)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app_main = FoodAppMain()
    app_main.run()
