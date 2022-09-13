import math
import time

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

def divide_with_error_handling():
    input1 = input("enter 1st number: ")
    input2 = input("input 2nd number: ")    

    if input2 == 0:
        print(" WARNING, division by 0")

    else:
        answer = input1/input2
        return answer

def decode_csv_data_into_dictionary():
    input1 = input("Enter input here: ")
    

fizz_buzz_game()

print(sphere_volume(3))