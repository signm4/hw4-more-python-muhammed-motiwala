import math
import time

''' This function replaces any number divisible by 3 with Fizz, 5 with Buzz, and both with FizzBuzz'''
def fizz_buzz_game(): 
    start = time.time()
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i% 5 == 0:
            print("Buzz")
        else:
            print(i) 

    end = time.time()
    elapsed_time = end - start
    print (elapsed_time)

def sphere_volume(rad):
    # rad = input("Enter the Radius")
    volume1 = (math.pow(rad, 3)) * (math.pi) * (4/3)
    return (volume1)

def divide_with_error_handling(int1, int2):
    # input1 = input("enter 1st number: ")
    # input2 = input("input 2nd number: ")    

    # if int2 == 0:
    #     print(" WARNING, division by 0")

    # else:
    #     answer = int1/int2
    #     return answer

    try:
        return int1/int2
    except:
        print("WARNING can't divide by 0")

def decode_csv_data_into_dictionary(csv_file_name):
    input_file = open(csv_file_name)

    # read the first column of names and make a list
    column_names_string = input_file.readline().strip()
    list_of_column_names = column_names_string.split(",")

    # create dict with column name as keys("none" val for now)
    decoded_csv_data_dictionary = dict.fromkeys(list_of_column_names)

    # read in the rest of file and create table of the deata
    csv_table_data = []
    for line in input_file:
        csv_table_data.append(line.strip().split(","))
    
    #iterate over table column by column and append data to the proper column key

    for index, key in enumerate(decoded_csv_data_dictionary):
        decoded_csv_data_dictionary[key] = []
        for row in csv_table_data:
            decoded_csv_data_dictionary[key].append(row[index])

    return decoded_csv_data_dictionary

#print(decode_csv_data_into_dictionary('data.csv'))
    

fizz_buzz_game()

print(sphere_volume(3))

print(divide_with_error_handling(6, 9))
print(divide_with_error_handling(6, 0))