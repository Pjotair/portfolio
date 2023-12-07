# WORK IN PROGRESS


import arrow
from os import path
from typing import Dict
from yaml import safe_load


class Helpers:
    def __init__(self):
        self.current_timestamp = arrow.utcnow()
        self.times_list = []
    
    @staticmethod
    def read_yml_file(file_name: str) -> Dict:
        with open(path.join(path.dirname(__file__), file_name)) as config_file:
            return safe_load(config_file)
    

    def generate_timestamps(self, start_day: str, units: str):
        start_date = arrow.get(start_day, "YYYY-MM-DD").replace(tzinfo="local").to("UTC")
        end_date = self.current_timestamp
        shift_unit = {"d": "days", "h": "hours", "min": "minutes"}.get(units)

        if shift_unit:
            shift_amount = 1 if units != "min" else 15
            while start_date < end_date:
                new_date = start_date.isoformat()
                self.times_list.append(new_date)
                start_date = start_date.shift(**{shift_unit: shift_amount})
        
        return self.times_list
    