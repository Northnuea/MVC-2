##### food_model.py #####
import json
import random

class FoodDatabase:
    FILE_PATH = "food_data.json"
    FOOD_TYPES = ["อาหารสด", "อาหารดอง", "อาหารกระป๋อง"]
    DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    def __init__(self):
        self.food_data = []
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                self.food_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.generate_sample_data()
    
    def save_data(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(self.food_data, file, ensure_ascii=False, indent=4)
    
    def generate_sample_data(self):
        self.food_data = []
        num_per_type = {"อาหารสด": 20, "อาหารดอง": 15, "อาหารกระป๋อง": 15}
        
        for food_type, count in num_per_type.items():
            for _ in range(count):
                food_id = str(random.randint(1, 9)) + str(random.randint(10000, 99999))
                exp_year = random.randint(2015, 2030)
                exp_month = random.randint(1, 12)
                exp_day = random.randint(1, self.DAYS_IN_MONTH[exp_month])
                self.food_data.append({
                    "food_id": food_id,
                    "type": food_type,
                    "exp_date": f"{exp_day}/{exp_month}/{exp_year}"
                })
        self.save_data()
    
    def get_food_by_id(self, food_id):
        return next((food for food in self.food_data if food["food_id"] == food_id), None)