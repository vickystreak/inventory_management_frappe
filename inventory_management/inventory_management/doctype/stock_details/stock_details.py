# Copyright (c) 2023, vignesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StockDetails(Document):
	pass


def stock_update(doc, method):
    # Fetch all Product Movement records for the product and location
    movements = frappe.get_all("Product Movement", filters={
        "product_id": doc.product_id,
        "from_location": doc.location,
    })

    balance = 0

    # Calculate the balance by summing the quantities of all movements
    for movement in movements:
        balance += movement.qty

    # Update the Inventory Balance doctype
    inventory_balance = frappe.get_doc({
        "doctype": "Inventory Balance",
        "product_id": doc.product_id,
        "location": doc.location,
        "balance_qty": balance
    })

    stock_update.save()