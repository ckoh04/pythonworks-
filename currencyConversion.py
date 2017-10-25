"""
This program will calculate the currency equivalence between U.S. Dollar ($) and EURO (€)
Current value (Feb 29, 2016 4:24) $1.00 US = € 0.92
"""
USD= input("Enter USD: (Q or q to execute)")
while(USD!="Q" and USD!="q"):
    EUR= eval(USD) -(eval(USD) * 0.08)
    print ("EUR",EUR)
    USD = input("Enter USD:(Q or q to execute)")
    
