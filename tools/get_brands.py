import urllib.request
import urllib.parse
import json

def download_wikimedia_svg(file_title, dest_filename):
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for k, v in pages.items():
            imageinfo = v.get('imageinfo', [])
            if imageinfo:
                svg_url = imageinfo[0]['url']
                print(f"Downloading {file_title} from {svg_url}")
                svg_req = urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(svg_req) as s_resp:
                    content = s_resp.read().decode('utf-8')
                    with open(dest_filename, 'w', encoding='utf-8') as out:
                        out.write(content)
                    print(f"Saved {dest_filename} ({len(content)} bytes)")

download_wikimedia_svg("File:MIZUNO logo.svg", "Official Website/assets/BRANDS/mizuno.svg")
download_wikimedia_svg("File:Joma Sport.svg", "Official Website/assets/BRANDS/joma.svg")
