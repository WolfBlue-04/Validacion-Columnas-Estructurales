import clr

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

# Elementos recibidos desde Dynamo
entrada = IN[0]

if not isinstance(entrada, list):
    entrada = [entrada]

elementos = [UnwrapElement(e) for e in entrada if e is not None]

registros = []

for el in elementos:

    # ID
    id_elemento = el.Id.Value

    # Tipo
    tipo = doc.GetElement(el.GetTypeId())

    if tipo:
        parametro_tipo = tipo.get_Parameter(
            BuiltInParameter.SYMBOL_NAME_PARAM
        )
        nombre_tipo = parametro_tipo.AsString() if parametro_tipo else ""
    else:
        nombre_tipo = ""

    # Nivel
    nivel_el = doc.GetElement(el.LevelId)
    nivel = nivel_el.Name if nivel_el else ""

    # Clasificación
    if nombre_tipo.startswith("CC"):
        clasificacion = "Hormigon"

    elif nombre_tipo.startswith("W"):
        clasificacion = "Acero W"

    elif nombre_tipo.startswith("HSS"):
        clasificacion = "Acero HSS"

    elif nombre_tipo.startswith("SC_"):
        clasificacion = "Pilar de referencia"

    else:
        clasificacion = "Otro tipo"

    registros.append([
        id_elemento,
        nombre_tipo,
        nivel,
        clasificacion
    ])

encabezados = [
    "Id",
    "Tipo",
    "Nivel",
    "Clasificacion"
]

OUT = [encabezados] + registros
