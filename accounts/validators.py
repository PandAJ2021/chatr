import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not re.fullmatch(r'09\d{9}', value):
        raise ValidationError('Number is not valid.')
