from django.shortcuts import render, redirect
from .models import Table, Booking, MenuItem
from .forms import BookingForm
from django.shortcuts import get_object_or_404
import datetime

def home(request):
    return render(request, 'home.html')

def list_tables(request):
    tables = Table.objects.all()
    return render(request, 'tables_booking.html', {'tables': tables})

def book_table(request):
    # Placeholder logic for now
    return render(request, 'booking_app/book_table.html')

def general_menu(request):
    menu_items = MenuItem.objects.all()
    context = {
        'menu': menu_items
    }
    return render(request, 'booking_app/general_menu.html', context)

def view_menu(request, table_id):
    table = get_object_or_404(Table, id=table_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.table = table
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()

    menu_items = table.restaurant.menuitem_set.all()  # Ensure your models are set up this way
    context = {
        'form': form,
        'table': table,
        'menu_items': menu_items,
    }
    return render(request, 'view_menu.html', context)

def booking_view(request, table_id=None):
    tables = Table.objects.all()

    if request.method == 'POST' and table_id:
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.table_id = table_id
            if request.user.is_authenticated:  # Check for authenticated user
                booking.user = request.user
            else:
                # Handle unauthenticated user (e.g., redirect to login or show an error)
                pass
            booking.save()
            return redirect('home')  # redirect to the home view after booking
    else:
        form = BookingForm()

    context = {
        'tables': tables,
        'form': form
    }
    return render(request, 'booking_app/tables_booking.html', context)

def available_tables_view(request):
    # Get all tables
    all_tables = Table.objects.all()

    # Get tables that are currently booked
    booked_tables = Booking.objects.filter(booking_datetime__date=datetime.date.today()).values_list('table', flat=True)

    # Filter out tables that are booked
    available_tables = all_tables.exclude(id__in=booked_tables)

    context = {
        'tables': available_tables,
    }
    return render(request, 'your_template_name.html', context)
