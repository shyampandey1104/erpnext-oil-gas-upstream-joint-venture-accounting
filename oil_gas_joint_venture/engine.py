"""Upstream Oil & Gas Joint Venture Accounting & Joint Interest Billing (JIB) Engine."""
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Dict, Any, Optional

@dataclass
class JointVenturePartner:
    partner_id: str
    company_name: str
    working_interest_pct: float     # e.g., Operator 40%, Partner A 30%, Partner B 30%
    is_operator: bool = False

@dataclass
class AuthorizationForExpenditure:
    afe_number: str
    block_name: str
    well_name: str
    approved_capex_ceiling_inr: float
    current_expended_inr: float = 0.0

class OilGasJointVentureEngine:
    def __init__(self, block_name: str, afe: AuthorizationForExpenditure):
        self.block_name = block_name
        self.afe = afe
        self.partners: Dict[str, JointVenturePartner] = {}
        self.cash_calls: List[Dict[str, Any]] = []

    def add_partner(self, partner: JointVenturePartner):
        self.partners[partner.partner_id] = partner

    def generate_monthly_jib_cash_call(self, total_capex_incurred_inr: float, billing_month: str) -> Dict[str, Any]:
        total_wi = sum(p.working_interest_pct for p in self.partners.values())
        if abs(total_wi - 100.0) > 0.01:
            raise ValueError(f"Total Working Interest {total_wi}% does not sum to 100.0%")

        # AFE Budget Check
        if (self.afe.current_expended_inr + total_capex_incurred_inr) > self.afe.approved_capex_ceiling_inr:
            afe_overrun = True
        else:
            afe_overrun = False
        
        self.afe.current_expended_inr += total_capex_incurred_inr

        partner_splits = []
        for p in self.partners.values():
            amount = round(total_capex_incurred_inr * (p.working_interest_pct / 100.0), 2)
            partner_splits.append({
                "partner_id": p.partner_id,
                "partner_name": p.company_name,
                "working_interest_pct": p.working_interest_pct,
                "share_payable_inr": amount
            })

        call_record = {
            "billing_month": billing_month,
            "block_name": self.block_name,
            "total_capex_inr": total_capex_incurred_inr,
            "afe_overrun_warning": afe_overrun,
            "partner_shares": partner_splits
        }
        self.cash_calls.append(call_record)
        return call_record
