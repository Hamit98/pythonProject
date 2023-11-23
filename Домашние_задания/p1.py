if __name__ == '__main__':

    sales = [
        {"id": 1, "product": "Playstation 5", "quantity": 1, "price": 1000},
        {"id": 2, "product": "Rocket launcher", "quantity": 10, "price": 15000},
        {"id": 3, "product": "Apple Ipod", "quantity": 3, "price": 9999},
        {"id": 4, "product": "7x62mm bullets", "quantity": 1000, "price": 50},
        {"id": 5, "product": "Apples", "quantity": 20, "price": 25.98},
        {"id": 6, "product": "Pineapples", "quantity": 2, "price": 100},
        {"id": 7, "product": "Laptop Lenovo", "quantity": 1, "price": 15600},
        {"id": 8, "product": "Chocolate cookies", "quantity": 7, "price": 34}
    ]

    customer_ids = {101, 102, 103, 104, 105, 106}

    customer_transactions = {
        101: [3, 7],
        102: [2, 1],
        103: [8],
        104: [4, 6],
        106: [4, 2]
    }

    # Задача 1: Расчет общего объема продаж для каждого продукта
    product_total_sales = {}
    for transaction in sales:
        product = transaction["product"]
        quantity = transaction["quantity"]
        price = transaction["price"]
        total_sales_value = quantity * price

        if product in product_total_sales:
            product_total_sales[product] += total_sales_value
        else:
            product_total_sales[product] = total_sales_value

    # Задача 2: Определение самого продаваемого продукта
    most_sold_product = max(product_total_sales, key=product_total_sales.get)

    # Задача 3: Расчет общей суммы продаж для всего бизнеса
    total_sales = sum(product_total_sales.values())

    # Задача 4: Расчет средней стоимости покупки для одного клиента
    average_purchase_per_customer = {}
    for customer, transactions in customer_transactions.items():
        total_purchase = sum([sales[id - 1]["quantity"] * sales[id - 1]["price"] for id in transactions])
        average_purchase_per_customer[customer] = total_purchase

    # Задача 5: Определение клиента с наибольшей общей стоимостью покупки
    customer_with_highest_total_purchase = max(average_purchase_per_customer, key=average_purchase_per_customer.get)

    # Задача 6: Определение клиентов, которые не сделали никакой покупки
    customers_with_no_purchase = [customer for customer in customer_ids if customer not in customer_transactions]

    # Задача 7: Определение продукта, который приобретен только одним клиентом
    unique_products = set()
    shared_products = set()

    for customer, transactions in customer_transactions.items():
        for transaction_id in transactions:
            product = sales[transaction_id - 1]["product"]
            if product in unique_products:
                shared_products.add(product)
            else:
                unique_products.add(product)

    products_bought_by_one_customer = unique_products - shared_products

    # Задача 8: Найти топ 3 клиентов по общей стоимости покупки
    top_3_customers = sorted(average_purchase_per_customer, key=average_purchase_per_customer.get, reverse=True)[:3]

    print("Общий объем продаж для каждого продукта:", product_total_sales)
    print("Самый продаваемый продукт:", most_sold_product)
    print("Общая сумма продаж для всего бизнеса:", total_sales)
    print("Средняя стоимость покупки для одного клиента:", average_purchase_per_customer)
    print("Клиент с наибольшей общей стоимостью покупки:", customer_with_highest_total_purchase)
    print("Клиенты, которые не сделали никакой покупки:", customers_with_no_purchase)
    print("Продукты, приобретенные только одним клиентом:", products_bought_by_one_customer)
    print("Топ 3 клиента по общей стоимости покупки:", top_3_customers)
