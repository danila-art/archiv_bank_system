import random
def  number() :
    a = "0123456789"
    b = list(a) 
    random. shuffle(b) 
    c = "".join([random.choice(b)  for x in range(16) ])
    return c 
    # print(f"ваш номер карты - {c}") 

def  number_1() :
    a = "0123456789"
    b = list(a) 
    random. shuffle(b) 
    c = "".join([random.choice(b)  for x in range(3) ])
    return c 
    # print(f"ваш CVC код - {c}") 

def  number_2() :
    a = "0123456789"
    b = list(a) 
    random. shuffle(b) 
    c = "".join([random.choice(b)  for x in range(4) ])
    return c 
    # print(f"дата обслуживания- {c}")

def main_number(card, pers):
    number_card = number()
    number_cvc = number_1()
    date = number_2()
    balance = 0
    type_card = card
    dict_card = {
        "personal_account": pers,
        "number_card" : number_card,        
        "number_cvc" : number_cvc,    
        "date" : date,    
        "balance" : balance,    
        "type_card" : type_card        
    }
    return dict_card