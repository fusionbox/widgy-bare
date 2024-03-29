from django.db import models
from django.core import urlresolvers

import widgy
from widgy.site import WidgySite
from widgy.db.fields import WidgyField
from widgy.models import Content


site = WidgySite()


class Owner(models.Model):
    name = models.CharField(max_length=255)
    content = WidgyField(
        site=site,
        root_choices=(
            'page_builder.Layout',
        ),
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return urlresolvers.reverse('owner_detail', kwargs={
            'pk': self.pk,
        })

    def get_form_action_url(self, form, widgy):
        return urlresolvers.reverse('owner_form', kwargs={
            'pk': self.pk,
            'form_node_pk': form.node.pk,
        })


@widgy.register
class Widget(Content):
    name = models.CharField(max_length=255)

    accepting_children = True
    editable = True
    draggable = False
    deletable = False


@widgy.register
class ChildWidget(Content):
    name = models.CharField(max_length=255)

    editable = True
