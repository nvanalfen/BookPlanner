from msilib.schema import Error
from Field import FieldType, TextField, ExtendedTextField, NumberField, \
                    ListField, SetField, DictField, FileField, ImageField

class Entity:
    def __init__(self):
        self.title = ""
        self.main_category = None
        self.sub_categories = set()
        self.related_entities = set()
        self.fields = {}
        self.field_order = []

    def set_fields(self):
        pass

    def add_field(self, label, field_type):

        if label in self.fields:
            raise Error("Field {} Already Exists".format(label))

        field = FieldType.get_field(field_type)
        
        self.fields[ label ] = field()
        self.field_order.append( label )