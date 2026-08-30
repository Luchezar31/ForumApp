from datetime import datetime, time

from django.http import HttpResponseForbidden


class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            # the same thing will be self.fields.values(),
            # because self.fields is dict and field in the case above is the key, which is string
            self.fields[field].disabled = True
            self.fields[field].widget.attrs['readonly'] = True


class TimeRestrictionMixin:
    def dispatch(self, request, *args, **kwargs):
        current_time = datetime.now().time()

        restrict_start = time(8, 0)  # 8:00 PM
        restrict_end = time(23, 59)

        if not restrict_start <= current_time <= restrict_end:
            return HttpResponseForbidden('The site does not work before 8 and after 20')

        return super().dispatch(request, *args, **kwargs)