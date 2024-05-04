def total_salary(path) -> tuple:
    try:
        with open(path, "r") as fh:
            salary = [int(el.split(',')[1]) for el in fh.readlines()]
            return sum(salary), sum(salary) / len(salary)
    except FileNotFoundError:
        print(f"No such file or directory: '{path}'")
