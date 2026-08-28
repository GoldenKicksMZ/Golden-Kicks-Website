import csv
import json
import random
import os

# Brands, silos, templates
templates = [
    ("Mercurial Superfly 16", "Nike", "Velocidade", "NK-MERC", "campo", "FG"),
    ("Phantom GX 2 Elite", "Nike", "Controlo", "NK-PGX", "campo", "FG"),
    ("Tiempo Legend 10", "Nike", "Toque", "NK-TMP", "society", "TF"),
    ("Mercurial Vapor 16", "Nike", "Velocidade", "NK-VAP", "futsal", "IC"),
    ("Predator Elite", "Adidas", "Precisão", "AD-PRED", "campo", "FG"),
    ("F50 League", "Adidas", "Velocidade", "AD-F50", "society", "TF"),
    ("Copa Pure 2", "Adidas", "Clássico", "AD-COPA", "campo", "FG"),
    ("Future Ultimate", "Puma", "Agilidade", "PM-FUT", "campo", "FG"),
    ("Ultra Ultimate", "Puma", "Velocidade", "PM-ULT", "society", "TF"),
    ("King Ultimate", "Puma", "Clássico", "PM-KNG", "campo", "FG"),
    ("Tekela V4 Pro", "New Balance", "Controlo", "NB-TEK", "campo", "FG"),
    ("Furon V7 Pro", "New Balance", "Velocidade", "NB-FUR", "society", "TF"),
    ("Morelia Neo IV", "Mizuno", "Clássico", "MZ-MOR", "society", "TF"),
    ("Alpha Japan", "Mizuno", "Velocidade", "MZ-ALP", "campo", "FG"),
    ("Top Flex Rebound", "Joma", "Clássico", "JM-TOP", "futsal", "IC"),
    ("Tactico Futsal", "Joma", "Agilidade", "JM-TAC", "futsal", "IC")
]

levels = ["Elite", "Pro", "Academy", "Club"]
colors = [
    "Black / Gold", "White / Gold", "Phantom / Silver", "Triple Black", 
    "Crimson / Bone", "Navy / Volt", "Volt / Silver", "Electric Yellow / Black",
    "Solar Red / White", "Emerald Green / Gold"
]
standard_sizes = "35,36,37,38,39,40,41,42,43,44,45,46"
sizes_list = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

# 7 Image angles pool
image_angles_pool = [
    "./assets/PRODUCTS/GX Firm Ground Angle 1.png",
    "./assets/PRODUCTS/GX Firm Ground Angle 2.png",
    "./assets/PRODUCTS/Superfly Firm Ground Angle 1.jpg",
    "./assets/PRODUCTS/Superfly Firm Ground Angle 2.jpg",
    "./assets/PRODUCTS/F50 Firm Ground Angle 1.png",
    "./assets/PRODUCTS/F50 Firm Ground Angle 2.png",
    "./assets/PRODUCTS/Predator Firm Ground Angle 1.png"
]

csv_headers = [
    "sku", "name", "brand", "silo", "level", "category", "surface", "price", 
    "color", "sizes", "description", "badge",
    "angle1", "angle2", "angle3", "angle4", "angle5", "angle6", "angle7"
]

csv_rows = []
json_products = []

for i in range(1, 506): # 505 products total
    tmpl, brand, silo, sku_prefix, cat, surf = random.choice(templates)
    level = random.choice(levels)
    color = random.choice(colors)
    price = random.choice([4800, 5800, 6800, 8900, 12500, 15800, 18500, 19200, 21500])
    
    # Auto generated SKU e.g. NK-MERC-42 or NK-MERC-1001
    size_sample = random.choice(sizes_list)
    sku = f"{sku_prefix}-{size_sample}-{i:03d}"
    
    prod_name = f"{brand} {tmpl} {surf} #{i}"
    desc = f"Chuteira {brand} {tmpl} {level} de alta performance para relvado {surf}. Desenho ergonómico com 7 ângulos visuais e tamanhos do 35 ao 46."
    badge = "Novidade" if i % 8 == 0 else ("Mais Vendido" if i % 5 == 0 else "Stock Verificado")
    
    # 7 angles
    shuffled_angles = list(image_angles_pool)
    random.shuffle(shuffled_angles)
    # Ensure 7 items
    while len(shuffled_angles) < 7:
        shuffled_angles.append(random.choice(image_angles_pool))
    
    angles = shuffled_angles[:7]
    
    # CSV row dictionary
    csv_row = {
        "sku": sku,
        "name": prod_name,
        "brand": brand,
        "silo": silo,
        "level": level,
        "category": cat,
        "surface": surf,
        "price": price,
        "color": color,
        "sizes": standard_sizes,
        "description": desc,
        "badge": badge,
        "angle1": angles[0],
        "angle2": angles[1],
        "angle3": angles[2],
        "angle4": angles[3],
        "angle5": angles[4],
        "angle6": angles[5],
        "angle7": angles[6]
    }
    csv_rows.append(csv_row)
    
    # JSON object
    json_prod = {
        "id": f"prod-{i}",
        "sku": sku,
        "name": prod_name,
        "silo": silo,
        "level": level,
        "brand": brand,
        "category": cat,
        "surface": surf,
        "price": price,
        "badge": badge,
        "subtitle": {
            "pt": f"Chuteira {brand} {level} para {surf}.",
            "en": f"High performance {brand} {level} for {surf}."
        },
        "description": {
            "pt": desc,
            "en": f"{brand} {tmpl} {level} engineered for elite performance. Sizes 35 to 46."
        },
        "image": angles[0],
        "hoverImage": angles[1],
        "gallery": angles,
        "sizes": sizes_list,
        "color": color,
        "inStock": True
    }
    json_products.append(json_prod)

# Write CSV
csv_file = "catalog_500_products.csv"
with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(csv_rows)

print(f"Successfully generated CSV spreadsheet: {csv_file} with {len(csv_rows)} products!")

# Write JSON to products.json
json_dir = "Official Website/assets/data"
os.makedirs(json_dir, exist_ok=True)
json_file = os.path.join(json_dir, "products.json")
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(json_products, f, ensure_ascii=False, indent=2)

print(f"Successfully updated JSON dataset: {json_file} with {len(json_products)} products!")
