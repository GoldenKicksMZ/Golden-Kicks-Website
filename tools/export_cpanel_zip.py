import os
import zipfile

def zip_cpanel():
    source_dir = "Official Website"
    output_zip = "golden_kicks_cpanel.zip"
    
    if not os.path.exists(source_dir):
        print(f"Error: {source_dir} directory not found.")
        return

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=source_dir).replace('\\', '/')
                zipf.write(file_path, arcname)

    size_mb = os.path.getsize(output_zip) / (1024 * 1024)
    print(f"SUCCESS: Created {output_zip} ({size_mb:.2f} MB)")
    print("Ready to upload and extract in cPanel public_html!")

if __name__ == '__main__':
    zip_cpanel()
