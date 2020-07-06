"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Homework 3 - Mortgage Calculations

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""


def fill(text, cols=60):
    return f'{text:^{cols}}'


def pad(text, char='-', n=10):
    n_chars = char * n
    return f'{n_chars} {text} {n_chars}'


def title(text):
    return fill(pad(text))


def input_type(text, type, is_positive=False):
    value = None
    while value is None:
        try:
            i = input(text)
            value = type(i)
        except ValueError:
            print(f'Wrong value entered. Please input type {type}')
            value = None
        if is_positive:
            if value <= 0:
                print(f'The value entered ({value}) is not positive. Please reenter a positive value.')
                value = None
    return value


def get_inputs():
    print(title('Mortgage Report'))
    house_price = input_type('Enter house purchase price: ', int, True)
    while True:
        down_payment = input_type('Enter down payment: ', int, True)
        if down_payment < house_price:
            break
        else:
            print('The down payment entered is greater than the house price. Please try again.')

    interest_rate = input_type('Enter interest rate (without the % sign): ', float, True)
    mortgage_term = input_type('Enter term of mortgage in years: ', int, True)
    tax_rate = input_type('Enter tax rate on home (without the % sign): ', float, True)
    home_insurance = input_type('Enter home insurance (per year): ', float, True)
    return house_price, down_payment, interest_rate, mortgage_term, tax_rate, home_insurance


def main():
    house_price, down_payment, interest_rate, mortgage_term, tax_rate, home_insurance = get_inputs()
    loan_amount = house_price - down_payment

    print(title('Loan Summary'))
    print(f'{"House Purchase Price:": <24}${house_price: >13,.2f}')
    print(
        f'{"Down Payment:": <24}${down_payment: >13,.2f} ({int(down_payment / house_price * 100)}% of purchase price)')
    print(f'{"Loan Amount:": <24}${loan_amount: >13,.2f}')
    print(f'{"Loan Term:": <24}{mortgage_term} years ({mortgage_term * 12} months)')
    print(f'{"Interest Rate:": <24}{interest_rate:.3f}%')
    print(f'{"Tax Rate:": <24}{tax_rate:.2f}%/year')
    print(f'{"Home Insurance:": <24}${home_insurance:.2f}/year')

    monthly_interest = 0.01 * interest_rate / 12
    num_payments = mortgage_term * 12
    loan_amount = house_price - down_payment
    monthly_payments = (loan_amount * monthly_interest) / (1 - (1 / ((1 + monthly_interest) ** num_payments)))
    monthly_insurance = home_insurance / 12
    monthly_tax = house_price * tax_rate / 12

    print(title('Monthly Payment Breakdown'))
    print(f'{"Principal and Interest:": <24}${monthly_payments: >10,.2f}/month')
    print(f'{"Monthly Tax:": <24}${monthly_tax: >10,.2f}/month')
    print(f'{"Monthly Insurance:": <24}${monthly_insurance: >10,.2f}/month')
    total = monthly_payments + monthly_tax + monthly_insurance
    print(f'{"Total:": <24}${total: >10,.2f}/month')

    print(title('Monthly Payment Breakdown'))

    total_cost = mortgage_term * 12 * total
    total_interest = loan_amount - total_cost
    print(f'By the end of the {mortgage_term}-year period, you would pay ${total_cost:.2f}',
          f'in total payments (${loan_amount:.2f} would be for the original loan',
          f'amount and ${total_interest:.2f} in interest).')

    while True:
        payment_schedule_type = input(
            'Do you want a Detailed Payment Schedule or a Summary Payment Schedule (D or S): ')
        if payment_schedule_type == 'D' or payment_schedule_type == 'S':
            break
        else:
            print('Please try again.')

    if payment_schedule_type == 'D':
        principal_remaining = loan_amount
        total_interest = 0
        print(title('Payment Schedule'))
        print('Year Month   Principal & Interest  Principal  Interest    Principal Remaining  Total Interest')
        for year in range(1, mortgage_term + 1):
            for month in range(1, 13):
                interest = principal_remaining * interest_rate / 100 / 12
                principal = monthly_payments - interest
                principal_remaining -= principal
                total_interest += interest

                print(f'{year:<4}',
                      f'{month:^5}',
                      f'  {f"${monthly_payments:.2f}":^20}',
                      f' {f"${principal:.2f}":^9}',
                      f' {f"${interest:.2f}":^8}',
                      f'   {f"${principal_remaining: >10,.2f}":^19}',
                      f' {f"${total_interest: >10,.2f}":^14}')
    elif payment_schedule_type == 'S':
        print(title('Summary Payment Schedule'))
        print('Year      Total Principal   Total Interest')
        principal_remaining = loan_amount
        total_interest = 0
        for year in range(1, mortgage_term + 1):
            for month in range(1, 13):
                interest = principal_remaining * interest_rate / 100 / 12
                principal = monthly_payments - interest
                principal_remaining -= principal
                total_interest += interest
                principal_paid = loan_amount - principal_remaining

            print(f'{year:<13}',
                  f'  {f"${principal_paid:.2f}":^20}',
                  f' {f"${total_interest: >10,.2f}":^14}')
        print('Grand Totals: ',
              f'  {f"${principal_paid:.2f}":^20}',
              f' {f"${total_interest: >10,.2f}":^14}')


if __name__ == '__main__':
    main()
