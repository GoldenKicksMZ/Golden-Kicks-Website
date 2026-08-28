import csv
import json
import os
import sys

def convert_csv_to_products_json(csv_filepath, json_filepath):
    products = []
    
    with open(csv_filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse sizes array if comma separated
            sizes_str = row.get('sizes', '35,36,37,38,39,40,41,42,43,44,45,46')
            sizes = [int(s.strip()) for s in sizes_str.split(',') if s.strip().isdigit()]
            
            # Determine 7 angles
            angle1 = row.get('angle1', row.get('image', './assets/PRODUCTS/GX Firm Ground Angle 1.png'))
            angle2 = row.get('angle2', row.get('hoverImage', angle1))
            angle3 = row.get('angle3', angle1)
            angle4 = row.get('angle4', angle2)
            angle5 = row.get('angle5', angle1)
            angle6 = row.get('angle6', angle2)
            angle7 = row.get('angle7', angle1)
            
            # If explicit gallery column is provided as comma separated string
            if 'gallery' in row and row['gallery'].strip():
                gallery_list = [g.strip() for g in row['gallery'].split(',') if g.strip()]
                if len(gallery_list) > 0:
                    angle1 = gallery_list[0]
                    if len(gallery_list) > 1: angle2 = gallery_list[1]
                    gallery = gallery_list[:7]
                else:
                    gallery = [angle1, angle2, angle3, angle4, angle5, angle6, angle7]
            else:
                gallery = [angle1, angle2, angle3, angle4, angle5, angle6, angle7]

            sku = row.get('sku', f"GK-{len(products)+1:04d}")
            prod_name = row.get('name', 'Chuteira Golden Kicks')
            desc = row.get('description', row.get('description_pt', 'Chuteira de alta performance com 7 ângulos de visualização.'))

            prod = {
                "id": row.get('id', f"prod-{len(products)+1}"),
                "sku": sku,
                "name": prod_name,
                "silo": row.get('silo', 'Velocidade'),
                "level": row.get('level', 'Elite'),
                "brand": row.get('brand', 'Nike'),
                "category": row.get('category', 'campo'),
                "surface": row.get('surface', 'FG'),
                "price": float(row.get('price', 18500)),
                "badge": row.get('badge', 'Stock Verificado'),
                "subtitle": {
                    "pt": row.get('subtitle_pt', prod_name),
                    "en": row.get('subtitle_en', prod_name)
                },
                "description": {
                    "pt": desc,
                    "en": desc
                },
                "image": angle1,       # Main Angle 1 on Product Cards
                "hoverImage": angle2,  # Angle 2 on Card Hover
                "gallery": gallery,    # Full 7 Angles array [angle1 .. angle7]
                "sizes": sizes if sizes else [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
                "color": row.get('color', 'Black / Gold'),
                "inStock": row.get('inStock', 'true').lower() in ['true', '1', 'yes']
            }
            products.append(prod)

    os.makedirs(os.path.dirname(json_filepath), exist_ok=True)
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"Successfully converted {len(products)} products with 7-angle galleries to {json_filepath}!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
        dest_path = sys.argv[2] if len(sys.argv) > 2 else "Official Website/assets/data/products.json"
        convert_csv_to_products_json(csv_path, dest_path)
    else:
        print("Usage: python import_csv.py catalog_500_products.csv [Official Website/assets/data/products.json]")
