# mock_reservations.py

import os
import django
import random
from datetime import datetime, timedelta
from booking_app.models import Booking, Table, User
from faker import Faker

fake = Faker()
# Initialize Django settings for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()


def create_mock_reservations(num_reservations=30):
    """
    Generate mock reservations.
    """
    # Fetch all tables and users
    tables = Table.objects.all()
    users = User.objects.all()

    if not tables or not users:
        print("No tables or users found. Please make sure some tables and users exist.")
        return

    for _ in range(num_reservations):
        # Randomly select a user and a table
        user = random.choice(users)
        table = random.choice(tables)

        # Generate a fake future date and time for booking
        fake_future_date = fake.date_between_dates(date_start=datetime.now(), date_end=datetime.now() + timedelta(days=60))
        fake_time = fake.time_object()

        # Combining date and time into a datetime object
        booking_datetime = datetime.combine(fake_future_date, fake_time)

        # Randomly generate number of guests, assume max 10 guests for simplicity
        num_guests = random.randint(1, 10)

        # Create the booking
        Booking.objects.create(user=user, table=table, booking_date=booking_datetime, number_of_guests=num_guests)

    print(f"{num_reservations} mock reservations created!")


if __name__ == '__main__':
    create_mock_reservations()
