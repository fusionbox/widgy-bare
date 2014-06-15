from django.db import models

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
            'xxx.Widget',
        ),
    )


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
