import frappe
import random
from frappe.model.document import Document
from frappe import _

# class AirplaneTicket(Document):
#     def validate(self):
#         self.remove_duplicate_addons()
#         self.calculate_total_amount()

#     def before_insert(self):
#         if not self.seat:
#             row = random.randint(1, 99)
#             column = random.choice(['A', 'B', 'C', 'D', 'E'])
#             self.seat = f"{row}{column}"

#     def calculate_total_amount(self):
#         total = self.flight_price or 0
#         for addon in self.add_ons:
#             total += addon.amount or 0
#         self.total_amount = total

#     def remove_duplicate_addons(self):
#         seen = set()
#         unique_addons = []
#         for addon in self.add_ons:
#             if addon.item not in seen:
#                 seen.add(addon.item)
#                 unique_addons.append(addon)
#         self.add_ons = unique_addons



class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_addons()
        self.calculate_total_amount()
        self.check_capacity()

    def before_insert(self):
        if not self.seat:
            row = random.randint(1, 99)
            column = random.choice(['A', 'B', 'C', 'D', 'E'])
            self.seat = f"{row}{column}"

    def calculate_total_amount(self):
        total = self.flight_price or 0
        for addon in self.add_ons:
            total += addon.amount or 0
        self.total_amount = total

    def remove_duplicate_addons(self):
        seen = set()
        unique_addons = []
        for addon in self.add_ons:
            if addon.item not in seen:
                seen.add(addon.item)
                unique_addons.append(addon)
        self.add_ons = unique_addons

    def check_capacity(self):
        if not self.flight:
            frappe.throw("Flight must be selected before saving the ticket.")

        # Get the Airplane Flight doc
        flight_doc = frappe.get_doc("Airplane Flight", self.flight)

        # Get the linked Airplane and its capacity
        airplane = frappe.get_doc("Airplane", flight_doc.airplane)
        capacity = airplane.capacity

        # Count existing tickets for this flight (excluding current doc)
        booked_tickets = frappe.db.count(
            "Airplane Ticket",
            filters={
                "flight": self.flight,
                "name": ["!=", self.name]  # exclude self
            }
        )

        if booked_tickets >= capacity:
            frappe.throw(
                f"Cannot book ticket. Airplane '{airplane.name}' has only {capacity} seats and they are fully booked."
            )



