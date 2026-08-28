import os
import zipfile

def create_zip_light(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Normalize path separator to forward slash for path checks
            norm_root = root.replace('\\', '/')
            if 'assets/products' in norm_root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=source_dir)
                arcname = arcname.replace('\\', '/')
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    create_zip_light('golden-kicks-wp-editable-theme', 'golden-kicks-wp-editable-theme-light.zip')
    print('Lightweight ZIP created successfully.')
