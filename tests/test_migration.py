import unittest
from src.migration import assess, summarize
from src.approval import Change, evaluate

class MigrationTests(unittest.TestCase):
    def test_coverage(self):
        result=assess([{"id":"a","type":"linux","source":"zabbix","owner":"ops","criticality":"high","target_coverage":False}])
        self.assertEqual(summarize(result)["coverage_pct"],0)
        self.assertEqual(result[0]["status"],"gap")
    def test_approval_gate(self):
        self.assertEqual(evaluate(Change("a","deploy","low"))["decision"],"BLOCKED")
        self.assertEqual(evaluate(Change("a","deploy","high",True))["decision"],"REVIEW")
        self.assertEqual(evaluate(Change("a","deploy","low",True))["decision"],"ELIGIBLE")
if __name__ == "__main__": unittest.main()
