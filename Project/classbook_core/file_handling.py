from django.conf import settings
from pathlib import Path
import os

# Construct the directory path in which the document-related file will be saved
def construct_file_save_directory(document):

    directory_save_path = os.path.join(settings.COURSES_STORAGE_DIR, str(document.course.id))

    return directory_save_path

# Construct the full file path to retrieve document-related file from
def construct_file_path(document):

    file_name_with_extension = '{0}.{1}'.format(document.name, document.doc_type) # Files are saved as 'name.doc_type'
    file_path = os.path.join(settings.COURSES_STORAGE_DIR, str(document.course.id), file_name_with_extension)

    return file_path
