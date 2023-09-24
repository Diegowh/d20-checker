import csv
import matplotlib.pyplot as plt

csv_file = "300d20.csv"
roll_counter = {}

with open(csv_file, newline='') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader) # Skipea la primera row que contiene los headers

    for row in reader:
        # La columna 2 contiene las tiradas del dado
        roll_number = int(row[1])
        roll_counter[roll_number] = roll_counter.get(roll_number, 0) + 1

numbers = list(roll_counter.keys())
frequencies = list(roll_counter.values())


plt.bar(numbers, frequencies, align='center', alpha=0.7)
plt.xlabel('Roll Number')
plt.ylabel('Frequency')
plt.title('Frecuency of d20 rolls')
plt.xticks(numbers)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()