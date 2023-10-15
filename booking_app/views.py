from django.shortcuts import render, redirect
from .models import Table, Booking
from .forms import BookingForm
from .models import MenuItem
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')


def list_tables(request):
    # Placeholder logic for now
    return render(request, 'booking_app/list_tables.html')


def book_table(request):
    # Placeholder logic for now
    return render(request, 'booking_app/book_table.html')


def general_menu(request):
    menu_items = MenuItem.objects.all()

    context = {
        'menu': menu_items
    }

    return render(request, 'general_menu.html', context)


def view_menu(request, table_id):
    # Fetching the table or redirecting if it does not exist
    table = get_object_or_404(Table, id=table_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.table = table
            booking.save()
            # Redirect to a confirmation page or home after successful booking
            return redirect('home')
    else:
        form = BookingForm()

    # Assuming there's a menu related to the restaurant of the table
    menu_items = table.restaurant.menuitem_set.all()

    context = {
        'form': form,
        'table': table,
        'menu_items': menu_items,
    }

    return render(request, 'view_menu.html', context)
