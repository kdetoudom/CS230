"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Giving the total price of the ticket(s) after sales tax and city tax

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.

"""
STATETAX = .0625
CITYTAX = .0075
print("Welcome to the automatic ticket price tabulater")

print("Please enter ticket price level")
ticketPriceLevel = int(input())
print("Please enter number of tickets")
ticketNumber = int(input())
print("Sale report for ticket purchase")
print("-" * 20)

ticketCost = ticketPriceLevel * ticketNumber
print("Ticket Cost: ", str(ticketCost).rjust(8))
stateTaxTotal = ticketCost * STATETAX
print("State Tax: ", str(stateTaxTotal).rjust(8))
cityTaxTotal = ticketCost * CITYTAX
print("City Tax: ", str(cityTaxTotal).rjust(8))
totalCost = ticketCost + stateTaxTotal + cityTaxTotal
print("Total Cost: ", str(totalCost).rjust(8))
