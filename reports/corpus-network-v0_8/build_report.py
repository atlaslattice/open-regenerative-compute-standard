"""Render the public markdown white paper and appendices to an accessible PDF."""
import csv
import html
import re
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT=Path(__file__).resolve().parent
PDF=ROOT/'output/pdf/Atlas_Corpus_Network_White_Paper_v0_8.pdf'
FONT='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Atlas',FONT+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('AtlasBold',FONT+'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('Atlas',normal='Atlas',bold='AtlasBold',italic='Atlas',boldItalic='AtlasBold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyAtlas',fontName='Atlas',fontSize=9,leading=13,spaceAfter=7,textColor=colors.HexColor('#24333d')))
styles.add(ParagraphStyle(name='TitleAtlas',fontName='AtlasBold',fontSize=27,leading=33,spaceAfter=14,textColor=colors.HexColor('#123d4c')))
styles.add(ParagraphStyle(name='H1Atlas',fontName='AtlasBold',fontSize=16,leading=21,spaceBefore=16,spaceAfter=9,keepWithNext=True,textColor=colors.HexColor('#123d4c')))
styles.add(ParagraphStyle(name='H2Atlas',fontName='AtlasBold',fontSize=11,leading=15,spaceBefore=10,spaceAfter=7,keepWithNext=True,textColor=colors.HexColor('#176878')))
styles.add(ParagraphStyle(name='CellAtlas',fontName='Atlas',fontSize=7.2,leading=10,spaceAfter=0))
styles.add(ParagraphStyle(name='RefAtlas',fontName='Atlas',fontSize=7.5,leading=11,spaceAfter=8,splitLongWords=True))

def fmt(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`(.*?)`',r'<font color="#176878">\1</font>',s)
    return s

def table(rows,width):
    n=len(rows[0]);ratios={3:[.43,.23,.34],4:[.22,.23,.23,.32],5:[.08,.25,.22,.13,.32]}.get(n,[1/n]*n)
    cells=[[Paragraph(fmt(x),styles['CellAtlas']) for x in row] for row in rows]
    t=Table(cells,colWidths=[width*x for x in ratios],repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([
      ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcebf0')),
      ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f4f7f8')]),
      ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),
      ('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),
      ('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#91abb5'))]))
    return t

def footer(canvas,doc):
    canvas.saveState();w,h=A4
    canvas.setFont('Atlas',7);canvas.setFillColor(colors.HexColor('#607783'))
    canvas.drawString(42,25,'ATLAS LATTICE | CORPUS NETWORK | v0.8 | 24 OCT 2026 | SCREENING ONLY')
    canvas.drawRightString(w-42,25,str(doc.page));canvas.restoreState()

def render():
    story=[];lines=(ROOT/'WHITE_PAPER.md').read_text().splitlines();i=0;refs=False
    width=A4[0]-84
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[: -]+',x) for x in row):rows.append(row)
                i+=1
            story.append(table(rows,width));story.append(Spacer(1,9));continue
        if line.startswith('# '):story.append(Paragraph(fmt(line[2:]),styles['TitleAtlas']))
        elif line.startswith('## '):
            refs='References and provenance' in line
            story.append(Paragraph(fmt(line[3:]),styles['H1Atlas']))
        elif line.startswith('### '):story.append(Paragraph(fmt(line[4:]),styles['H2Atlas']))
        else:
            para=[line];i+=1
            while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|')):
                para.append(lines[i].strip());i+=1
            story.append(Paragraph(fmt(' '.join(para)),styles['RefAtlas'] if refs else styles['BodyAtlas']));continue
        i+=1
    story.append(PageBreak());story.append(Paragraph('Appendix A. All retained price anchors',styles['H1Atlas']))
    story.append(Paragraph('User-supplied DeepSeek claims, 24 October 2026. NEEDS SOURCING URLS. USD at assumed CNY7.25/USD. Imported comparisons are excluded from proposed Chinese-supply packages. No prices are summed into an installed budget.',styles['BodyAtlas']))
    rows=[['ID','Item / scope','USD reference','Price type','Open issue']]
    for r in csv.DictReader((ROOT/'price_anchor_comparison.csv').open()):
        lo=float(r['china_equipment_anchor_usd_low']);hi=float(r['china_equipment_anchor_usd_high'])
        price=f'${lo:,.2f}' if lo==hi else f'${lo:,.2f}-${hi:,.2f}'
        rows.append([r['anchor_id'],r['item'],price+'; '+r['quoted_unit'].replace('CNY','USD'),r['anchor_kind'].replace('_',' '),r['scope_limitation']+'; '+r['proposed_chinese_package_status']])
    story.append(table(rows,width))
    story.append(PageBreak());story.append(Paragraph('Appendix B. Thirty candidate modules',styles['H1Atlas']))
    rows=[['ID','Module','Candidate','Node','Principal unresolved gate']]
    for r in csv.DictReader((ROOT/'module_register.csv').open()):rows.append([r['module_id'],r['module'],r['candidate_supplier'],r['node'],r['open_gate']])
    story.append(table(rows,width))
    PDF.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(PDF),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=42,
        title='Atlas Lattice Corpus Christi: Networked Retrofits, Desalination, Landfill Mining and Compute',
        author='Atlas Lattice research / prepared with GPT for Dave Sheldon')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(PDF)

if __name__=='__main__':render()
