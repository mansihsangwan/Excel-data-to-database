from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django import forms
import django_excel as excel
from .models import *


class UploadFileForm(forms.Form):
    file = forms.FileField()


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        # def choice_func(row):
        #     q = TrainerDetails.objects.filter(slug=row[0])[0]
        #     row[0] = q
        #     return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[TrainerDetails],
                initializers=[None],
                mapdicts=[
                    ['first_name', 'last_name', 'mobile_number', 'location']
                    ]
            )
            return redirect('handson_view')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload xls file:'
        })


def handson_table(request):
    return excel.make_response_from_tables(
        [TrainerDetails], 'handsontable.html')