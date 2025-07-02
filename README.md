# Service Booking Management

A custom ERPNext module for managing spa and therapy bookings at a wellness center.

---


## 📦 Features

- Custom Doctype: `Service Booking`
- Workflow: Requested → Approved → Completed
- Email notification sent on booking approval
- Jinja-based Print Format for booking confirmation
- Custom Report with filters: Service Type & Status
- Bonus: REST API endpoint to send booking details via GET (Tested via Postman)

---

## 🛠️ Installation

```bash
# Go to your bench folder
cd ~/frappe-bench

# Get the app
bench get-app https://github.com/sandeepgithup/service_booking_management.git

# Install the app on your site
bench --site your-site-name install-app service_booking_management


---

## ⚙️ System Info

| Setting        | Value              |
|----------------|--------------------|
| OS             | Ubuntu 22.04       |
| Python Version | 3.10.17            |
| Frappe Version | 15.68.1            |
| ERPNext Version| Not Installed (Custom App Only) |
| Developer Mode | Enabled            |
| Tools Used     | VS Code, Postman   |

