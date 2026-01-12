#!/usr/bin/env python3
"""
DATA CLEANER V1: Data merging but gamified
"""
import datetime
import csv

header = ["Value_A", "Value_B", "Status","Answer", "Timestamp"]

csv_data1 = [header]
csv_data2 = [header]
list_nums = [ "15", "52", "65","18", "17","21","9","45", "59",  "18", "17","21","9","38","18", "17","21","9", "28","100",
  "12","48", "39","49","38","20","40","58","12","30","45","50","56", "46","14", "15",  "16",  "30", "70", "20",
   "84", "20", "38",  "42", "89", "67", "79",  "653", "59","49" ]

list_data2 = []

with open("data.txt", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            list_data2.append(row[0])

data = zip(list_nums, list_data2)

for row in data:

         value_a = int(row[0].strip())
         value_b = int(row[1].strip())
         correct_answer = value_a + value_b
         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         # 2. The "Infinite" Gate
         while True:
             try:
                 guess = input(f"What is {value_a} + {value_b}?")
                 if int(guess) == correct_answer:
                   csv_data1.append([value_a, value_b, correct_answer, "Correct", timestamp])
                   print("Correct Answer, Sending data to Csv File1...")
                 else:
                     csv_data2.append([value_a, value_b, correct_answer, "Incorrect", timestamp])
                     print("Wrong Answer, Sending data to Csv File2...")

                 break

             except ValueError:

              print("Not a number! Try again.")
             # We do NOT break here. The loop automatically restarts!

             except Exception as e:

                 print(f"Error: {e}")
                 break

# Write the clean data first
with open('cleaned_data.csv', 'w', newline='') as f1:
    writer1 = csv.writer(f1)
    writer1.writerows(csv_data1)
    print("Cleaned data saved successfully.")


with open('needs_review.csv', 'w', newline='') as f2:
    writer2 = csv.writer(f2)
    writer2.writerows(csv_data2)
    print("Review file updated.")



