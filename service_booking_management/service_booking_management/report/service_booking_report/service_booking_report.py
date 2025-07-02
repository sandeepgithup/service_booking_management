# Copyright (c) 2025, sessions.sandeep and contributors
# For license information, please see license.txt

# import frappe

import frappe

def execute(filters=None):
    columns = [
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data", "width": 120},
        {"label": "Preferred Date/Time", "fieldname": "preferred_datetime", "fieldtype": "Datetime", "width": 180},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]

    conditions = ""
    if filters.get("service_type"):
        conditions += " AND service_type = %(service_type)s"
    if filters.get("status"):
        conditions += " AND status = %(status)s"

    data = frappe.db.sql(f"""
        SELECT
            customer_name,
            service_type,
            preferred_datetime,  -- ✅ Corrected here
            status
        FROM `tabService Booking`
        WHERE 1=1 {conditions}
        ORDER BY preferred_datetime DESC  -- ✅ Corrected here
    """, filters, as_dict=True)

    return columns, data
