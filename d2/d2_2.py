


def get_ranges_from_file(file_name:str)->list[list[int]]:
    ranges = []
    with open(file_name, 'r') as f:
        lines = f.readline()
        f.close()
        for i in lines.split(','):
            nums = i.split('-')
            ranges.append([int(nums[0]), int(nums[1])])
    return ranges


def divide_into_parts(num_str:str, pattern_len:int)->list[str]:
    lst = []
    for i in range(len(num_str)//pattern_len):
        lst.append(num_str[i*pattern_len:(i+1)*pattern_len])
    return lst



def is_invalid(num:int)->bool:
    str_num = str(num)
    for pattern_length in range(1, len(str_num), 1):
        if len(str_num) % pattern_length != 0:
            continue
        elif pattern_length > len(str_num)/ 2:
            return False
        parts = divide_into_parts(str_num, pattern_length)
        
        matches:bool = True
        for i in parts:
            if i != str_num[0:pattern_length]:
                matches = False
                break
    
        if matches:
            return True

    return False




def solve(ranges:list[list[int]])->int:
    invalid_sum = 0
    for i in ranges:
        num = i[0]
        while num <= i[1]:
            if is_invalid(num):
                invalid_sum += num
                # print(num)
            num += 1
    return invalid_sum


if __name__ == '__main__':
    ranges = get_ranges_from_file('2.txt')
    print(solve(ranges))