def display_routes(routes):
    """
    Отобразить список маршрутов.
    """
    if routes:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^30} | {:^20} | {:^8} |'.format(
                "Начало",
                "Конец",
                "Номер"
            )
        )
        print(line)
        for route in routes:
            print(
                '| {:<30} | {:<20} | {:>8} |'.format(
                    route.get('начальный пункт', ''),
                    route.get('конечный пункт', ''),
                    route.get('номер маршрута', '')
                )
            )
        print(line)
    else:
        print("Список маршрутов пуст.")