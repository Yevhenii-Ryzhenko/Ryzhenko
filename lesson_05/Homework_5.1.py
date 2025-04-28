# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)


print ('Варіант №1 (навчальний):')
year = 2017
engine = 1.6
car_price = 36000

car_list_v1 = []
for car_model, car_info in car_data.items():
    if car_info[1] >= year and car_info[2] >= engine and car_price >= car_info[4]:
        car_list_v1.append((car_model, car_info[4]))
wish_list = sorted(car_list_v1, key=lambda x: x[1])
print(f'Під запит підходять наступні моделі: {wish_list[:5]}')
print('-'*100)


print ('Варіант №2 (більш практичний та правильний):')
car_list_v2 = []
for car_model, car_info in car_data.items():
    if car_info[1] >= search_criteria[0] and car_info[2] >= search_criteria[1] and  car_price >= car_info[4]:
        car_list_v2.append((car_model, car_info[4]))
wish_list = sorted(car_list_v2, key=lambda x: x[1])
print(f'Під запит підходять наступні моделі: {wish_list[:5]}')
print('-'*100)

print ('Варіант №3 (інтерактивний):')
car_list_v3 = []
year = int(input('Будь ласка введіть мінімальний бажаний рік випуску авто (тільки цілі числа): '))
engine_volume = float(input('Будь ласка введіть мінімальний бажаний об\'єм двигуна: '))
price = int(input('Будь ласка введіть максимальну бажану вартість авто (тільки цілі числа): '))
car_list = []
for car_model, car_info in car_data.items():
    if car_info[1] >= year and car_info[2] >= engine_volume and  car_info[4] <= price:
        car_list_v3.append((car_model, car_info[4]))
wish_list = sorted(car_list_v3, key=lambda x: x[1])
print(f'Під ваш запит підходять наступні моделі: {wish_list}')
user_choice = input('Введіть назву моделі, яка вам подобалася і я надам більше інформації: ')
print(f'Ось більше інформації про Ваш вибір: {car_data.get(user_choice, 'ghsfjkhgjksdf')}')
print('-'*100)
