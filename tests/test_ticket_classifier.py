import unittest
from classifier import classify_ticket  # your file is classifier.py

class TestTicketClassifier(unittest.TestCase):

    def test_login_issue(self):
        result = classify_ticket("I cannot log in to my account")
        self.assertIsNotNone(result)

    def test_payment_issue(self):
        result = classify_ticket("Payment failed but money was deducted")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()