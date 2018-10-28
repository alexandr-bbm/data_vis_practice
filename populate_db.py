import os

from django.contrib.gis.geos import Point


def run():
    clear_db()
    populate_db()


def clear_db():
    models = [Region, Dept, Employee, Customer, Order]
    for model in models:
        model.objects.all().delete()


def populate_db():
    regions = create_model_instances(Region, [
        {'name': 'North America'},
        {'name': 'South America'},
        {'name': 'Africa / Middle East'},
        {'name': 'Asia'},
        {'name': 'Europe'},
    ])
    depts = create_model_instances(Dept, [
        {'region': regions[0], 'geo_coords': Point(38.881799, -77.018364), 'name': 'Administration', },
        {'region': regions[0], 'geo_coords': Point(38.933656, -77.065035), 'name': 'Finance', },
        {'region': regions[0], 'geo_coords': Point(38.886525, -76.988218), 'name': 'Sales', },
        {'region': regions[1], 'geo_coords': Point(6.232213, -75.554030), 'name': 'Sales', },
        {'region': regions[2], 'geo_coords': Point(26.713333, 20.111205), 'name': 'Sales', },
        {'region': regions[3], 'geo_coords': Point(32.120960, 110.880505), 'name': 'Sales', },
        {'region': regions[4], 'geo_coords': Point(34.687161, 33.047102), 'name': 'Sales', },
        {'region': regions[0], 'geo_coords': Point(85.3240, 27.7172), 'name': 'Operations', },
        {'region': regions[1], 'geo_coords': Point(3.399982, -76.431565), 'name': 'Operations', },
        {'region': regions[2], 'geo_coords': Point(25.020791, 28.635636), 'name': 'Operations', },
        {'region': regions[3], 'geo_coords': Point(56.477242, 84.991905), 'name': 'Operations', },
        {'region': regions[4], 'geo_coords': Point(41.827361, 14.022168), 'name': 'Operations', },
    ])

    dept_admin = depts[0]
    dept_finance = depts[1]
    dept_sales_r_1 = depts[2]
    dept_sales_r_2 = depts[3]
    dept_sales_r_3 = depts[4]
    dept_sales_r_4 = depts[5]
    dept_sales_r_5 = depts[6]
    dept_operations_r_1 = depts[7]
    dept_operations_r_2 = depts[8]
    dept_operations_r_3 = depts[9]
    dept_operations_r_4 = depts[10]
    dept_operations_r_5 = depts[11]

    employees = create_model_instances(Employee, [
        {'last_name': 'Magee', 'first_name': 'Colin', 'title': 'Sales Representative', 'salary': '1400', 'dept': dept_sales_r_1},
        {'last_name': 'Giljum', 'first_name': 'Henry', 'title': 'Sales Representative', 'salary': '1490', 'dept': dept_sales_r_2},
        {'last_name': 'Sedeghi', 'first_name': 'Yasmin', 'title': 'Sales Representative', 'salary': '1515', 'dept': dept_sales_r_3},
        {'last_name': 'Nguyen', 'first_name': 'Mai', 'title': 'Sales Representative', 'salary': '1525', 'dept': dept_sales_r_4},
        {'last_name': 'Dumas', 'first_name': 'Andre', 'title': 'Sales Representative', 'salary': '1450', 'dept': dept_sales_r_5},
        {'last_name': 'Velasquez', 'first_name': 'Carmen', 'title': 'President', 'salary': '2500', 'dept': dept_admin},
        {'last_name': 'Ngao', 'first_name': 'LaDoris', 'title': 'VP, Operations', 'salary': '1450', 'dept': dept_admin},
        {'last_name': 'Nagayamn', 'first_name': 'Midori', 'title': 'VP, Sales', 'salary': '1400', 'dept': dept_admin},
        {'last_name': 'Ropeburn', 'first_name': 'Audry', 'title': 'VP, Administration', 'salary': '1550', 'dept': dept_admin},
        {'last_name': 'Urguhart', 'first_name': 'Molly', 'title': 'Warehouse Manager', 'salary': '1200', 'dept': dept_finance},
        {'last_name': 'Menchu', 'first_name': 'Robertn', 'title': 'Warehouse Manager', 'salary': '1250', 'dept': dept_finance},
        {'last_name': 'Biri', 'first_name': 'Ben', 'title': 'Warehouse Manager', 'salary': '1100', 'dept': dept_operations_r_1},
        {'last_name': 'Catchpole', 'first_name': 'Antoinette', 'title': 'Warehouse Manager', 'salary': '1300', 'dept': dept_operations_r_2},
        {'last_name': 'Havel', 'first_name': 'Marta', 'title': 'Warehouse Manager', 'salary': '1307', 'dept': dept_operations_r_3},
        {'last_name': 'Maduro', 'first_name': 'Elena', 'title': 'Stock Clerk', 'salary': '1400', 'dept': dept_operations_r_4},
        {'last_name': 'Smith', 'first_name': 'George', 'title': 'Stock Clerk', 'salary': '940', 'dept': dept_operations_r_5},
        {'last_name': 'Nozaki', 'first_name': 'Akira', 'title': 'Stock Clerk', 'salary': '1200', 'dept': dept_operations_r_3},
        {'last_name': 'Patei', 'first_name': 'Vikram', 'title': 'Stock Clerk', 'salary': '795', 'dept': dept_operations_r_2},
        {'last_name': 'Newman', 'first_name': 'Chad', 'title': 'Stock Clerk', 'salary': '750', 'dept': dept_operations_r_1},
        {'last_name': 'Markarian', 'first_name': 'Alexandr', 'title': 'Stock Clerk', 'salary': '850', 'dept': dept_operations_r_1},
        {'last_name': 'Chang', 'first_name': 'Eddie', 'title': 'Stock Clerk', 'salary': '800', 'dept': dept_operations_r_1},
        {'last_name': 'Patel', 'first_name': 'Radha', 'title': 'Stock Clerk', 'salary': '795', 'dept': dept_operations_r_4},
        {'last_name': 'Dancs', 'first_name': 'Bela', 'title': 'Stock Clerk', 'salary': '860', 'dept': dept_operations_r_2},
        {'last_name': 'Schwartz', 'first_name': 'Sylvie', 'title': 'Stock Clerk', 'salary': '1100', 'dept': dept_operations_r_1},
        {'last_name': 'novikova', 'first_name': 'nina', 'title': 'Warehouse Manager', 'salary': '2000', 'dept': dept_operations_r_3},
    ])

    sales_rep_1 = employees[0]
    sales_rep_2 = employees[1]
    sales_rep_3 = employees[2]
    sales_rep_4 = employees[3]
    sales_rep_5 = employees[4]
    
    customers = create_model_instances(Customer, [
        {'name': 'Unisports', 'phone': '55-2066101', 'region': regions[0], 'sales_rep': sales_rep_1},
        {'name': 'Simms', 'phone': '81-20101', 'region': regions[0], 'sales_rep': sales_rep_1},
        {'name': 'Delhi', 'phone': '91-10351', 'region': regions[1], 'sales_rep': sales_rep_1},
        {'name': 'Womansport', 'phone': '1-206-104-0103', 'region': regions[1], 'sales_rep': sales_rep_1},
        {'name': 'Kam', 'phone': '852-3692888', 'region': regions[1], 'sales_rep': sales_rep_2},
        {'name': 'Sportique', 'phone': '33-2257201', 'region': regions[2], 'sales_rep': sales_rep_2},
        {'name': 'Sweet', 'phone': '234-6036201', 'region': regions[2], 'sales_rep': sales_rep_2},
        {'name': 'Muench', 'phone': '1-716-555-7171', 'region': regions[3], 'sales_rep': sales_rep_2},
        {'name': 'Beisbol', 'phone': '7-3892456', 'region': regions[3], 'sales_rep': sales_rep_2},
        {'name': 'Futbol', 'phone': '1-415-555-6281', 'region': regions[4], 'sales_rep': sales_rep_3},
        {'name': 'Kuhn', 'phone': '2-11129', 'region': regions[4], 'sales_rep': sales_rep_3},
        {'name': 'Hamada', 'phone': '20-120921', 'region': regions[0], 'sales_rep': sales_rep_3},
        {'name': 'Big', 'phone': '2-11329', 'region': regions[1], 'sales_rep': sales_rep_3},
        {'name': 'Ojibvay', 'phone': '2411129', 'region': regions[2], 'sales_rep': sales_rep_4},
        {'name': 'Sporta', 'phone': '2-111212', 'region': regions[3], 'sales_rep': sales_rep_5},
    ])

    customer1 = customers[0]
    customer2 = customers[1]
    customer3 = customers[2]

    orders = create_model_instances(Order, [
        {'customer': customer1, 'date_ordered': '2018-09-09T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 1000},
        {'customer': customer1, 'date_ordered': '2018-09-10T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 1000},
        {'customer': customer2, 'date_ordered': '2018-09-11T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 2000},
        {'customer': customer2, 'date_ordered': '2018-09-12T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 2000},
        {'customer': customer2, 'date_ordered': '2018-09-13T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 2500},
        {'customer': customer3, 'date_ordered': '2018-09-13T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 30.33},
        {'customer': customer3, 'date_ordered': '2018-09-14T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 10000},
        {'customer': customer3, 'date_ordered': '2018-09-14T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 8888},
        {'customer': customer1, 'date_ordered': '2018-09-14T12:35:01.828Z', 'date_shipped': '2018-09-29T12:35:01.828Z', 'total': 1400},
    ])

    order1 = orders[0]
    order2 = orders[1]
    order3 = orders[2]

    products = create_model_instances(Product, [
        {'name': 'Football ball', 'short_descr': 'description. '},
        {'name': 'Basketball ball', 'short_descr': 'description. '},
        {'name': 'Golf ball', 'short_descr': 'description. '},
        {'name': 'Tenis ball', 'short_descr': 'description. '},
    ])

    product1 = products[0]
    product2 = products[1]
    product3 = products[2]
    product4 = products[4]


    items = create_model_instances(Item, [
        {'order': order1, 'product': product1, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order1, 'product': product2, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order2, 'product': product3, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order2, 'product': product4, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order2, 'product': product1, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order3, 'product': product2, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order3, 'product': product3, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order3, 'product': product4, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order1, 'product': product1, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order1, 'product': product1, 'quantity_ordered': 3, 'quantity_shipped': 2},
        {'order': order1, 'product': product2, 'quantity_ordered': 3, 'quantity_shipped': 2},
        {'order': order2, 'product': product3, 'quantity_ordered': 3, 'quantity_shipped': 2},
        {'order': order2, 'product': product4, 'quantity_ordered': 3, 'quantity_shipped': 2},
        {'order': order2, 'product': product1, 'quantity_ordered': 3, 'quantity_shipped': 2},
        {'order': order3, 'product': product2, 'quantity_ordered': 3, 'quantity_shipped': 2},
        {'order': order3, 'product': product3, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order3, 'product': product4, 'quantity_ordered': 5, 'quantity_shipped': 1},
        {'order': order1, 'product': product1, 'quantity_ordered': 5, 'quantity_shipped': 1},
    ])


def create_model_instances(model, data):
    result = []

    for idx, value in enumerate(data):
        instance, created = model.objects.get_or_create(**value)
        result.append(instance)

    return result


if __name__ == '__main__':
    print('\n' + ('=' * 80) + '\n')
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'data_vis_practice.settings')
    django.setup()
    from lab1.models import Region, Dept, Employee, Customer, Order, Product, Item

    run()
