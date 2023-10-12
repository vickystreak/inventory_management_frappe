# Copyright (c) 2023, vignesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Location(Document):
	def before_save(self):
		product_doc  = frappe.get_doc('Product',self.product_name)
		product_doc.quantity += self.quantity
		print(product_doc.quantity + self.quantity)
		product_doc.save()
		
