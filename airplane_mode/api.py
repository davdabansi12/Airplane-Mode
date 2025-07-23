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
