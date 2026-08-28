import json
import random
import os

# Brands and details
brands = ["Nike", "Adidas", "Puma", "New Balance", "Mizuno", "Joma"]
silos = ["Velocidade", "Controlo", "Precisão", "Agilidade", "Clássico"]
levels = ["Elite", "Pro", "Academy", "Club"]
categories = ["campo", "society", "futsal"]
surfaces = {
    "campo": ["FG", "SG", "AG", "MG", "HG"],
    "society": ["TF"],
    "futsal": ["IN", "IC"]
}
colors = ["Phantom / Gold", "Black / Gold", "White / Gold", "Triple Black", "Crimson / Bone", "Navy / Volt", "Volt / Silver"]

# Sizes range strictly 35 to 46
standard_sizes = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

angle_pools = [
    [
        "./assets/PRODUCTS/GX Firm Ground Angle 1.png",
        "./assets/PRODUCTS/GX Firm Ground Angle 2.png",
        "./assets/PRODUCTS/Superfly Firm Ground Angle 1.jpg",
        "./assets/PRODUCTS/Superfly Firm Ground Angle 2.jpg",
        "./assets/PRODUCTS/F50 Firm Ground Angle 1.jpg",
        "./assets/PRODUCTS/F50 Firm Ground Angle 2.jpg"
    ],
    [
        "./assets/PRODUCTS/Predator Firm Ground Angle 1.png",
        "./assets/PRODUCTS/Predator Firm Ground Angle 2.png",
        "./assets/PRODUCTS/Puma Firm Ground Angle 1.png",
        "./assets/PRODUCTS/New Balance Firm Ground Angle 1.png",
        "./assets/PRODUCTS/Mizuno Turf Angle 1.png",
        "./assets/PRODUCTS/Mizuno Turf Angle 2.png"
    ]
]

templates = [
    ("Phantom GX 2", "Nike", "Controlo"),
    ("Mercurial Vapor 16", "Nike", "Velocidade"),
    ("F50 League", "Adidas", "Velocidade"),
    ("Predator Elite", "Adidas", "Precisão"),
    ("Future Ultimate", "Puma", "Agilidade"),
    ("Ultra Ultimate", "Puma", "Velocidade"),
    ("Tekela V4 Pro", "New Balance", "Controlo"),
    ("Furon V7 Pro", "New Balance", "Velocidade"),
    ("Morelia Neo IV", "Mizuno", "Clássico"),
    ("Top Flex Rebound", "Joma", "Clássico")
]

products = []

for i in range(1, 501):
    name_prefix, brand, silo = random.choice(templates)
    cat = random.choice(categories)
    surf = random.choice(surfaces[cat])
    level = random.choice(levels)
    price = random.choice([4500, 6800, 8900, 12500, 15800, 18500, 19200, 21500])
    
    prod_id = f"{brand.lower()}-{name_prefix.lower().replace(' ', '-')}-{surf.lower()}-{i}"
    
    base_pool = random.choice(angle_pools)
    gallery = list(base_pool)
    random.shuffle(gallery)
    
    main_angle = gallery[0]
    hover_angle = gallery[1]
    
    prod = {
        "id": prod_id,
        "name": f"{brand} {name_prefix} {surf} #{i}",
        "silo": silo,
        "level": level,
        "brand": brand,
        "category": cat,
        "surface": surf,
        "price": price,
        "badge": "Edição Especial" if i % 10 == 0 else ("Mais Vendido" if i % 7 == 0 else "Stock Verificado"),
        "subtitle": {
            "pt": f"Chuteira {brand} {level} de alta performance para {surf}.",
            "en": f"High performance {brand} {level} boots for {surf}."
        },
        "description": {
            "pt": f"Edição {level} desenhada para tração elite e controlo superior no relvado {surf}. Tamanhos disponíveis do 35 ao 46.",
            "en": f"{level} edition engineered for elite traction and ball control on {surf} pitches. Sizes 35 to 46 available."
        },
        "image": main_angle,
        "hoverImage": hover_angle,
        "gallery": gallery,
        "sizes": standard_sizes,
        "color": random.choice(colors),
        "inStock": True
    }
    products.append(prod)

dest_dir = "Official Website/assets/data"
os.makedirs(dest_dir, exist_ok=True)

with open(os.path.join(dest_dir, "products.json"), "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"Successfully generated 500 products with sizes 35 to 46 in {dest_dir}/products.json!")
