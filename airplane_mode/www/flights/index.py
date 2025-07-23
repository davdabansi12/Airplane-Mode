import frappe

def get_context(context):
    context.flights = frappe.get_all(
        "Airplane Flight",
        fields=[
            'airplane', "date_of_departure", 'time_of_departure', "source_airport_code",
             "destination_airport_code", "duration", "route", "name",
        ],
		filters={"is_published": 1}    )
    return context




