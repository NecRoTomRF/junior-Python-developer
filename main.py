from src import *

if __name__ == "__main__":
    records = ["Иван: 30", "Коля: 40", "Толя: 60", "Оля: abs", "А: 99", ": 21"]
    print(process_grades(records))
    print(longest_increasing_streak([1, 3, 2, 5, 8, 4, 7]))
