from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.pdf', '.doc', '.docx','.xls','.xlsx','.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Tipo de archivo no soportado.')