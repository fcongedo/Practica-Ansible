# /home/fran/practica-ansible/ejercicios-avanzados/filter_plugins/custom_filters.py

def to_uppercase(value):
    """Convierte un texto a mayúsculas."""
    if isinstance(value, str):
        return value.upper()
    return value

class FilterModule(object):
    """Clase que contiene el filtro personalizado."""
    def filters(self):
        return {
            'to_uppercase': to_uppercase
        }
