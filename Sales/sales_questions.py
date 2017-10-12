import os

with open('sales_data.txt', 'r') as dataSet:
    arry_list = []
    for word in dataSet:
        arry_list.append(word.split())
    
def main():
    # get_total_amount()
    # highest_feb_city_sales()
    # cash_people()
    # oakland_payment_type()
    # get_cities(filter_months("4/"))
    # print("Miami")
    # highest_value(filter_city("Miami"))
    # print("Philadelphia")
    # highest_value(filter_city("Philadelphia"))
    # print("Oakland")
    # highest_value(filter_city("Oakland"))
    # print("Boston")
    # highest_value(filter_city("Boston"))
    # print("Kansas")
    # highest_value(filter_city("Kansas"))
    # print("NYC")
    # highest_value(filter_city("NYC"))
    # print("Ocala")
    # highest_value(filter_city("Ocala"))
    # print("LA")
    # highest_value(filter_city("LA"))
    # print("Palo")
    # highest_value(filter_city("Palo"))
    # print("SF")
    # highest_value(filter_city("SF"))
    # credit_card_type()
    baseball_card_type()

    
    

def get_total_amount():
    add_price_list = []
    for item_set in arry_list:
        for single_word in item_set:
            for digit in single_word:
                if "$" in digit:
                    price_list = list(single_word)
                    price_list.remove("$")
                    no_dollar_sign = ''.join(price_list)
                    add_price_list.append(no_dollar_sign)
    rounded_amount = round(sum(map(float, add_price_list)),2)
    total_amount = '$' + str(rounded_amount)
    print(total_amount)    

def highest_feb_city_sales():
    all_febs = []
    all_sets_with_feb = []
    all_feb_prices = []
    #get all febs
    for item_set in arry_list:
        for single_word in item_set:
            if "12/" in single_word:
                pass
            elif "2/" in single_word:
                all_febs.append(single_word)
                all_sets_with_feb.append(item_set)
                # Making sure all index is price amount
                if "$" in item_set[3]:
                    all_feb_prices.append(item_set[3])
                    max_price = max(all_feb_prices)
                else: 
                    pass
            else:
                pass
    # Check which set's price amount match with max_price
    for feb_set in all_sets_with_feb:
        for feb_set_price in feb_set:
            if feb_set_price == max_price:
                best_location = feb_set[0]
                print(best_location)

    
def cash_people():
    all_cash = []
    no_dollar_sign_cash_list = []
    for item_set in arry_list:
        for single_word in item_set:
            if 'Cash' == single_word:
                if len(item_set) == 4:
                    all_cash.append(item_set[3])
                elif len(item_set) == 5:
                     all_cash.append(item_set[4])
    for price in all_cash:
        no_dollar_sign_cash = price.replace('$', '')
        no_dollar_sign_cash_list.append(no_dollar_sign_cash)
    total_cash_amount = round(sum(map(float, no_dollar_sign_cash_list)),2)
    print("$" + str(total_cash_amount))

def oakland_payment_type():
    all_oakland = []
    all_oakland_march = []
    cash = 0
    credit = 0
    check = 0
    cards = 0
    # Filter for Oakland
    for item_set in arry_list:
        for single_word in item_set:
            if 'Oakland' == single_word:
                all_oakland.append(item_set)   

    # Filter for March
    for marches in all_oakland:
        if '3/' in marches[1]:
            all_oakland_march.append(marches)

    # Count payment type occurrence 
    for payment in all_oakland_march:
        if len(payment) == 4:
            if payment[2] == 'Cash':
                cash = cash + 1
            elif payment[2] == 'Credit':
                credit = credit + 1
            elif payment[2] == 'Check':
                check = check + 1
            elif payment[2] == 'Cards':
                cards = cards + 1
        elif len(payment) == 5:
            if payment[3] == 'Cards':
                cards = cards + 1
    print(cash, "cash")
    print(credit, "credit")
    print(check, "check")
    print(cards, "card")
# Helper Methods ============================================================================================================
def filter_months(month):
    month_list = []
    for item_set in arry_list:
        for single_word in item_set:
            if month in single_word:
                month_list.append(item_set)   
    return month_list

def get_cities(month_list):
    all_cities = []
    for city_set in month_list:
        all_cities.append(city_set[0])
    filtered_cities = list(set(all_cities))
    return filtered_cities

def filter_city(city):
    filtered_city = []
    for item_set in arry_list:
        if city in item_set:
            filtered_city.append(item_set)

    return filtered_city

def highest_value(filtered_city):
    all_prices = []
    float_prices = []
    for value in filtered_city:
        if len(value) == 4:
            all_prices.append(value[3])
        elif len(value) == 5:
            all_prices.append(value[4])

    for price in all_prices:
        digits = list(price)
        digits.remove('$')
        digits = ''.join(digits)
        float_prices.append(digits)

    highest_total_value = round(sum(map(float, float_prices)),2)
    print(highest_total_value)

def credit_card_type():
    all_credit_users = []
    all_prices = []
    all_prices_no_dollar = []
    for item_set in arry_list:
        if item_set[2] == 'Credit':
            all_credit_users.append(item_set)
    
    for i in all_credit_users:
        all_prices.append(i[3])

    for digit in all_prices:
        amount = list(digit)
        del amount[0]
        add_price = ''.join(amount)
        all_prices_no_dollar.append(add_price)
    total_price = round(sum(map(float, all_prices_no_dollar)),2)
    print('$' + str(round(total_price/len(all_credit_users),2)), "is the average sales for credit card purchases")
    

def baseball_card_type():
    baseball_card = []
    cards = 0
    # Filter for cards
    for item_set in arry_list:
        for single_word in item_set:
            if 'Cards' == single_word:
                cards = cards + 1
    print("Baseball cards were used", cards, "many times for bartering")

main()