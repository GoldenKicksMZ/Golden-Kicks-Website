const fs = require('fs');
const path = require('path');

const logoSrc = 'C:/Users/neyton/.gemini/antigravity/brain/19ca4b60-97e1-4715-be82-e319e4e9f9b1/.user_uploaded/media_1785962314922.png';

const targetDirs = [
  'Official Website/assets/LOGO',
  'golden-kicks-wp-editable-theme/assets/LOGO',
  'golden-kicks/assets/LOGO',
  'goldenkicks-theme/assets/LOGO',
  'assets/LOGO'
];

targetDirs.forEach(dir => {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.copyFileSync(logoSrc, path.join(dir, 'golden-kicks-logo.png'));
  console.log('Copied logo to', dir);
});

function replaceInFile(filePath, targets) {
  if (!fs.existsSync(filePath)) return;
  let content = fs.readFileSync(filePath, 'utf8');
  let updated = content;
  targets.forEach(t => {
    updated = updated.replace(t.regex, t.replacement);
  });
  if (updated !== content) {
    fs.writeFileSync(filePath, updated);
    console.log('Updated file:', filePath);
  }
}

replaceInFile('golden-kicks-wp-editable-theme/parts/header.html', [
  { regex: /<span class="gk-logo-fallback">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img src="./assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-10 w-auto object-contain scale-[3.2] origin-center">' }
]);

replaceInFile('golden-kicks-wp-editable-theme/_qa/preview.html', [
  { regex: /<span class="gk-logo-fallback">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img src="./assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-10 w-auto object-contain scale-[3.2] origin-center">' }
]);

replaceInFile('golden-kicks/template-parts/official-app-shell.php', [
  { regex: /<span class="font-display font-bold text-\[18px\] tracking-tight text-black flex items-center justify-center">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img src="<?php echo get_template_directory_uri(); ?>/assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-7 w-auto object-contain scale-[2.8] origin-left">' },
  { regex: /<span id="desktop-header-logo" class="font-display font-bold text-\[22px\] tracking-tight text-black flex items-center justify-center">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img id="desktop-header-logo" src="<?php echo get_template_directory_uri(); ?>/assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-10 w-auto object-contain scale-[3.2] origin-center">' },
  { regex: /<span class="font-display font-bold text-\[20px\] tracking-tight text-black flex items-center justify-center">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img src="<?php echo get_template_directory_uri(); ?>/assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-7 w-auto object-contain scale-[3.0] origin-center">' }
]);

replaceInFile('goldenkicks-theme/header.php', [
  { regex: /<span class="font-display font-bold text-\[18px\] tracking-tight text-black flex items-center justify-center">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img src="<?php echo get_template_directory_uri(); ?>/assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-7 w-auto object-contain scale-[2.8] origin-left">' },
  { regex: /<span id="desktop-header-logo" class="font-display font-bold text-\[22px\] tracking-tight text-black flex items-center justify-center">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img id="desktop-header-logo" src="<?php echo get_template_directory_uri(); ?>/assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-10 w-auto object-contain scale-[3.2] origin-center">' },
  { regex: /<span class="font-display font-bold text-\[20px\] tracking-tight text-black flex items-center justify-center">\[Inserir Logo Aqui\]<\/span>/g, replacement: '<img src="<?php echo get_template_directory_uri(); ?>/assets/LOGO/golden-kicks-logo.png" alt="Golden Kicks" class="h-7 w-auto object-contain scale-[3.0] origin-center">' }
]);

console.log('All logo updates done.');
