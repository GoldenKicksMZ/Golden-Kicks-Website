const fs = require('fs');
const path = require('path');

const themeDir = path.join(__dirname, 'tgolden-kicks-extracted', 'tgolden-kicks');
const frontPagePath = path.join(themeDir, 'templates', 'front-page.html');

let content = fs.readFileSync(frontPagePath, 'utf8');

// Strip all HTML comments that do NOT start with " wp:" or " /wp:"
content = content.replace(/<!--(?!\s*\/?wp:).*?-->/gs, '');

fs.writeFileSync(frontPagePath, content, 'utf8');
console.log('Stripped regular HTML comments to prevent Gutenberg parser crashes.');
