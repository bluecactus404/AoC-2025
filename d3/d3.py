import math



def get_banks(file_name:str)->list[list[int]]:
    battery_banks= []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        f.close()
        for line in lines:
            arr = get_int_arr_from_str(line.strip())
            battery_banks.append(arr)
    return battery_banks


def find_max_index(nums:list[int])->int:
    # returns index of maximum integer
    max = nums[0]
    number_index = 0
    for index, num in enumerate(nums):
        if num > max:
            number_index = index
            max = num
    return number_index

def get_int_arr_from_str(nums:str)->list[int]:
    number_array = []
    for num in list(nums):
        number_array.append(int(num))
    return number_array


def part_one_solve(battery_banks:list[list[int]])->int:
    # 1) find largest number that is not at index -1
    # 2) find next largest number after the index of the first largest one
    output_joltage = 0
    for bank in battery_banks:
        num_1_index = find_max_index(bank[:-1])
        num_2_index = find_max_index(bank[num_1_index+1:])
        joltage = bank[num_1_index] * 10 + bank[num_2_index+num_1_index+1]
        output_joltage += joltage
    return output_joltage


# functions for part 2


def int_arr_to_num(arr:list[int])->int:
    number = 0
    length = len(arr)
    for index, num in enumerate(arr):
        number += num * int(math.pow(10, length-index))
    return 0



def part_two_solve(battery_banks:list[list[int]])->int:
    # 1) find largest number between index 0 and -11, 
    # then the next largest number between largest num index +1 and -10 (non inclusive)
    # repeat
    sum_joltage = 0
    for bank in battery_banks:
        number = 0
        previous_index = -1

        for i in range(11, 0, -1):
            # if remaining number of elements == number of 
            if i+1 == len(bank) - new_index:
                pass

            current_range = bank[previous_index+1:-i]
            print(current_range)
            new_index = find_max_index(current_range) + previous_index+1
            

            new_number = bank[new_index]
            print(new_number)
            number += int(math.pow(10, i+1)) * new_number
            previous_index = new_index


        sum_joltage += number
    return sum_joltage



if __name__ == '__main__':
    battery_banks = get_banks('t.txt')
    print(f'part 1: {part_one_solve(battery_banks)}')
    print(f'part 2: {part_two_solve(battery_banks)}')