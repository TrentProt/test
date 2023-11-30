import os

import pdfkit
import qrcode
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.views import APIView
from pdfkit.configuration import Configuration
from items.models import Item, Basket, PDF
import random
import datetime

CONFIG = Configuration(wkhtmltopdf='C:/Disk/Convet/wkhtmltopdf/bin/wkhtmltopdf.exe')
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

class ItemAPIViewPost(APIView):

    def post(self, request):
        Basket.objects.all().delete()
        list_items_id = request.data['items']
        summa = 0
        now_time = datetime.datetime.now()
        fromat_time = now_time.strftime("%d-%m-%Y %H:%M")

        for i in list_items_id:
            item = Item.objects.get(id=i)
            summa += item.price
            baskets = Basket.objects.filter(item=item)

            if not baskets.exists():
                Basket.objects.create(item=item, quantity=1)

            else:
                basket = baskets.first()
                basket.quantity += 1
                basket.save()

        items_in_basket = Basket.objects.all()
        html_layout = render_to_string('items/example.html', {'items': items_in_basket, 'summa': summa, 'time': fromat_time})
        random_number = random.randint(10000000, 99999999)
        pdfkit.from_string(html_layout,configuration=CONFIG, output_path=f'media/{random_number}.pdf')
        qr.add_data(f'http://127.0.0.1:8000/media/{random_number}.pdf')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'media/qrcodes/{random_number}.png')
        PDF.objects.create(number=random_number, img=f'qrcodes/{random_number}.png', file=f'{random_number}.pdf')
        pdf = PDF.objects.get(number=random_number)
        return render(request, 'items/qrcode.html', {'pdf': pdf})

class ItemAPIViewGet(APIView):

    def get(self, request, pdfname):
        pdf = PDF.objects.filter(file=pdfname)

        if not pdf.exists():
            return HttpResponse('404')

        else:
            file = PDF.objects.get(file=pdfname)
            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = f'attachment; filename={pdfname}'
            return render(request, 'items/pdfcheck.html', {'file': file})
