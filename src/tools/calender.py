from datetime import datetime, timedelta

class CalendarTool:
    def check_availability(self, date_str: str):
        # Mock logic: In a real app, use google-api-python-client
        return f"The receptionist checked the calendar for {date_str}. 2:00 PM is available."

    def book_appointment(self, date_str: str, name: str):
        # Mock logic
        return f"Successfully booked an appointment for {name} on {date_str}."