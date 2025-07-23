# Copyright (c) 2025, bansi davda and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShop(Document):
	def before_insert(self):
		# Set rent from global settings if not provided
		if not self.rent_amount:
			settings = frappe.get_single("Settings")
			self.rent_amount = settings.default_rent_amount

	def validate(self):
		# Safely compare contract dates
		if self.contract_start_date and self.contract_end_date:
			if self.contract_start_date >= self.contract_end_date:
				frappe.throw("Contract start date should be less than contract end date")
