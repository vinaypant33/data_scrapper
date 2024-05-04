import itertools
import os

def brute_force(file_path, password_length):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    total_combinations = len(digits) ** password_length
    file_size_bytes = total_combinations * password_length
    with open(file_path, 'w') as file:
        for combination in itertools.product(digits, repeat=password_length):
            file.write(''.join(map(str, combination)) + '\n')
    return total_combinations, file_size_bytes

password_length = 7
total_combinations, file_size_bytes = brute_force('full_rollnumber.txt', password_length)
print(f"Total combinations: {total_combinations}")
print(f"File size: {file_size_bytes} bytes")
