def get_cats_info(path) -> list:
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readline():
                cats_info.append({"id": line.split(',')[0], "name": line.split(',')[0], "age": line.split(',')[0]})
        return cats_info
    except FileNotFoundError:
        print(f"No such file or directory: '{path}'")
