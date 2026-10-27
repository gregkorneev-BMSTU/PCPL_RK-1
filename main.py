from operator import itemgetter


class DataRow:
    """Строка данных."""

    def __init__(self, id, name, value_count, table_id):
        self.id = id
        self.name = name
        self.value_count = value_count
        self.table_id = table_id


class DataTable:
    """Таблица данных."""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class DataRowTable:
    """Связь строк и таблиц для отношения многие-ко-многим."""

    def __init__(self, row_id, table_id):
        self.row_id = row_id
        self.table_id = table_id


tables = [
    DataTable(1, "Основная таблица"),
    DataTable(2, "Архив"),
    DataTable(3, "Справочник"),
]

data_rows = [
    DataRow(1, "Альфа", 7, 1),
    DataRow(2, "Бета", 3, 1),
    DataRow(3, "Альманах", 5, 2),
    DataRow(4, "Гамма", 2, 2),
    DataRow(5, "Атрибут", 9, 3),
]

data_row_tables = [
    DataRowTable(1, 1),
    DataRowTable(1, 3),
    DataRowTable(2, 1),
    DataRowTable(3, 2),
    DataRowTable(3, 1),
    DataRowTable(4, 2),
    DataRowTable(5, 3),
    DataRowTable(5, 2),
]


def main():
    """Выполнение запросов варианта В."""

    # Соединение данных один-ко-многим по полю table_id.
    one_to_many = [
        (row.name, row.value_count, table.name)
        for table in tables
        for row in data_rows
        if row.table_id == table.id
    ]

    # Соединение данных многие-ко-многим через класс DataRowTable.
    many_to_many = []
    for link in data_row_tables:
        for row in data_rows:
            if row.id == link.row_id:
                for table in tables:
                    if table.id == link.table_id:
                        many_to_many.append((row.name, table.name))

    print("Задание В1")
    res_11 = [row for row in one_to_many if row[0].startswith("А")]
    print(res_11)

    print("\nЗадание В2")
    min_values_by_table = []
    for table in tables:
        table_rows = [row for row in one_to_many if row[2] == table.name]
        if table_rows:
            values = [row[1] for row in table_rows]
            min_value = min(values)
            min_values_by_table.append((table.name, min_value))
    print(sorted(min_values_by_table, key=itemgetter(1)))

    print("\nЗадание В3")
    print(sorted(many_to_many, key=itemgetter(0)))


if __name__ == "__main__":
    main()
