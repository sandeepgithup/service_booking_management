// Copyright (c) 2025, sessions.sandeep and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking Report"] = {
	"filters": [
		{
			"fieldname": "service_type",
			"label": "Service Type",
			"fieldtype": "Select",
			"options": ["", "Therapy", "Spa", "Others"],
			"default": ""
		},
		{
			"fieldname": "status",
			"label": "Status",
			"fieldtype": "Select",
			"options": ["", "Requested", "Approved", "Completed"],
			"default": ""
		}
	]
};
