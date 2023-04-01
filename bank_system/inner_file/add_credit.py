# import random
# import datetime

# def add_credit():
#     pass

# def number():
#     a = "123456789"
#     er = list(a)
#     random.shuffle(er)
#     yt = "".join([random.choice(er) for x in range(16)])
#     print(f"ваш номер карты - {yt}")
#     return yt


# def number_1():
#     print("Хотите взять кредит под 10.5% годовых? \nда/нет?")
#     i = input("")
#     if i == "да":
#         b = input("Какую сумму вы хотите взять в кредит?\n")
#         a = input("На сколько месецев?\n")
#         r = "10.5"
#         year = int(b) // 12
#         print(f"Годов: {year}")
#         summ = (int(b) / 100) * float(r)
#         total_credit = int(a) + int(summ)
#         print(f"Сумма переплаты: {summ}")
#         print(f"Итоговый кредит: {total_credit}")
#         month_summa = int(total_credit) / a
#         arr_data_credit = [summ, total_credit, a, month_summa]
#         return arr_data_credit


# def data():

#     a = "0123456789"
#     b = list(a)
#     random.shuffle(b)
#     c = "".join([random.choice(b) for x in range(3)])
#     print(f"ваш CVC код - {c}")
#     return c

# # def chet():
# #     a = "0123456789"
# #     d = list(a)
# #     random.shuffle(d)
# #     c = "".join([random.choice(d) for x in range(11)])
# #     e = "qwertyuiopasdfghjklzxcvbnm".upper()
# #     b = list(e)
# #     random.shuffle(b)
# #     f = "".join([random.choice(b) for x in range(1)])
# #     print(f"ваш номер лицевого счета - {f}-{c}")
# def  number_2() :
#     a = "0123456789"
#     b = list(a) 
#     random. shuffle(b) 
#     c = "".join([random.choice(b)  for x in range(2) ])
#     h = "0123456789"
#     k = list(a) 
#     random. shuffle(b) 
#     g = "".join([random.choice(b)  for x in range(2) ])
#     print(f"{c}/{g}")
#     return c+g

#     return c 
#     # print(f"дата обслуживания- {c}")

# if __name__ == '__main__':
#     number()
#     data()
#     number_1()
#     number_2()