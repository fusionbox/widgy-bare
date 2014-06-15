from django.views.generic import DetailView

from widgy.contrib.form_builder.views import HandleFormMixin

from .models import Owner


class OwnerView(DetailView):
    model = Owner


class OwnerFormView(HandleFormMixin, OwnerView):
    model = Owner


owner_detail = OwnerView.as_view()
owner_form = OwnerFormView.as_view()
