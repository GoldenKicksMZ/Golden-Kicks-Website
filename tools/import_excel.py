import os
import json
import openpyxl
from io import BytesIO
from PIL import Image

def import_excel_catalogs():
    excel_files = [
        ("catalog_futsal.xlsx", "IC", "Futsal / Indoor"),
        ("catalog_campo.xlsx", "FG", "Campo / Firm Ground"),
        ("catalog_society.xlsx", "TF", "Society / Turf")
    ]

    products = []
    total_images_saved = 0

    products_dir = os.path.join("Official Website", "assets", "PRODUCTS")
    os.makedirs(products_dir, exist_ok=True)

    for filename, default_surface, default_surface_name in excel_files:
        if not os.path.exists(filename):
            print(f"Skipping missing catalog: {filename}")
            continue

        wb = openpyxl.load_workbook(filename, data_only=True)
        ws = wb.active

        # Map drawing images attached to cell (row, col) coordinates
        # col is 1-indexed (col 13 is angle1, 14 angle2, etc.)
        cell_images = {}
        if hasattr(ws, '_images'):
            for img in ws._images:
                try:
                    r = img.anchor._from.row + 1   # 1-indexed row
                    c = img.anchor._from.col + 1   # 1-indexed col
                    cell_images[(r, c)] = img
                except Exception:
                    pass

        row_num = 1
        for row in ws.iter_rows(min_row=2, values_only=False):
            row_num += 1
            vals = [cell.value for cell in row]

            sku = str(vals[0]).strip() if len(vals) > 0 and vals[0] else f"GK-PROD-{row_num:03d}"
            name = str(vals[1]).strip() if len(vals) > 1 and vals[1] else ""
            brand = str(vals[2]).strip() if len(vals) > 2 and vals[2] else ""
            silo = str(vals[3]).strip() if len(vals) > 3 and vals[3] else "Pro Line"
            level = str(vals[4]).strip() if len(vals) > 4 and vals[4] else "Elite"
            category = str(vals[5]).strip() if len(vals) > 5 and vals[5] else "Chuteiras"
            surface = str(vals[6]).strip() if len(vals) > 6 and vals[6] else default_surface
            
            if not name and len(vals) < 2:
                continue
            if not name and not brand:
                continue

            # Price
            try:
                price = float(vals[7]) if len(vals) > 7 and vals[7] is not None else 0.0
            except ValueError:
                price = 0.0

            color = str(vals[8]).strip() if len(vals) > 8 and vals[8] else "White / Gold"

            # Sizes
            sizes_val = vals[9] if len(vals) > 9 else ""
            if isinstance(sizes_val, (int, float)):
                sizes = [int(sizes_val)]
            elif isinstance(sizes_val, str) and sizes_val.strip():
                sizes = []
                for part in sizes_val.replace(";", ",").split(","):
                    try:
                        sizes.append(int(float(part.strip())))
                    except ValueError:
                        pass
                if not sizes:
                    sizes = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
            else:
                sizes = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

            description = str(vals[10]).strip() if len(vals) > 10 and vals[10] else f"Chuteira oficial {brand} {name} com máxima estabilidade e controlo superior."
            badge = str(vals[11]).strip() if len(vals) > 11 and vals[11] else "Novo"

            # Process 6 angle columns (index 12 through 17 -> excel columns 13 to 18)
            angles = []
            for angle_idx in range(6):
                col_idx = 13 + angle_idx
                val_idx = 12 + angle_idx
                
                img_val = str(vals[val_idx]).strip() if len(vals) > val_idx and vals[val_idx] else ""

                # Check if cell has a pasted picture object!
                if (row_num, col_idx) in cell_images:
                    img_obj = cell_images[(row_num, col_idx)]
                    try:
                        img_data = img_obj._data()
                        image = Image.open(BytesIO(img_data))
                        
                        clean_sku = sku.lower().replace(" ", "-")
                        img_filename = f"{clean_sku}-angle{angle_idx+1}.png"
                        save_path = os.path.join(products_dir, img_filename)
                        image.save(save_path)
                        
                        img_val = f"./assets/PRODUCTS/{img_filename}"
                        total_images_saved += 1
                    except Exception as e:
                        print(f"Error saving pasted image at row {row_num}, col {col_idx}: {e}")

                if img_val:
                    angles.append(img_val)

            if not angles:
                angles = ["./assets/logo.png"]

            main_image = angles[0]
            hover_image = angles[1] if len(angles) > 1 else main_image

            if not brand and name:
                brand = name.split()[0]

            surface_name = "Futsal / Indoor" if surface == "IC" else ("Society / Turf" if surface == "TF" else "Campo / Firm Ground")

            product_entry = {
                "id": sku,
                "sku": sku,
                "name": name,
                "brand": brand,
                "silo": silo,
                "level": level,
                "category": category,
                "subtitle": f"Chuteira {brand} {surface_name}",
                "description": description,
                "price": price,
                "badge": badge,
                "surface": surface,
                "surfaceName": surface_name,
                "image": main_image,
                "hoverImage": hover_image,
                "sizes": sizes,
                "color": color,
                "gallery": angles
            }
            products.append(product_entry)

    out_json = os.path.join("Official Website", "assets", "data", "products.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    print(f"\nSUCCESS: Imported {len(products)} products across all 3 Excel catalogs.")
    print(f"Extracted and saved {total_images_saved} pasted cell images.")
    print(f"Updated JSON database at {out_json}")

if __name__ == "__main__":
    import_excel_catalogs()
