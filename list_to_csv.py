#this program will read from a list and a txt file, clean the data and deliver it to a csv file based on a condition
import datetime
import csv

list_nums = [ "15", "52", "65","18", "17","21","9","45", "59",  "18", "17","21","9","38","18", "17","21","9", "28","100",
  "12","48", "39","49","38","20","40","58","12","30","45","50","56", "46","14", "15",  "16",  "30", "70", "20",
   "84", "20", "38",  "42", "89", "67", "79",  "653", "59","49" ]
#list of  50 integers
list_data2 = []
#empty list for data from txt file.

input_file =open("data.txt")
for line in input_file:
    list_data2.append(line)
#appends numbers from txt file to empty list
input_file.close()

data = zip(list_nums, list_data2)
# list and txt are zipped to allow for simultaneous iteration

with open("data1.csv", "w", newline="") as f1, open("data2.csv", "w", newline="") as f2:
 writer1 = csv.writer(f1)
 writer2 = csv.writer(f2)

 labels = ["Value from Csv","Data from list","Guess","Result","time"]

 writer1.writerow(labels)
 writer2.writerow(labels)



 for row in data:
     value_a = int(row[0].strip())
     value_b = int(row[1].strip())
     correct_answer = value_a + value_b
     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     f1.flush()
     f2.flush()

     try:
      guess= float(input(f" what is {value_a} + {value_b}? "))
      if guess == correct_answer:
         print(f"correct answer writing {correct_answer} to file")
         difference = 0
         new_row= list(row) +[value_a, value_b, "Correct",timestamp]
         writer1.writerow(new_row)
      else:
         print("Wrong! sending data to review file....")
         difference = correct_answer - guess
         new_row = list(row) + [value_a, value_b, guess, "Incorrect",timestamp]
         writer2.writerow(new_row)
     except ValueError:
        print("please use numbers")




