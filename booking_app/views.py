from django.shortcuts import render
from .models import Table, Booking
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')


def list_tables(request):
    # Placeholder logic for now
    return render(request, 'booking_app/list_tables.html')


def book_table(request):
    # Placeholder logic for now
    return render(request, 'booking_app/book_table.html')


def view_menu(request, table_id):
    table = Table.objects.get(id=table_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.table = table
            booking.save()
            # Redirect to a confirmation page or home
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'book_table.html', {'form': form, 'table': table})
