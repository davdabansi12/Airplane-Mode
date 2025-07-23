import frappe
from frappe.utils import today, get_first_day, get_last_day, getdate
from frappe import _

# -------------------------------
# 1. Monthly Rent Generation + Email Reminder
# -------------------------------

# def generate_rent_and_send_reminders():
#     settings = frappe.get_single("Airport Shop Settings")
#     current_month_start = get_first_day(today())
#     current_month_end = get_last_day(today())

#     contracts = frappe.get_all(
#         "Shop Contract",
#         filters={"active": 1},
#         fields=["name", "shop", "tenant", "rent_amount"]
#     )

#     for contract in contracts:
#         shop = contract.shop
#         tenant = contract.tenant
#         rent_amount = contract.rent_amount

#         # Check if payment already exists for this month
#         existing = frappe.get_all("Rent Payment", filters={
#             "shop": shop,
#             "tenant": tenant,
#             "paid_on": ["between", [current_month_start, current_month_end]]
#         })

#         if not existing:
#             # Create Rent Payment
#             frappe.get_doc({
#                 "doctype": "Rent Payment",
#                 "shop": shop,
#                 "tenant": tenant,
#                 "rent_amount": rent_amount,
#                 "paid_on": today(),
#                 "remarks": "Auto-generated monthly rent"
#             }).insert()

#             # Send reminder email if enabled
#             if settings.enable_rent_reminder:
#                 tenant_doc = frappe.get_doc("Tenant", tenant)
#                 frappe.sendmail(
#                     recipients=[tenant_doc.email],
#                     subject="Monthly Rent Reminder",
#                     message=frappe.render_template("""
#                         Dear {{ name }},

#                         Please note that your rent for this month (₹{{ rent }}) has been recorded, but is still due.

#                         Kindly ensure payment is completed soon.

#                         Thank you!
#                     """, {
#                         "name": tenant_doc.tenant_name,
#                         "rent": rent_amount
#                     })
#                 )

#     frappe.db.commit()

# -------------------------------
# 2. REST API - Get all Airport Shops
# -------------------------------

@frappe.whitelist(allow_guest=True)
def get_airport_shops():
    shops = frappe.get_all("Airport Shop", fields=["*"])
    return shops




# {
#     "message": [
#         {
#             "name": "S106",
#             "creation": "2025-07-21 12:11:25.488592",
#             "modified": "2025-07-22 10:39:34.685157",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 0,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S106",
#             "shop_name": "Book Haven",
#             "area_sq_ft": 0.0,
#             "airport": "Singapore Changi Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "Bookie Books",
#             "is_occupied": 0,
#             "area_sqft": 200.0,
#             "status": "Available",
#             "shop_type": "Stall",
#             "contract_start_date": "2025-07-22",
#             "contract_end_date": "2037-04-29"
#         },
#         {
#             "name": "S102",
#             "creation": "2025-07-21 12:07:33.168944",
#             "modified": "2025-07-22 10:39:20.886688",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 0,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S102",
#             "shop_name": "Brew Café",
#             "area_sq_ft": 0.0,
#             "airport": "Dubai International Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "Coffee Craze",
#             "is_occupied": 0,
#             "area_sqft": 180.0,
#             "status": "Available",
#             "shop_type": "Stall",
#             "contract_start_date": "1939-11-29",
#             "contract_end_date": "2037-11-17"
#         },
#         {
#             "name": "S101",
#             "creation": "2025-07-21 12:06:55.964377",
#             "modified": "2025-07-22 10:38:47.927098",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 0,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S101",
#             "shop_name": "ABC Retail\t",
#             "area_sq_ft": 0.0,
#             "airport": "Chhatrapati Shivaji Maharaj Int'l Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "ABC Retailers",
#             "is_occupied": 0,
#             "area_sqft": 250.0,
#             "status": "Available",
#             "shop_type": "Stall",
#             "contract_start_date": "2025-07-20",
#             "contract_end_date": "2031-01-02"
#         },
#         {
#             "name": "S107",
#             "creation": "2025-07-21 12:11:55.425746",
#             "modified": "2025-07-21 12:11:55.425746",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 0,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S107",
#             "shop_name": "Snacky’s",
#             "area_sq_ft": 0.0,
#             "airport": "Tokyo Haneda Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "Snack Stop",
#             "is_occupied": 0,
#             "area_sqft": 150.0,
#             "status": "Available",
#             "shop_type": null,
#             "contract_start_date": null,
#             "contract_end_date": null
#         },
#         {
#             "name": "S105",
#             "creation": "2025-07-21 12:10:33.992175",
#             "modified": "2025-07-21 12:10:33.992175",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 1,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S105",
#             "shop_name": "Metro Mart\t",
#             "area_sq_ft": 0.0,
#             "airport": "London Heathrow Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "Metro Mart",
#             "is_occupied": 0,
#             "area_sqft": 260.0,
#             "status": "Available",
#             "shop_type": null,
#             "contract_start_date": null,
#             "contract_end_date": null
#         },
#         {
#             "name": "S104",
#             "creation": "2025-07-21 12:09:58.393200",
#             "modified": "2025-07-21 12:09:58.393200",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 0,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S104",
#             "shop_name": "Fit Station",
#             "area_sq_ft": 0.0,
#             "airport": "John F. Kennedy International Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "FlyFit Gym",
#             "is_occupied": 0,
#             "area_sqft": 300.0,
#             "status": "Available",
#             "shop_type": null,
#             "contract_start_date": null,
#             "contract_end_date": null
#         },
#         {
#             "name": "S103",
#             "creation": "2025-07-21 12:09:13.824781",
#             "modified": "2025-07-21 12:09:13.824781",
#             "modified_by": "Administrator",
#             "owner": "Administrator",
#             "docstatus": 0,
#             "idx": 0,
#             "_user_tags": null,
#             "_comments": null,
#             "_assign": null,
#             "_liked_by": null,
#             "shop_number": "S103",
#             "shop_name": "Sky Gifts",
#             "area_sq_ft": 0.0,
#             "airport": "Indira Gandhi International Airport",
#             "rent_amount": 0.0,
#             "contract_expiry": null,
#             "tenant": "Sky Souvenirs",
#             "is_occupied": 0,
#             "area_sqft": 220.0,
#             "status": "Available",
#             "shop_type": null,
#             "contract_start_date": null,
#             "contract_end_date": null
#         }
#     ]
# }

# -------------------------------
# 3. Public API - Shop Lead Creation
# -------------------------------

@frappe.whitelist(allow_guest=True)
def create_shop_lead(shop, full_name, email, message=None):
    doc = frappe.new_doc("Shop Lead")
    doc.shop = shop
    doc.full_name = full_name
    doc.email = email
    doc.message = message or ""
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "message": _("Your interest has been recorded.")
    }


# {
#     "message": {
#         "status": "success",
#         "message": "Your interest has been recorded."
#     }
# }