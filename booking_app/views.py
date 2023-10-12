from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def list_tables(request):
    # Placeholder logic for now
    return render(request, 'booking_app/list_tables.html')


def book_table(request):
    # Placeholder logic for now
    return render(request, 'booking_app/book_table.html')


def view_menu(request):
    # Placeholder logic for now
    return render(request, 'booking_app/menu.html')
