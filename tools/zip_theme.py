import os
import zipfile

def create_zip(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # arcname should be relative to source_dir (files at the root of the zip)
                arcname = os.path.relpath(file_path, start=source_dir)
                # Ensure forward slashes for zip compatibility
                arcname = arcname.replace('\\', '/')
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    create_zip(os.path.join('tgolden-kicks-extracted', 'goldenkicks-fse-theme'), 'goldenkicks-fse-theme.zip')
    print('ZIP created successfully with Python.')
