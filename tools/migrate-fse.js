const fs = require('fs');
const path = require('path');

const themeDir = path.join(__dirname, 'tgolden-kicks-extracted', 'goldenkicks-fse-theme');
const appShellPath = path.join(themeDir, 'template-parts', 'official-app-shell.php');
const frontPageHtmlPath = path.join(themeDir, 'templates', 'front-page.html');

let shellContent = fs.readFileSync(appShellPath, 'utf8');

// Remove the PHP opening tag and comments
shellContent = shellContent.replace(/<\?php[\s\S]*?\?>/, '').trim();

// Wrap the content in wp:html blocks, splitting where [Inserir Logo Aqui] is.
const parts = shellContent.split('[Inserir Logo Aqui]');

let fseHtml = '';

for (let i = 0; i < parts.length; i++) {
    fseHtml += '<!-- wp:html -->\n' + parts[i] + '\n<!-- /wp:html -->\n';
    
    // If not the last part, insert the site logo block
    if (i < parts.length - 1) {
        fseHtml += '<!-- wp:site-logo {"width":120,"className":"gk-site-logo"} /-->\n';
    }
}

// Write to front-page.html
fs.writeFileSync(frontPageHtmlPath, fseHtml, 'utf8');
console.log('Successfully generated front-page.html with FSE Custom HTML blocks and Site Logo.');

// Also we should delete the template-parts/official-app-shell.php since it's no longer needed?
// No, let's keep it just in case, it doesn't hurt if it's not loaded by any PHP file.

// We should also ensure the Site Editor can load.
// If index.php is gone, WordPress requires templates/index.html. Let's make sure it exists.
const indexHtmlPath = path.join(themeDir, 'templates', 'index.html');
if (!fs.existsSync(indexHtmlPath)) {
    console.log('Creating index.html fallback...');
    fs.writeFileSync(indexHtmlPath, '<!-- wp:group --><main><h1>Fallback</h1></main><!-- /wp:group -->', 'utf8');
}
