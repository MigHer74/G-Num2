import src.db_tools as db


def game_engine(game_type):
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
