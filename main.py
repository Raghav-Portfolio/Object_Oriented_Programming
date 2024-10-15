import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id':str}) # load all the data as string because even if you were to use int(input()),
    #the way the data is read in the class is as a string and it's more complicated to make all of these changes instead of
    # loading the dataframe as str
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records') # it makes sense to import this data as a dictionary
    # because a single dictionary represents one row of the card data

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()
        
        
    def book_room(self):
        """Change the availability of a hotel from yes to no if selected"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)
        
    def available(self):
        """Check the availability of a hotel"""
        availability =  df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate_ticket(self):
        content = f"""
        Thank you for your booking.
        Here is your booking data:
        Name: {self.customer_name}
        Hotel Name : {self.hotel.name}
        """
        return content
    
    
class CreditCard:
    def __init__(self, number):
        self.number = number
    
    def validated(self, expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration,
                     'holder': holder, 'cvc':cvc}
        if card_data in df_cards:
            print('Your Card was Validated!')
            return True
        

print(df)
id = input('Enter the hotel ID')
hotel = Hotel(hotel_id=id)

if hotel.available():
    credit_card = CreditCard(number ='1234')
    if credit_card.validated(expiration='12/26', holder='JOHN SMITH', cvc='123'):
        hotel.book_room()
        name = input('Enter your name')
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel) #the reservation ticket class should point to the specified hotel
        print(reservation_ticket.generate_ticket())
    else:
        print("Credit Card was not validated")
else:
    print('Hotel is not free')
    