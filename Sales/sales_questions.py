import os

with open('sales_data.txt', 'r') as dataSet:
    arry_list = []
    for word in dataSet:
        arry_list.append(word.split())
    
def main():
    # get_total_amount()
    # highest_feb_city_sales()
    cash_people()

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

    
main()