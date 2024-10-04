import os
from datetime import datetime, timedelta

# Ruta base
base_path = "/home/santanaoliva_u/Documents/Universidad Tec Playacar/00 - Ingenieria en Sistemas/2024"

# Materias con su horario (día de la semana y hora de inicio y fin)
subjects = {
    '211': {'name': 'DISEÑO ESTRUCTURADO DE ALGORITMOS', 'days': ['Lun', 'Mié', 'Jue'], 'time': '18-30'},
    '212': {'name': 'TEMAS SELECTOS DE FÍSICA APLICADA A LA INGENIERIA', 'days': ['Lun', 'Mié'], 'time': '17-00'},
    '213': {'name': 'FUNDAMENTOS DE REDES', 'days': ['Lun', 'Mié'], 'time': '15-00'},
    '214': {'name': 'ESTRATEGIAS PARA LA AUTONOMÍA DEL APRENDIZAJE', 'days': ['Mar', 'Vie'], 'time': '15-00'},
    '215': {'name': 'FUNDAMENTOS DE INGENIERÍA DEL SOFTWARE', 'days': ['Mar', 'Vie'], 'time': '17-00'}
}

# Días en español
dias_semana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']

# Meses en español
meses = ['Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Crear carpetas de materias
def create_subject_folders(base, subjects):
    for code, subject_info in subjects.items():
        subject_folder = os.path.join(base, f"{code} {subject_info['name']}")
        if not os.path.exists(subject_folder):
            os.makedirs(subject_folder)

# Crear cuatrimestres, meses y carpetas para cada fecha
def create_quarters_months_and_dates(subject_folder, start_date, end_date, subject_info):
    cuatrimestres = ["01 - Cuatrimestre", "02 - Cuatrimestre", "03 - Cuatrimestre", "04 - Cuatrimestre", "05 - Cuatrimestre"]
    
    current_quarter_start = start_date
    
    for i, cuatrimestre in enumerate(cuatrimestres):
        quarter_path = os.path.join(subject_folder, f"{cuatrimestre}")
        os.makedirs(quarter_path, exist_ok=True)
        
        # Crear carpetas para los meses dentro del cuatrimestre
        for j, mes in enumerate(meses):  # Meses por cuatrimestre (Septiembre a Diciembre en este caso)
            month_folder = os.path.join(quarter_path, f"{str(j).zfill(2)} - {mes}")
            os.makedirs(month_folder, exist_ok=True)
            
            # Generar fechas dentro del mes
            current_date = current_quarter_start
            counter = 0
            
            while current_date.month == start_date.month + j and current_date <= end_date:
                day_of_week = dias_semana[current_date.weekday()]  # Día en español
                
                # Solo crear carpetas si es uno de los días de clase para la materia
                if day_of_week in subject_info['days']:
                    counter += 1  # Contador para el orden
                    folder_name = f"{str(counter).zfill(2)} - {day_of_week} - {current_date.strftime('%d%b').lower()} - {subject_info['time']}"
                    date_folder = os.path.join(month_folder, folder_name)
                    os.makedirs(date_folder, exist_ok=True)
                    
                    # Crear subcarpetas
                    create_subfolders(date_folder)
                
                # Avanzar al siguiente día
                current_date += timedelta(days=1)
        
        # Avanzar al siguiente cuatrimestre
        current_quarter_start = current_date

# Crear las subcarpetas dentro de cada fecha
def create_subfolders(date_folder):
    subfolders = ['00 - Apuntes', '01 - Tareas', '02 - Recursos']
    for subfolder in subfolders:
        os.makedirs(os.path.join(date_folder, subfolder), exist_ok=True)
    
    # Crear archivo .md
    with open(os.path.join(date_folder, "00 - Actividad.md"), "w") as f:
        f.write(f"# Notas del día {os.path.basename(date_folder)}")

# Crear la estructura completa
def create_structure(base, subjects, start_date, end_date):
    create_subject_folders(base, subjects)
    
    for subject_code, subject_info in subjects.items():
        subject_folder = os.path.join(base, f"{subject_code} {subject_info['name']}")
        create_quarters_months_and_dates(subject_folder, start_date, end_date, subject_info)

# Fechas de inicio y fin del cuatrimestre
start_date = datetime(2024, 9, 2)  # Inicio del cuatrimestre
end_date = datetime(2024, 12, 12)  # Fin del cuatrimestre

# Ejecutar el script
create_structure(base_path, subjects, start_date, end_date)

print("Estructura de carpetas creada con éxito.")
