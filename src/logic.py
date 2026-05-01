import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="py_log.log",
    filemode="w",
    encoding="utf_8",
    format="%(asctime)s %(levelname)s %(message)s",
)


def process_grades(records: list[str]) -> dict:
    """Обрабатывает список строк. Длина минимального валидного имени - 2 символа"""

    logging.info(f"Старт функции: process_grades(\n{records})")

    result = {"valid_count": 0, "average": [], "passed": [], "skipped": 0}
    for row in records:
        name, assessment = row.split(": ")
        try:
            assessment = int(assessment)
            if not (name.isalpha() and len(name) > 2):
                result["skipped"] += 1
                continue
            if assessment >= 60:
                result["passed"].append(name)
            result["average"].append(assessment)
            result["valid_count"] += 1
        except ValueError as e:

            logging.info(
                f"Ошибка {e} значение {assessment} не может быть преобразовано к целочисленному"
            )

            result["skipped"] += 1
            continue
    if len(result["average"]) == 0:
        result["average"] = 0.0
    else:
        result["average"] = round(
            sum(result["average"]) / len(result["average"]), 1
        )

    sorted_passed = set(result["passed"])
    result["passed"] = sorted(sorted_passed)
    logging.info(
        f"Результат отработки функции: longest_increasing_streak(\n{result})"
    )

    return result


def longest_increasing_streak(nums: list[int]) -> dict:
    """Находит самую длинную непрерывную подпоследовательность"""
    logging.info(f"Старт функции: longest_increasing_streak(\n{nums})")
    result = {"length": 0, "streak": []}
    if (len_list := len(nums)) <= 1:
        logging.info(
            f"Результат отработки функции: longest_increasing_streak(\n{nums})"
        )
        return result
    max_len = 0
    max_streak = [nums[0]]
    counter = 1
    new_streak = [nums[0]]
    for i in range(1, len_list):
        if nums[i - 1] < nums[i]:
            counter += 1
            new_streak.append(nums[i])
        else:
            logging.debug(f"Текущая последовательность: {new_streak}")
            if max_len < counter:
                max_len = counter
                max_streak = new_streak
            counter = 1
            new_streak = [nums[i]]
    logging.debug(f"Текущая последовательность: {new_streak}")
    if max_len < counter:
        max_len = counter
        max_streak = new_streak

    if max_len != 1:
        result = {"length": max_len, "streak": max_streak}
    logging.info(
        f"Результат отработки функции: longest_increasing_streak(\n{nums})"
    )
    return result
