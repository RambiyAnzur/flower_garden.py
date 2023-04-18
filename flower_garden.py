# Код программы Flower Garden

import random

flowers = ['розы', 'тюльпаны', 'орхидеи', 'лилии', 'ирисы']

def create_flower():
    # функция для создания случайного цветка
    color = random.choice(['красный', 'желтый', 'розовый', 'белый', 'фиолетовый'])
    flower = random.choice(flowers)
    return f"{color} {flower}"

garden = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(create_flower())
    garden.append(row)

for row in garden:
    print(row)
