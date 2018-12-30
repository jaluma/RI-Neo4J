

def serialize_concursante(concursante):
    return {
        'nombre': concursante['nombre'],
        'apellido': concursante['apellido'],
        'edad': concursante['edad'],
        'pais': concursante['pais'],
        'nombre_artistico': concursante['nombre_artistico'],
    }

def serialize_gala(gala):
    return {
        'numero': gala['numero'],
        'nombre': gala['nombre'],
        'fecha': gala['fecha'],
    }
