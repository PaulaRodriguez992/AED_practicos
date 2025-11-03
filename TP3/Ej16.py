
from heap import HeapMax

# 1. Creamos una instancia de nuestra cola de prioridad para la impresora.
#    Ya no necesitamos definir la clase aquí, ¡solo la usamos!
cola_impresion = HeapMax()

print("Iniciando simulación de la cola de impresión...")
print("-" * 40)

# a. Cargue tres documentos de empleados (prioridad 1).
print("a. Cargando 3 documentos de empleados...")
cola_impresion.arrive("Informe_Ventas_Empleado.docx", 1)
cola_impresion.arrive("Planilla_Horarios_Empleado.xlsx", 1)
cola_impresion.arrive("Memo_Interno_Empleado.pdf", 1)
print(f"   Estado de la cola: {cola_impresion.elements}")
print("-" * 40)

# b. Imprima el primer documento de la cola.
print("b. Imprimiendo el primer documento...")
documento_impreso = cola_impresion.attention()
print(f"   Imprimiendo: '{documento_impreso[1]}' (Prioridad: {documento_impreso[0]})")
print(f"   Estado de la cola: {cola_impresion.elements}")
print("-" * 40)

# c. Cargue dos documentos del staff de TI (prioridad 2).
print("c. Cargando 2 documentos de TI...")
cola_impresion.arrive("Actualizacion_Servidores_TI.pdf", 2)
cola_impresion.arrive("Log_Errores_Sistema_TI.txt", 2)
print(f"   Estado de la cola: {cola_impresion.elements}")
print("-" * 40)

# d. Cargue un documento del gerente (prioridad 3).
print("d. Cargando 1 documento de Gerente...")
cola_impresion.arrive("Reporte_Financiero_Gerente.xlsx", 3)
print(f"   Estado de la cola: {cola_impresion.elements}")
print("-" * 40)

# e. Imprima los dos primeros documentos de la cola.
print("e. Imprimiendo los dos siguientes documentos...")
documento_impreso_1 = cola_impresion.attention()
print(f"   Imprimiendo: '{documento_impreso_1[1]}' (Prioridad: {documento_impreso_1[0]})")
documento_impreso_2 = cola_impresion.attention()
print(f"   Imprimiendo: '{documento_impreso_2[1]}' (Prioridad: {documento_impreso_2[0]})")
print(f"   Estado de la cola: {cola_impresion.elements}")
print("-" * 40)

# f. Cargue dos documentos de empleados y uno de gerente.
print("f. Cargando 2 docs de empleados y 1 de gerente...")
cola_impresion.arrive("Solicitud_Vacaciones_Empleado.docx", 1)
cola_impresion.arrive("Presentacion_Resultados_Empleado.pptx", 1)
cola_impresion.arrive("Plan_Estrategico_Gerente.docx", 3)
print(f"   Estado de la cola: {cola_impresion.elements}")
print("-" * 40)

# g. Imprima todos los documentos de la cola de impresión.
print("g. Vaciando la cola de impresión en orden de prioridad...")
while cola_impresion.size() > 0:
    documento_final = cola_impresion.attention()
    print(f"   Imprimiendo: '{documento_final[1]}' (Prioridad: {documento_final[0]})")

print("-" * 40)
print(f"Simulación finalizada. La cola está vacía: {cola_impresion.elements}")