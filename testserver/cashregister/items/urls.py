from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from items.views import ItemAPIViewPost, ItemAPIViewGet

urlpatterns = [
    path('api/cash_machine', ItemAPIViewPost.as_view()),
    path('media/<str:pdfname>', ItemAPIViewGet.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)