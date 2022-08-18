"""Generate sales report showing total melons each salesperson sold."""


def sales_report(file):
    open_file = open(file)

    sales_people = {}

    for line in open_file:
        line = line.rstrip()
        entries = line.split('|')
        salesperson, melon_price, melon_quntity = entries[0], float(entries[1]), int(entries[2])
        sales_people[salesperson] = [melon_price, melon_quntity]


    return sales_people

print(sales_report('sales-report.txt'))
