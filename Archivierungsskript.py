import os
import zipfile

def zip_files(directory_path, output_zip):
    # Erstellen eines ZipFile-Objekts im Schreibmodus
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Durchlaufen aller Dateien im Verzeichnis
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Hinzufügen der Datei zum ZIP-Archiv
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(directory_path, '..')))

# Verzeichnispfad, der archiviert werden soll
directory_to_zip = '/pfad/zum/verzeichnis'
# Zielpfad der ZIP-Datei
zip_output_name = '/pfad/zum/zip_output.zip'

zip_files(directory_to_zip, zip_output_name)
