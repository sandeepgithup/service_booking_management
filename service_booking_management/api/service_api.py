import frappe
import requests

@frappe.whitelist(allow_guest=True)
def receive_booking(**kwargs):
    try:
        # Create Service Booking document
        doc = frappe.get_doc({
            "doctype": "Service Booking",
            "customer_name": kwargs.get("customer_name"),
            "service_type": kwargs.get("service_type"),
            "preferred_datetime": kwargs.get("preferred_datetime"),
            "email": kwargs.get("email"),
            "status": kwargs.get("status") or "Requested"
        })
        doc.insert(ignore_permissions=True)

        #  Send data to webhook
        webhook_url = "https://webhook.site/42e86370-46f9-45a6-928b-2d16cb8e8d38"
        payload = {
            "customer_name": doc.customer_name,
            "service_type": doc.service_type,
            "preferred_datetime": str(doc.preferred_datetime),
            "email": doc.email,
            "status": doc.status
        }

        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code != 200:
                frappe.log_error("Webhook Error", f"Status: {response.status_code}\n{response.text}")
        except Exception:
            frappe.log_error("Webhook Send Failed", frappe.get_traceback())

        return {
            "message": "Booking received and webhook sent",
            "booking_id": doc.name
        }

    except Exception:
        frappe.log_error("API Error", frappe.get_traceback())
        frappe.throw("Something went wrong.")
