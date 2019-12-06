import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_stealabilityweight(self):
        prod = Product('Test Product')
        prod.price = 100
        prod.weight = 201
        self.assertEqual(prod.stealability(), 'Not so stealable...')

        prod = Product('Test Product')
        prod.price = 100
        prod.weight = 200
        self.assertEqual(prod.stealability(), 'Kinda stealable')

        prod = Product('Test Product')
        prod.price = 100
        prod.weight = 100
        self.assertEqual(prod.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        for prod in products:
            words = prod.name.split(' ')
            adjective = words[0]
            noun = words[1]
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
