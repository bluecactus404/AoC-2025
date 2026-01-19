from pathlib import Path
from collections import namedtuple


Position = namedtuple('Position', ['row_index', 'column_index'])


def get_input_as_array(file_name:str)->list[list[str]]:
    PATH = Path(file_name)
    floor = []
    with open(PATH, 'r') as f:
        lines = f.readlines()
        for line in lines:
            floor.append(list(line.strip()))
    return floor

def is_paper(floor:list[list[str]], position:Position)->bool:
    if floor[position.row_index][position.column_index] == '@':
        return True
    else:
        return False


def is_tile_accessable(floor:list[list[str]], position:Position)->bool:
    '''
    For a tile to be accessable must have a roll of paper at the center and less than 4 rolls of paper immediately surrounding 
    said tile
    '''
    papers = 0
    for i in range(3):
        for j in range(3):
            current_row_index = position.row_index-1+i
            current_column_index = position.column_index -1 + j
            if not (i == 1 and j == 1) and 0 <= current_column_index < len(floor[0]) and 0 <= current_row_index < len(floor):
                if is_paper(floor, Position(current_row_index, current_column_index)):
                    papers += 1
    if papers >= 4:
        return False
    else:
        return True
    
def solve_part_1(floor:list[list[str]])->int:
    accesable_count = 0
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            if is_paper(floor, Position(i, j)) and is_tile_accessable(floor, Position(i, j)):
                accesable_count += 1

    return accesable_count


def get_array_of_rolls_to_be_removed(floor:list[list[str]])->list[Position]:
    rolls_to_be_removed = []
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            current_position = Position(i,j)
            if is_paper(floor, current_position) and is_tile_accessable(floor, current_position):
                rolls_to_be_removed.append(current_position)

    return rolls_to_be_removed




def solve_part_2(floor:list[list[str]])->int:
    total_removed_rolls = 0
    while True:
        rolls_to_be_removed = get_array_of_rolls_to_be_removed(floor)
        total_removed_rolls += len(rolls_to_be_removed)
        if len(rolls_to_be_removed) == 0:
            break

        for i in rolls_to_be_removed:
            floor[i.row_index][i.column_index] = '.'

    return total_removed_rolls


def run(file_name:str):
    floor = get_input_as_array(file_name)
    solution_1 = solve_part_1(floor)
    print(f'Solution to p1: {solution_1}')
    solution_2 = solve_part_2(floor)
    print(f'Solution to p2: {solution_2}')


if __name__ == '__main__':
    run('4.txt')