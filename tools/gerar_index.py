"""Gera o index.html (página completa para o GitHub Pages) a partir do banner-elas.html.

O banner-elas.html é a mesma página publicada no Claude, que ganha o cabeçalho
<!doctype>/<head> automaticamente. Aqui montamos esse cabeçalho à mão.

Uso: python tools/gerar_index.py
"""
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
banner = (raiz / "banner-elas.html").read_text(encoding="utf-8")

corte = banner.index('<div id="progress"')
cabeca, corpo = banner[:corte].strip(), banner[corte:].strip()

pagina = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Banner interativo sobre violência contra a mulher: folha A4 para desenhar, tipos de violência, ciberviolência, fisiologia do estresse e rede de apoio em Macapá e no Amapá.">
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{cabeca}
</head>
<body>
{corpo}
</body>
</html>
"""
(raiz / "index.html").write_text(pagina, encoding="utf-8", newline="\n")
print("index.html gerado")
