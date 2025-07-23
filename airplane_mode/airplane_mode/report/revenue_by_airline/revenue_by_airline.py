import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 250
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 180
        }
    ]

    all_airlines = frappe.get_all("Airline", fields=["name"])
    airline_names = [a["name"] for a in all_airlines]

    revenue_map = {airline: 0 for airline in airline_names}

    airline_tickets = frappe.get_all(
        "Airplane Ticket",
        fields=["name", "total_amount", "flight"]
    )

    for ticket in airline_tickets:
        total_amount = ticket.get("total_amount") or 0

        airplane = frappe.get_value("Airplane Flight", ticket["flight"], "airplane")
        if not airplane:
            continue

        airline = frappe.get_value("Airplane", airplane, "airline")
        if not airline:
            continue

        if airline in revenue_map:
            revenue_map[airline] += total_amount
        else:
            revenue_map[airline] = total_amount

    data = []
    total_revenue = 0

    for airline in airline_names:
        revenue = revenue_map.get(airline, 0)
        total_revenue += revenue
        data.append({
            "airline": airline,
            "revenue": revenue
        })

    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [
                {"name": "Revenue", "values": [d["revenue"] for d in data]}
            ]
        },
        "type": "donut"
    }

    summary = [
        {"label": "Total Revenue", "value": total_revenue, "indicator": "Green"}
    ]

    return columns, data, None, chart, summary