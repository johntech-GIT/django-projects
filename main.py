product_1 = Product(name = "Витая пара (3 м)", price = 993.0)
product_1.save()

product_2 = Product.objects.create(name = "Клавиатура", price = 1060.0)