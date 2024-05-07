# Copyright (c) 2024, Abhishek Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirportShop(Document):
	def validate(self):
		self.area_in_square_feet = self.length*self.width
