# Golden Kicks — Official Website & Product Catalogs

Welcome to the official repository for **Golden Kicks** (Mozambique).

---

## 📁 Repository Structure

- 📁 **`Official Website/`**: Production web application (SPA with single-file shell, Tailwind CSS, Lucide Icons, and multi-language PT/EN support).
- 📊 **Excel Product Catalogs**:
  - 👟 [`catalog_futsal.xlsx`](./catalog_futsal.xlsx) (Indoor / IC boots)
  - ⚽ [`catalog_campo.xlsx`](./catalog_campo.xlsx) (Firm Ground / FG / AG boots)
  - 🌿 [`catalog_society.xlsx`](./catalog_society.xlsx) (Turf / TF boots)
- 📁 **`tools/`**: Automated python scripts for catalog management:
  - `import_excel.py`: Parses Excel catalogs & cell images into `products.json`.
  - `build_excel_catalogs.py`: Generates formatted 18-column Excel spreadsheets.
  - `export_cpanel_zip.py`: Packages the website for cPanel deployment.
- ⚙️ **`.cpanel.yml`**: Automatic cPanel deployment task configuration.
- 📄 **`deployment_guide.md`**: Full instructions for cPanel & GitHub integration.

---

## 🛠️ How to Update Products & Prices

1. Open any of the 3 Excel files (`catalog_futsal.xlsx`, `catalog_campo.xlsx`, or `catalog_society.xlsx`) in Microsoft Excel.
2. Edit product details or paste boot images directly into the `angle1` through `angle6` cells.
3. Run the automated importer:
   ```bash
   python tools/import_excel.py
   ```
4. Push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Update product catalog"
   git push origin main
   ```
5. In cPanel **Git Version Control**, click **Update from Remote** ➔ **Deploy HEAD Commit**.

---

© Golden Kicks Mozambique. All rights reserved.
