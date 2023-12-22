from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl import Workbook
from sample_app.models import Details

def HOME(request):
    if request.method == "POST":
        Details.objects.create(name=request.POST['name'], profile=request.POST['pf'])
        return render(request, 'margins.html')
    return render(request, 'margins.html')

def display_det(request):
    all_details = Details.objects.all()
    return render(request, 'display_all.html', {'det': all_details})

def generate_excel(request):
    all_details = Details.objects.all()

    # Create a workbook and add details to it
    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Name'
    sheet['B1'] = 'Profile'

    for index, detail in enumerate(all_details, start=2):
        sheet[f'A{index}'] = detail.name
        sheet[f'B{index}'] = detail.profile

    # Save the workbook to a BytesIO buffer
    from io import BytesIO
    buffer = BytesIO()
    workbook.save(buffer)
    buffer.seek(0)

    # Create a response with the Excel content
    response = HttpResponse(buffer.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=details.xlsx'

    return response
