class ReadOnlyMixin:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            # the same thing will be self.fields.values(),
            # because self.fields is dict and field in the case above is the key, which is string
            self.fields[field].disabled = True
            self.fields[field].widget.attrs['readonly'] = True