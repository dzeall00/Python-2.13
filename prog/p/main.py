import sys
import bisect
import re

from p.select_routes import select_routes
from p.get_route import get_route
from p.display_routes import display_routes


def main():
    """
    Главная функция программы.
    """
    routes = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            route = get_route()
            if route not in routes:
                bisect.insort(
                    routes, route, key=lambda item: item.get(
                        'номер маршрута'
                    )
                )
            else:
                print("Данный маршрут уже добавлен.")

        elif command == 'list':
            display_routes(routes)

        elif (m := re.match(r'select (.+)', command)):
            name_punct = m.group(1)
            selected = select_routes(routes, name_punct)
            display_routes(selected)

        elif command == 'help':
            print("Список команд:")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select <номер маршрута> - запросить маршруты, которые имеют данный номер")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
