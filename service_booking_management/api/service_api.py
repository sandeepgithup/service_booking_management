import frappe

@frappe.whitelist(allow_guest=True)
def receive_booking(**kwargs):
    try:
        doc = frappe.get_doc({
            "doctype": "Service Booking",
            "customer_name": kwargs.get("customer_name"),
            "service_type": kwargs.get("service_type"),
            "preferred_datetime": kwargs.get("preferred_datetime"),
            "email": kwargs.get("email"),
            "status": kwargs.get("status") or "Requested"
        })
        doc.insert(ignore_permissions=True)
        return {"message": "Booking received", "name": doc.name}

    except Exception as e:
        frappe.log_error("API Error", frappe.get_traceback())
        frappe.throw("Something went wrong.")
