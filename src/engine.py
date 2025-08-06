import src.db_tools as db


def game_engine(game_type: str) -> list:
    all_values = []
    row_results_1 = []
    row_results_2 = []
    row_results_3 = []
    row_results_4 = []

    data_storage = db.get_stored_values(game_type)

    for value in data_storage:
        valueList = value[3:]
        for number in valueList:
            all_values.append(number)

    all_values.sort()

    if game_type == "short":
        for number in range(1, 40):
            choice = all_values.count(number)

            if choice >= 5:
                row_results_1.append(str(number))
            elif choice == 4:
                row_results_2.append(str(number))
            elif choice == 3:
                row_results_3.append(str(number))
            elif choice == 2:
                row_results_4.append(str(number))

            choice = 0
    else:
        for number in range(1, 57):
            choice = all_values.count(number)

            if choice >= 6:
                row_results_1.append(str(number))
            elif choice == 5:
                row_results_2.append(str(number))
            elif choice == 4:
                row_results_3.append(str(number))
            elif choice == 3:
                row_results_4.append(str(number))

            choice = 0

        return row_results_1, row_results_2, row_results_3, row_results_4
