import sys

try:
    month = int(input())
    months_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(months_dict.get(month, "Mês inválido"))
except ValueError:
    print("Por favor, insira um número válido.")