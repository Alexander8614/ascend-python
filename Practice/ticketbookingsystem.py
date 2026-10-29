def book_seats(seats_available, seats_requested):
    if seats_requested <= 0:
        raise ValueError('You should pick at least one ticket')
    else:
        return seats_available - seats_requested

def send_confirmation_email(email_address):
    return email_address.strip()

try:
    remaining = book_seats(50, 3)
    send_confirmation_email(12345)
except ValueError as err:
    print("Booking problem:", err)
except AttributeError as err:
    print("System error, please contact support:", err)
