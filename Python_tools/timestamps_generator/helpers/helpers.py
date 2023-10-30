import arrow


class Helpers:
    def __init__(self):
        self.current_timestamp = arrow.utcnow()
        self.times_list = []
    
    def generate_timestamps(self, start_day: str, units: str) -> list:
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
    