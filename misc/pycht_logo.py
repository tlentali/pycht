import svgwrite
import base64

def embed_font_base64(font_path):
    with open(font_path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    return f"""
    @font-face {{
        font-family: 'Cloister Black';
        src: url(data:font/truetype;charset=utf-8;base64,{encoded}) format('truetype');
    }}
    """

def generate_svg_with_embedded_font(word, font_path, font_size=100, fill_color='black', output_file='output.svg'):
    dwg = svgwrite.Drawing(output_file, profile='full', size=('275px', '170px'))

    font_css = embed_font_base64(font_path)
    dwg.defs.add(dwg.style(font_css))

    dwg.add(dwg.text(
        word,
        insert=(5, font_size),
        fill=fill_color,
        font_family='Cloister Black',
        font_size=font_size
    ))

    dwg.save()
    print(f"SVG with embedded font saved as {output_file}")

generate_svg_with_embedded_font(
    word='Pycht',
    font_path='../../../Downloads/cloister-black-font/CloisterBlackLight-axjg.ttf',
    font_size=120,
    fill_color='#f60386',
    output_file='pycht_logo.svg'
)
