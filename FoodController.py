##### food_controller.py #####
import datetime
from dateutil.relativedelta import relativedelta

class FoodController:
    def __init__(self, model):
        self.model = model
    
    def validate_food_id(self, food_id):
        return food_id.isdigit() and len(food_id) == 6 and not food_id.startswith("0")
    
    def check_expiry(self, food):
        exp_day, exp_month, exp_year = map(int, food["exp_date"].split("/"))
        today = datetime.date.today()
        
        if food["type"] == "อาหารสด":
            expiry_date = datetime.date(exp_year, exp_month, exp_day)
            return today > expiry_date
        elif food["type"] == "อาหารดอง":
            expiry_date = datetime.date(exp_year, exp_month, 1) + relativedelta(months=1)
            return today >= expiry_date
        elif food["type"] == "อาหารกระป๋อง":
            expiry_date = datetime.date(exp_year, 12, 31) + relativedelta(months=9)
            return today > expiry_date
        return False
    
    def get_summary(self):
        expired_count = 0
        valid_count = 0
        summary = {"อาหารสด": 0, "อาหารดอง": 0, "อาหารกระป๋อง": 0}
        
        for food in self.model.food_data:
            summary[food["type"]] += 1
            if self.check_expiry(food):
                expired_count += 1
            else:
                valid_count += 1
        
        return summary, expired_count, valid_count