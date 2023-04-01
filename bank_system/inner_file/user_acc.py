import module_csv
import time
import main
import konstantin_code as code
import add_credit


class user_class:
    surname = None
    name = None
    patronomyk = None
    seria = None
    number = None
    date_of_birth = None
    login = None
    password = None
    personal_account = None
    card = None
    rang = None

    def __init__(self, arr_user):
        self.surname = arr_user[0]
        self.name = arr_user[1]
        self.patronomyk = arr_user[2]
        self.seria = arr_user[3]
        self.number = arr_user[4]
        self.date_of_birth = arr_user[5]
        self.login = arr_user[6]
        self.password = arr_user[7]
        self.personal_account = arr_user[8]
        self.card = arr_user[9]
        self.rang = arr_user[10]

    def hello_user(self):
        print(f"Добро пожаловать, {self.name} {self.patronomyk}")
        print("Производится выгрузка данных -->")
        point = "-"*20
        print(f"{point*3}\nФамилия: {self.surname} | Имя: {self.name} | Отчество: {self.patronomyk}\n{point*3}\nПаспортные данные: {self.seria}-{self.number}\tДата Рождения: {self.date_of_birth}\n{point}\nЛицевой счет -> {self.personal_account}\n{point}")
        read_all_card = module_csv.read_card() 
        i = 0
        for element in read_all_card:
            if(element['personal_account'] == self.personal_account):
                print(f"Номер карты: {element['number_card']}\nCvC - код : {element['number_cvc']} | Дата: {element['date']}\nБаланс: {element['balance']} | Тип карты: {element['type_card']}")
                i +=1
        if(i == 0):
            print("Карты: нет")
    def system_managment(self):
        arr = [
            "| 1 <-- Получить дебетовую карту |",
            "| 2 <-- Получить кредитную карту |",
            "| 3 <-- Получить кредит наличным |",
            "| 0 <-- Вернуться в главное меню |"
        ]
        for el_arr in arr:
            print("-"*len(el_arr))
            print(el_arr)
            print("-"*len(el_arr))
            time.sleep(.5)

        while True:
            select_operation = input("Выберете что хотите сделать: ")
            if (select_operation == ""):
                print("Вы ничего не указали, повторите ещё раз...")
            elif (select_operation == '1'):
                time.sleep(.5)
                print("Формирую пакет ваших данных для оформления услуги -> ")
                # Код формирования dict_user
                dict_user = self.create_dict_user() # Данные для отправки 
                time.sleep(1)
                print(f"Фамилия: {dict_user['surname']} | Имя: {dict_user['name']} | Отчество: {dict_user['patronomyk']}\nПаспорт: {dict_user['pasport']} | Дата: {dict_user['date_of_birth']} | Лицевой счет: {dict_user['personal_account']} |")
                # <- Функция добавления дебетовой карты
                card = "дебетовая"
                card = code.main_number(card, self.personal_account)
                print(f"Ваша карта сформирована:\nНомер карты: {card['number_card']}\nCvC - код : {card['number_cvc']} | Дата: {card['date']}\nБаланс: {card['balance']} | Тип карты: {card['type_card']}")
                module_csv.append_card(card)
                time.sleep(2)
                print("Карта успешно добавлена...")
                time.sleep(1)
                self.system_managment()
                pass
            elif (select_operation == '2'):
                time.sleep(.5)
                print("Формирую пакет ваших данных для оформления услуги -> ")
                # Код формирования dict_user
                dict_user = self.create_dict_user() # Данные для отправки
                time.sleep(1)
                print(f"Фамилия: {dict_user['surname']} | Имя: {dict_user['name']} | Отчество: {dict_user['patronomyk']}\nПаспорт: {dict_user['pasport']} | Дата: {dict_user['date_of_birth']} | Лицевой счет: {dict_user['personal_account']} |")
                # <- Функция добавления кредитной карты
                card = "Кредитная"
                card = code.main_number(card, self.personal_account)
                print(f"Ваша карта сформирована:\nНомер карты: {card['number_card']}\nCvC - код : {card['number_cvc']} | Дата: {card['date']}\nБаланс: {card['balance']} | Тип карты: {card['type_card']}")
                module_csv.append_card(card)
                time.sleep(2)
                print("Карта успешно добавлена...")
                time.sleep(1)
                self.system_managment()

                pass
            elif (select_operation == '3'):
                time.sleep(.5)
                print("Формирую пакет ваших данных для оформления услуги -> ")
                # Код формирования dict_user
                dict_user = self.create_dict_user() # Данные для отправки
                time.sleep(1)
                print(f"Фамилия: {dict_user['surname']} | Имя: {dict_user['name']} | Отчество: {dict_user['patronomyk']}\nПаспорт: {dict_user['pasport']} | Дата: {dict_user['date_of_birth']} | Лицевой счет: {dict_user['personal_account']} |")
                # <- Функция выдачи кредитов
                add_credit.add_credit(dict_user)
                pass
            elif (select_operation == '0'):
                print("Возвращаюсь в стартовое меню...")
                time.sleep(1)
                main.main()
            else:
                print("Вы ввели несуществующее значение, попробуйте ещё раз")

    def create_dict_user(self):  # Функция формировани документов для отправки
        dict_user = {
            "surname": self.surname,
            "name": self.name,
            "patronomyk": self.patronomyk,
            "pasport": str(self.seria)+"-"+str(self.number),
            "date_of_birth": self.date_of_birth,
            "personal_account": self.personal_account,
            "card": self.card
        }
        return dict_user
# Главная функция управления ->


def select_user(get_login, get_password):
    arr_users = module_csv.read_csv_user()
    create_arr_user = []
    for el_user in arr_users:
        if (el_user['login'] == get_login and el_user['password'] == get_password):
            print("Пользователь найден -->")
            for key, value in el_user.items():
                create_arr_user.append(value)
    user = user_class(create_arr_user)
    user.hello_user()
    user.system_managment()
