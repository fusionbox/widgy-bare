from django.views.generic import DetailView

from .models import Owner


owner_detail = DetailView.as_view(model=Owner)
