# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "oil_gas_joint_venture"
app_title = "Erpnext Oil Gas Upstream Joint Venture Accounting"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Oil Gas Upstream Joint Venture Accounting - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/oil_gas_joint_venture/css/oil_gas_joint_venture.bundle.css"
app_include_js = "/assets/oil_gas_joint_venture/js/oil_gas_joint_venture.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Oil Gas Upstream Joint Venture Accounting Entry": {
        "validate": "oil_gas_joint_venture.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "oil_gas_joint_venture.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "oil_gas_joint_venture.tasks.hourly_sync"
    ],
    "daily": [
        "oil_gas_joint_venture.tasks.daily_reconciliation"
    ],
    "weekly": [
        "oil_gas_joint_venture.tasks.weekly_digest"
    ]
}
