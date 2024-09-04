import os

def rename_pdf_files(directory, prefix_to_remove):
    # Lista todos los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith('.pdf') and filename.startswith(prefix_to_remove):
            # Genera el nuevo nombre del archivo sin el prefijo
            new_filename = filename[len(prefix_to_remove):]
            
            # Crea las rutas completas para el archivo antiguo y el nuevo
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Renombra el archivo
            os.rename(old_file_path, new_file_path)
            print(f'Renombrado: {old_file_path} -> {new_file_path}')

# Directorio donde están los archivos PDF
pdf_directory = 'C:/Users/emili/Downloads/nums'

# Prefijo que queremos eliminar del nombre del archivo
prefix_to_remove = 'Numerología'

# Llama a la función para renombrar los archivos PDF
rename_pdf_files(pdf_directory, prefix_to_remove)
