# Copyright (c) 2025, bansi davda and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShop(Document):
	def before_insert(self):
		# Set default rent amount from Settings if not provided
		if not self.rent_amount:
			settings = frappe.get_single("Settings")
			self.rent_amount = settings.default_rent_amount

	def validate(self):
		# Ensure contract dates are logically correct
		if self.contract_start_date and self.contract_end_date:
			if self.contract_start_date >= self.contract_end_date:
				frappe.throw("Contract start date should be less than contract end date")
				





import frappe

def get_context(context):
    context.shops = frappe.get_all(
        "Airport Shop",
        fields=[
            "name",
            "shop_name",
            "shop_number",
            "area_sqft",
            "is_occupied",
            "status",
            "tenant",
            "shop_type"
        ]
        # ✅ Don't add any filters unless required
    )
    return context
