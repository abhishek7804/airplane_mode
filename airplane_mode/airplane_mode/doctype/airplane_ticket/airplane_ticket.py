# Copyright (c) 2024, Abhishek Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import random
import string


class AirplaneTicket(Document):
	def validate(self):
		tickets_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})
		airplane=frappe.db.get_value("Airplane Flight",self.flight,"airplane")
		capcity=0
		if airplane:
			capcity=frappe.db.get_value("Airplane",airplane,"capacity")
		self.exceed_capcity_validation(tickets_count,capcity)
		if self.is_new() and not self.seat:
			self.seat= generate_seat(capcity)
		# Get unique items from add-ons
		unique_items = set()

		# Remove duplicates and calculate total amount
		total_amount = self.flight_price if self.flight_price else 0
		new_add_ons = []
		for addon in self.add_ons:
			if addon.item not in unique_items:
				unique_items.add(addon.item)
				new_add_ons.append(addon)
				total_amount += addon.amount

		# Update child table add_ons with unique items
		self.set("add_ons", [])
		for addon in new_add_ons:
			self.append("add_ons", {"item": addon.item, "amount": addon.amount})

		# Set total amount
		self.total_amount = total_amount

	def exceed_capcity_validation(self,tickets_count,capacity):
		if tickets_count >= capacity:
			frappe.throw(_("Cannot create ticket. All seats for this flight are occupied."))
	
	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw(_("Status Must Be Boarded in order to submit the ticket."))
	def before_insert(self):
		random_integer = random.randint(10, 99)
		random_alphabet = random.choice(string.ascii_uppercase[:5])  # Random capital alphabet from A to E
		seat_string = f"{random_integer}{random_alphabet}"
        
        # Set the seat field
		self.seat = seat_string

def generate_seat(capcity):
		random_integer = random.randint(1, capcity)
		random_alphabet = random.choice(['A', 'B', 'C', 'D', 'E'])
		return str(random_integer) + random_alphabet
