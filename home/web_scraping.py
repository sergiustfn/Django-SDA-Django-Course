import bs4
import requests
import xlsxwriter


url = 'https://www.emag.ro/laptopuri/c?ref=hp_menu_quick-nav_1_1&type=category'

result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
cases = soup.find_all('div', class_='card-v2')
context = {'data': []}

for case in cases:
    data = {}
    product_name = case.find('a', class_="card-v2-title semibold mrg-btm-xxs js-product-url")
    product_price = case.find('p', class_='product-new-price')
    data['product_name'] = product_name.text
    data['product_price'] = product_price.text
    context['data'].append(data)

workbook = xlsxwriter.Workbook('Laptopuri.xlsx')
worksheet = workbook.add_worksheet('Laptopuri de pe Emag')

row = 0
col = 0

for i in context['data']:
    worksheet.write(row, col, i['product_name'])
    worksheet.write(row, col + 1, i['product_price'])
    row += 1

workbook.close()





