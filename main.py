import random

import pandas as pd

df = pd.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CredictCart:
    def __init__(self, holder, card_number, expiration_date, cvc):
        self.holder = holder
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvc = cvc

    def make_payment(self):
        # :)
        succeed = random.choice([True, False])
        return succeed

    def validate(self):
        cards_df = pd.read_csv('cards.csv')
        result = cards_df.loc[cards_df['number'] == self.card_number]
        for i in result.iterrows():
            if i[1]['expiration'] == self.expiration_date and i[1]['cvc'] == self.cvc and i[1]['holder'] == self.holder:
                succeed = self.make_payment()
                if succeed:
                    return True, 0
                return False, "Payment failed: Insufficient funds"
            return False, "Payment failed: The card is not valid"


hotel_id = int(input('Enter hotel id: '))
hotel = Hotel(hotel_id)

if hotel.available():
    holder = input("Enter your name: ")
    card_number = int(input("Enter your card number: "))
    expiration_date = input("Enter expiration date: ")
    cvc = int(input("Enter CVC: "))

    credict_cart = CredictCart(holder, card_number, expiration_date, cvc)
    payment_succeed = credict_cart.validate()[0]
    if payment_succeed:
        hotel.book()
        reservation = ReservationTicket(holder, hotel)
        print(reservation.generate())
    else:
        print(credict_cart.validate()[1])
else:
    print("Sorry, the hotel is not available")
