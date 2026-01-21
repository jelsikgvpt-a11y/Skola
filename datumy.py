def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    
    return h


def get_day_name(h):
    
    days = ["Sobota", "Nedeľa", "Pondelok", "Utorok", "Streda", "Štvrtok", "Piatok"]
    return days[h]


day = int(input("Deň: "))
month = int(input("Mesiac: "))
year = int(input("Rok: "))

h = zellers_congruence(day, month, year)
day_name = get_day_name(h)

print(f"{day}.{month}.{year} je: {day_name}")

if __name__ == "__main__":
    day = int(input("Deň: "))
    month = int(input("Mesiac: "))
    year = int(input("Rok: "))

    h = zellers_congruence(day, month, year)
    day_name = get_day_name(h)

    print(f"{day}.{month}.{year} je: {day_name}")