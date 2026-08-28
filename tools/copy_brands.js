const fs = require('fs');
const path = require('path');

const brands = ['nike', 'adidas', 'puma', 'newbalance', 'mizuno', 'joma'];
const srcDir = 'Official Website/assets/BRANDS';

const targetDirs = [
  'Official Website/assets/BRANDS',
  'golden-kicks-wp-editable-theme/assets/BRANDS',
  'golden-kicks/assets/BRANDS',
  'goldenkicks-theme/assets/BRANDS',
  'assets/BRANDS'
];

targetDirs.forEach(dir => {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  brands.forEach(b => {
    const file = `${b}.svg`;
    fs.copyFileSync(path.join(srcDir, file), path.join(dir, file));
  });
  console.log('Copied all 6 brand SVGs to:', dir);
});
