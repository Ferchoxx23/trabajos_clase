def Texto(texto=""):
    """
    Esta función recibe un texto y lo devuelve en mayúsculas.
    Si no se proporciona texto, devuelve un mensaje por defecto.
    """
    if not texto:
        return "No se proporcionó texto"
    return texto.upper()