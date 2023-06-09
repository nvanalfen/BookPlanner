from enum import Enum

class FieldType(Enum):
    TEXT = "Text"
    EXTENDED_TEXT = "Extended Text"
    NUMBER = "Number"
    LIST = "List"
    SET = "Set"
    DICT = "Dict"
    FILE = "File"
    IMAGE = "Image"

    def compatible_types(item, field_type):
        if item is None:
            return True
        
        switch = {
            FieldType.TEXT : type( "" ),
            FieldType.EXTENDED_TEXT : type( "" ),
            FieldType.NUMBER : type( 0.0 ),
            FieldType.LIST : type( list() ),
            FieldType.SET : type( set() ),
            FieldType.DICT : type( {} ),
            FieldType.FILE : type( {} ),
            FieldType.IMAGE : type( {} ),
        }

        return switch[ field_type ] == type( item )
    
    def get_field(field_type):

        switch = {
            FieldType.TEXT : TextField,
            FieldType.EXTENDED_TEXT : ExtendedTextField,
            FieldType.NUMBER : NumberField,
            FieldType.LIST : ListField,
            FieldType.SET : SetField,
            FieldType.DICT : DictField,
            FieldType.FILE : FileField,
            FieldType.IMAGE : ImageField,
        }

        return switch[field_type]

class Field:
    def __init__(self):
        self.type = None
        self.content = None

    def add_content(self, item):
        if not FieldType.compatible_types( item, self.type ):
            return False
        return True

    def set_content(self, item):
        if not FieldType.compatible_types( item, self.type ):
            return
        self.content = item

    def get_content(self):
        return self.content

class TextField(Field):
    def __init__(self):
        self.type = FieldType.TEXT
        self.content = ""

    def add_content(self, item):
        if not super().add_content(item):
            return

        self.content += " "
        self.content += item

class ExtendedTextField(Field):
    def __init__(self):
        self.type = FieldType.EXTENDED_TEXT
        self.content = ""

    def add_content(self, item):
        if not super().add_content(item):
            return

        self.content += "\n"
        self.content += item

class NumberField(Field):
    def __init__(self):
        self.type = FieldType.NUMBER
        self.content = 0.0

    def add_content(self, item):
        if not super().add_content(item):
            return

        self.content += item

class ListField(Field):
    def __init__(self):
        self.type = FieldType.LIST
        self.content = []

    def add_content(self, item):
        if not super().add_content(item):
            return

        self.content.append( item )

class SetField(Field):
    def __init__(self):
        self.type = FieldType.SET
        self.content = set()

    def add_content(self, item):
        if not super().add_content(item):
            return

        self.content.add( item )

class DictField(Field):
    def __init__(self):
        self.type = FieldType.DICT
        self.content = {}

    def add_content(self, item):
        if not super().add_content(item):
            return

        label, value = item
        self.content[ label ] = value

class FileField(Field):
    def __init__(self):
        self.type = FieldType.FILE
        self.content = {}

        self.content["Program"] = []
        self.content["Path"] = []
    
    def add_content(self, item):

        program, path = item
        self.content["Program"].append( program )
        self.content["Path"].append( path )

class ImageField(FileField):
    def __init__(self):
        super().__init__()

        self.type = FieldType.IMAGE