# ERPNext Upstream Oil & Gas Joint Venture Accounting & JIB Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![Energy Sector](https://img.shields.io/badge/Oil%20%26%20Gas-Upstream%20E%26P-orange.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

In upstream oil and gas exploration and production (E&P), exploration blocks are operated under **Production Sharing Contracts (PSC)** by multi-party consortiums (e.g. Operator 40%, Partner A 30%, Partner B 30%).

Critical accounting bottlenecks include:
1. **Joint Interest Billing (JIB) Disputes:** The operating company incurs drilling, offshore rig, and seismic capex, which must be apportioned monthly to non-operating partners strictly according to their **Working Interest (WI%)**.
2. **Authorization for Expenditure (AFE) Overruns:** Drilling deepwater wells involves high financial risk; expending capex beyond approved AFE budget ceilings without prior joint operating committee (JOC) approval leads to partner billing disputes.
3. **Cash Call Default Risk:** Non-operating partners must wire cash calls on scheduled notice; delays trigger punitive cash call penalty interest or forfeiture of equity barrels.

This Frappe application implements institutional Joint Venture Accounting tailored for upstream hydrocarbon operators.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["Approved Well Drilling AFE Ceiling (e.g. 500 Cr)"] -->|Budget Ceiling Interlock| B["AFE Capital Control Ledger"]
    C["Offshore Drilling & Rig Capex Incurred"] --> B
    B -->|Check AFE Budget Availability| D{"Capex Within AFE Ceiling?"}
    D -->|Yes| E["Apportion to Partners via Working Interest (WI%)"]
    D -->|No (Overrun)| F["AFE Overrun Warning: Requires Supplementary JOC Approval"]
    E -->|Generate Monthly Cash Call Notice| G["Joint Interest Billing (JIB) Statement"]
    G -->|Disburse Cash Calls to Bank Accounts| H["ERPNext Accounts Receivable Settlement"]
```

---

## 🚀 Key Engineering Capabilities

- **Working Interest Pro-Rata Allocator:** Mathematically divides drilling and operational expenditure among consortium partners.
- **AFE Budget Interlock:** Prevents operational over-expenditure without supplementary AFE approvals.
- **Monthly Joint Interest Billing (JIB):** Generates standardized upstream oil & gas joint billing statements.
- **Cash Call Reconciliation:** Tracks partner cash advance receipts and adjusts against actual work order billings.

---

## 📂 Frappe DocType Schema & Data Structure

```text
oil_gas_joint_venture/
├── oil_gas_joint_venture_core/
│   ├── doctype/
│   │   ├── joint_venture_block/
│   │   │   ├── joint_venture_block.json
│   │   │   ├── joint_venture_block.py
│   │   │   └── joint_venture_block.js
│   │   └── authorization_for_expenditure/
│   │       └── authorization_for_expenditure.json
│   └── workspace/
│       └── oil_gas_joint_venture_workspace/
│           └── oil_gas_joint_venture_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/oil_gas_joint_venture.api.generate_monthly_jib_cash_call`
- **Whitelisted Method:** `@frappe.whitelist() def add_partner(partner_id, company_name, working_interest_pct)`
- **Hooks Event:** `on_submit` of `Purchase Invoice` (Rig Capex) updates active AFE budget consumption.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/erpnext-oil-gas-upstream-joint-venture-accounting
bench --site erp.yourdomain.com install-app oil_gas_joint_venture
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Optimized for E&P Operators, Energy Consortiums, and Hydrocarbon Explorers.
