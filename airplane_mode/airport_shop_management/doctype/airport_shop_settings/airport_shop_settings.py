# Copyright (c) 2024, Abhishek Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShopSettings(Document):
	def validate(self):
		if self.enable_rent_reminders:
			frappe.db.set_value("Scheduled Job Type","shop_contract_details.reminder_for_payment","stopped",0)
		else:
			frappe.db.set_value("Scheduled Job Type","shop_contract_details.reminder_for_payment","stopped",1)