import math
import time

number = int(input("Enter the number to find the square root of: "))
delay_ms = int(input("Enter delay in milliseconds: "))

time.sleep(delay_ms / 1000) 
result = math.sqrt(number)

print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
