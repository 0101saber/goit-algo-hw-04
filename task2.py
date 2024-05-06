def get_cats_info(path) -> list:
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                cat = line.split(',')
                cats_info.append({"id": cat[0], "name": cat[1], "age": cat[2].rstrip('\n')})
        return cats_info
    except FileNotFoundError:
        print(f"No such file or directory: '{path}'")
