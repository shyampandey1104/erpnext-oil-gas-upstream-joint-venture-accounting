import unittest
from oil_gas_joint_venture.engine import JointVenturePartner, AuthorizationForExpenditure, OilGasJointVentureEngine

class TestOilGasJointVentureEngine(unittest.TestCase):
    def setUp(self):
        afe = AuthorizationForExpenditure("AFE-KG-D6-2026-001", "KG-DWN-98/3", "Deepwater Well D-14", 500000000.0)
        self.engine = OilGasJointVentureEngine("KG-D6 Block", afe)
        self.engine.add_partner(JointVenturePartner("ONGC-OP", "ONGC Ltd", 40.0, is_operator=True))
        self.engine.add_partner(JointVenturePartner("BP-PART", "BP Exploration", 30.0))
        self.engine.add_partner(JointVenturePartner("VED-PART", "Vedanta Cairn", 30.0))

    def test_jib_cash_call_distribution(self):
        res = self.engine.generate_monthly_jib_cash_call(100000000.0, "2026-03")
        self.assertFalse(res["afe_overrun_warning"])
        self.assertEqual(len(res["partner_shares"]), 3)
        self.assertEqual(res["partner_shares"][0]["share_payable_inr"], 40000000.0) # 40%

    def test_afe_overrun(self):
        res = self.engine.generate_monthly_jib_cash_call(550000000.0, "2026-04")
        self.assertTrue(res["afe_overrun_warning"])

if __name__ == "__main__":
    unittest.main()
