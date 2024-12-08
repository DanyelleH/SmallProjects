'''
    PSEUDOCODE
        1. Determine the amount of change due
        2. create a variable holding currency values, sorted from highest value 
            to lowest value, to look through and grab bill values while decrementing 
            the total change due.
        3. store a list of the actual change due, formatted into a string.
        4. return the values in a formatted string containing item cost, amount 
        paid, and the number of each bill to make the value.
'''


def optimal_change(item_cost, amount_paid):
    '''
    input : int/float , int/float
    output: string
    edgecases: plural values, exact payment, under payment.

    '''
    total_change = round(amount_paid - item_cost,2)
    if amount_paid < item_cost:
        return "Hey Guy, I need more money!"
    
    if total_change == 0:
        return " No change due"

    change_due = bill_breakdown(total_change)
    
    #list contains a dictionary of the count of bill type (key) and bill type(value): 
    # Key(billtype), Value(bill_count)
    formatted_change_list = [f"{count} {key}" for key,count in change_due.items()]

    if len(formatted_change_list) > 1: # if there are multiple items in the list, add an " and" between the last component and the value before it.
        formatted_change = ", ".join(formatted_change_list[:-1])+ f", and {formatted_change_list[-1]}"
    else:
        formatted_change = formatted_change_list[0]
    
    return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {formatted_change}."


def bill_breakdown(amount):
    # convert dollars to cents in order to avoid floating- point issues.
    amount_in_cents = int(round(amount *100))
    
    money_values = {
        10000: '$100 bill',
        5000: '$50 bill',
        2000: '$20 bill',
        1000: '$10 bill',
        500: '$5 bill',
        100: '$1 bill',
        25: 'quarter',
        10: 'dime',
        5: 'nickel',
        1: 'penny'
    }
    change_count={}
  
    for value in money_values:
        if value<=amount_in_cents:
            bill_count =amount_in_cents // value
            amount_in_cents -= bill_count * value

        # making plural versions of values when necessary
            if bill_count == 1:
                change_count[money_values[value]] = bill_count
            else: 
                if money_values[value] == 'penny':
                    plural_name = "pennies"
                else:
                    plural_name = money_values[value] + 's'
                change_count[plural_name] = int(bill_count)
                # in the new dictionary, the value( bill name) becomes the new key, the new value is the count of that bill
            
    return change_count