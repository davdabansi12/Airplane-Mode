from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):
    def before_insert(self):
        if not self.route:
            self.route = f"{self.airplane.lower().replace(' ', '-')}-{self.date_of_departure}"

    def on_submit(self):
        self.status = "Completed"