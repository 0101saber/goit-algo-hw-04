from task1 import total_salary
from task2 import get_cats_info
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # first task
    total, average = total_salary("texts/salary.txt")
    print('First task')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    print(20 * '#')
    
    # second task
    cats_info = get_cats_info("texts/cats.txt")
    print('Second task')
    print(cats_info)
    print(20 * '#')
