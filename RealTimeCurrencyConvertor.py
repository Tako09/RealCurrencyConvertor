# https://pypi.org/project/forex-python/
# https://forex-python.readthedocs.io/en/latest/usage.html --Currency Rtes
# https://forex-python.readthedocs.io/en/latest/usage.html
'''
1. List all exchange rates
2. BitCoin price for all currencies
3. Converting the amount into BitCoins
4. Get historical rates for any day since 1999
5. The conversion rate for a currency (ex; USD to INR)
6. Convert the amount from one currency to another. (‘USD $ 10’ to INR)
7. Currency symbols
8. Names of currencies
'''
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
import datetime as dt
bc = BtcConverter()
cr = CurrencyRates()
cc = CurrencyCodes()

# main method used to be more readable
def main():
    while True:
        ans = question()
        print()
        if ans == 'Q':
            break
        elif ans == 'L':
            Show_Currency_Rate(see_all=True)
        elif ans == 'B':
            Show_Bitcoin_price()
        elif ans == 'H':
            Show_Currency_Rate(historical=True)
        elif ans == 'R':
            Show_Currency_Rate()  
        elif ans == 'C':
            Currrency_Converter()
        elif ans == 'S':
            Show_Currency_Symbol()

    print('End the program. Thank you!')

# prompt user to input 
def question():
    q = '''
    Enter L to list all currency rates of a currency:
    Enter B to check BitCoin price for a currency:
    Enter H to get historical rates since 1999 from one to one another: 
    Enter R to get the conversion rate from one to one another:
    Enter C to convert the currency into one another: 
    Enter S to check the symbol and name of a currency:
    Enter Q to quit:
    '''
    print(q)
    # justification ref -> https://note.nkmk.me/python-rjust-center-ljust/
    ans = str(input('--'.rjust(6))).upper()
    return ans

# Bitcoin price
def Show_Bitcoin_price():
    currency = str(input('Enter a currency: ')).upper()
    #if historical == True:
    #    y = input('Enter a year, e.x. YYYY: ')
    #    m = input('Enter a month, e.x. MM: ')
    #    d = input('Enter a day, e.x. DD: ')
    #    date = dt.datetime(y, m, d)
    #    rate = cr.get_rate(from_currency, to_currency, date)
    price = bc.get_latest_price(currency)
    print('One Bitcoin in {}: {}'.format(currency, price))

# Show currency rates
def Show_Currency_Rate(historical=False, see_all=False):
    if see_all == False:
        from_currency = str(input('Conversion rate from: ')).upper()
        to_currency = str(input('to: ')).upper()
        if historical == True:
            y = input('Enter a year, e.x. YYYY: ')
            m = input('Enter a month, e.x. MM: ')
            d = input('Enter a day, e.x. DD: ')
            date = dt.datetime(y, m, d)
            rate = cr.get_rate(from_currency, to_currency, date)
            return
        else: 
            rate = cr.get_rate(from_currency, to_currency)
            print('from {} to {}: {}'.format(from_currency, to_currency, rate))
            return
    else:
        currency = str(input('Enter a currency: ')).upper()
        rate = cr.get_rates(currency)
        print('\n--{}--'.format(currency))
        for key, value in rate.items():
            print('{}: {}'.format(key, value))
        return

# Currency Converter
def Currrency_Converter():
    amount = int(input('Enter the amount: '))
    from_currency = str(input('From Currency: ').upper())
    to_currency = str(input('To Currency: ').upper())
    print(from_currency, ' To ', to_currency, amount)
    # round method for float type
    result = round(cr.convert(from_currency, to_currency, amount), 2)
    print('Amount in {}: {}'.format(to_currency, result))

# Show all symbols
def Show_Currency_Symbol():
    code = str(input('Enter a currency code: ')).upper()
    symbol = cc.get_symbol(code)
    name = cc.get_currency_name(code)
    print('Name: {}\nSymbol: {}'.format(name, symbol))

if __name__ == '__main__':
    main()