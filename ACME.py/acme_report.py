"""module to generate random products and print a summary of them"""

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + " " + sample(NOUNS, 1)[0]
        prod = Product(name)
        prod.price = randint(5, 101)
        prod.weight = randint(5, 101)
        prod.flammability = uniform(0, 2.5)
        products.append(prod)
    return products


def inventory_report(products):
    name_set = set()
    price_sum = 0
    weight_sum = 0
    flam_sum = 0
    for prod in products:
        name_set.add(prod.name)
        price_sum += prod.price
        weight_sum += prod.weight
        flam_sum += prod.flammability
    print('Number of unique product names', len(name_set))
    print('Average Price', price_sum/len(products))
    print('Average weight', weight_sum/len(products))
    print('Average flammability', flam_sum/len(products))


if __name__ == '__main__':
    inventory_report(generate_products())
