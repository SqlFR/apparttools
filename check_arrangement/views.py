from django.shortcuts import render, get_object_or_404, redirect
from .models import Apartment, ApartmentIssues
from .forms import ApartmentForm, IssuesForm


def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('check_arrangement:index')
    else:
        form = ApartmentForm()
    return render(request, 'check_arrangement/add_apartment.html', {'form': form})


def delete_apartment(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    apartment.delete()
    return redirect('check_arrangement:index')


def index(request):
    list_apartment = Apartment.objects.filter().order_by('name')
    context = {
        'list_apartment': list_apartment,
    }
    return render(request, "check_arrangement/index.html", context)


def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    if request.method == 'POST':
        form = IssuesForm(request.POST, apartment=apartment)
        if form.is_valid():
            form.instance.apartment = apartment
            form.save()
            return redirect('check_arrangement:detail', apartment_id=apartment.id)
    else:
        form = IssuesForm(apartment=apartment)
    context = {
        'apartment': apartment,
        'form': form
    }

    return render(request, 'check_arrangement/detail.html', context)


def results(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    apartment_issues = ApartmentIssues.objects.filter(apartment_id=apartment_id)
    context = {
        'apartment': apartment,
        'apartment_issues': apartment_issues
    }
    return render(request, 'check_arrangement/results.html', context)


