def select_routes(routes, name_punct):
    """
    Выбрать маршруты с заданным пунктом отправления или прибытия.
    """
    selected = []
    for route in routes:
        if str(route['номер маршрута']) == name_punct:
            selected.append(route)
    return selected