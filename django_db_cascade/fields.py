from django.db.models import ForeignKey as FK

class ForeignKey(FK):
    def __init__(self, *args, db_delete=False, **kwargs):
        self.db_delete = db_delete
        kwargs.pop('db_delete', None)
        super().__init__(*args, **kwargs)

