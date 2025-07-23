# Copyright (c) 2025, bansi davda and contributors
# For license information, please see license.txt

# flight_passenger.py

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
    def before_save(self):
        self.full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()

