import frappe
import random

def execute():
   
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]}, pluck="name")

    for ticket_name in tickets:
        ticket = frappe.get_doc("Airplane Ticket", ticket_name)

        # Generate seat value (same logic as before_insert)
        row = random.randint(1, 99)
        column = random.choice(['A', 'B', 'C', 'D', 'E'])
        ticket.seat = f"{row}{column}"

        ticket.save(ignore_permissions=True, ignore_version=True)
    
    frappe.db.commit()  
