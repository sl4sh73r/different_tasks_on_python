sales_dict = {}
def inputs():
    while True:
        try:
            yield input().split()
        except (ValueError, EOFError):
            return

for customer, purchase, count in inputs():
    if customer not in sales_dict:
        sales_dict[customer] = {purchase : int(count)}
    else:
        sales_dict[customer][purchase] = sales_dict[customer].get(purchase, 0) + int(count)

for customer, purchases in sorted(sales_dict.items()):
    print(customer +':')
    for purchase, count in sorted(sales_dict[customer].items()):
        print(purchase, count)
