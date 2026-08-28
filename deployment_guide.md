# Golden Kicks — Deployment & Continuous Updates Guide

This guide walks you through setting up automatic updates for your **Golden Kicks** storefront using **GitHub Actions** or **cPanel Git Version Control**.

---

## Option 1: Automatic GitHub Actions Deployment (Recommended)

Whenever you edit text, photos, logos, or products on your computer and push to GitHub, **GitHub Actions** will automatically sync your changes live to your cPanel host via FTP in ~15 seconds.

### Steps to Configure:

1. **Create/Push to GitHub**:
   - Initialize and push your project to a GitHub repository (e.g., `https://github.com/your-username/golden-kicks-website`).

2. **Configure GitHub Repository Secrets**:
   - Go to your GitHub repository: **Settings** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
   - Click **New repository secret** for each of the following 3 variables:

     | Secret Name | Description / Value |
     | :--- | :--- |
     | `FTP_SERVER` | Your website FTP host (e.g. `ftp.goldenkicks.co.mz` or server IP) |
     | `FTP_USERNAME` | Your cPanel FTP username |
     | `FTP_PASSWORD` | Your cPanel FTP password |

3. **How to Trigger Live Updates**:
   - Every time you push a change to the `main` or `master` branch, GitHub Actions automatically deploys the updated files inside `./Official Website/` straight to your live `public_html/` folder!

---

## Option 2: cPanel Git Version Control (1-Click cPanel Deploy)

If you prefer using cPanel's built-in Git tool (found in Softaculous / cPanel Tools):

### Steps to Configure:

1. Open `.cpanel.yml` in your project repository.
2. Edit line 4 to include your actual cPanel username:
   ```yaml
   ---
   deployment:
     tasks:
       - export DEPLOYPATH=/home/YOUR_CPANEL_USERNAME/public_html/
       - /bin/cp -R "Official Website/"* $DEPLOYPATH
   ```
3. In **cPanel**, go to **Git Version Control** $\rightarrow$ **Create Repository**.
4. Paste your GitHub repository URL and set the repository path.
5. Click **Create**.
6. When updating, click **Manage** $\rightarrow$ **Deploy Head Commit**. cPanel will pull the latest version and update your live website instantly!

---

## Summary of Editing Live Content

| Content | File Path in Repository / cPanel | How to Update |
| :--- | :--- | :--- |
| **Products & Prices** | `assets/data/products.json` | Edit JSON directly or run `python import_csv.py my_catalog.csv` |
| **Logo & Header Images** | `assets/LOGO/golden-kicks-logo.png` | Upload new PNG with same filename |
| **Brand Vectors** | `assets/BRANDS/*.svg` | Upload SVG vectors into `assets/BRANDS/` |
| **Header Text / Banners** | `Official Website/index.html` | Edit text in `index.html` and commit/push |
