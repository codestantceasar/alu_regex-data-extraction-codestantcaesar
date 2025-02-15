import unittest
from regex_validators import (
    validate_email,
    validate_url,
    validate_phone,
    validate_credit_card,
    validate_time,
    extract_html_tags,
    validate_hashtag,
    validate_currency,
)

class TestRegexValidators(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("firstname.lastname@company.co.uk"))
        self.assertFalse(validate_email("user@@example.com"))
        self.assertFalse(validate_email("user.com"))

    def test_validate_url(self):
        self.assertTrue(validate_url("https://www.example.com"))
        self.assertTrue(validate_url("https://subdomain.example.org/page"))
        self.assertFalse(validate_url("htt://badurl.com"))
        self.assertFalse(validate_url("www.example.com"))

    def test_validate_phone(self):
        self.assertTrue(validate_phone("(123) 456-7890"))
        self.assertTrue(validate_phone("123-456-7890"))
        self.assertTrue(validate_phone("123.456.7890"))
        self.assertFalse(validate_phone("1234567890"))
        self.assertFalse(validate_phone("123-456-789"))

    def test_validate_credit_card(self):
        self.assertTrue(validate_credit_card("1234 5678 9012 3456"))
        self.assertTrue(validate_credit_card("1234-5678-9012-3456"))
        self.assertFalse(validate_credit_card("1234567890123456"))
        self.assertFalse(validate_credit_card("1234 5678 9012"))

    def test_validate_time(self):
        self.assertTrue(validate_time("14:30"))
        self.assertTrue(validate_time("2:30 PM"))
        self.assertFalse(validate_time("25:00"))
        self.assertFalse(validate_time("2:60 PM"))

    def test_extract_html_tags(self):
        html_text = '<p>Hello</p> <div class="example">Content</div>'
        tags = extract_html_tags(html_text)
        self.assertIn(("p", "Hello"), tags)
        self.assertIn(("div", "Content"), tags)
        self.assertNotIn(("p", "Content"), tags)

    def test_validate_hashtag(self):
        self.assertTrue(validate_hashtag("#example"))
        self.assertTrue(validate_hashtag("#ThisIsAHashtag"))
        self.assertFalse(validate_hashtag("example"))
        self.assertFalse(validate_hashtag("#example!"))

    def test_validate_currency(self):
        self.assertTrue(validate_currency("$19.99"))
        self.assertTrue(validate_currency("$1,234.56"))
        self.assertFalse(validate_currency("19.99"))
        self.assertFalse(validate_currency("$1234.567"))
        self.assertFalse(validate_currency("$12,34"))

if __name__ == '__main__':
    unittest.main()