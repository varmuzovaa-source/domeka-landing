"""Rebuild the two-page guide from pruvodce.html. Requires reportlab and beautifulsoup4."""
from pathlib import Path
from xml.sax.saxutils import escape
from bs4 import BeautifulSoup
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
root=Path(__file__).resolve().parent.parent
fontdir=Path('/System/Library/Fonts/Supplemental')
pdfmetrics.registerFont(TTFont('Guide',str(fontdir/'Arial.ttf')))
pdfmetrics.registerFont(TTFont('GuideBold',str(fontdir/'Arial Bold.ttf')))
pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='GuideBold',italic='Guide',boldItalic='GuideBold')
ink=HexColor('#14232A'); ocean=HexColor('#0E3138'); muted=HexColor('#4B5A60')
styles={
 'body':ParagraphStyle('body',fontName='Guide',fontSize=10.3,leading=14,textColor=ink,spaceAfter=5),
 'lead':ParagraphStyle('lead',fontName='Guide',fontSize=11,leading=15,textColor=muted,spaceAfter=13),
 'h1':ParagraphStyle('h1',fontName='GuideBold',fontSize=22,leading=25,textColor=ocean,spaceAfter=12),
 'h2':ParagraphStyle('h2',fontName='GuideBold',fontSize=12.5,leading=16,textColor=ocean,spaceBefore=9,spaceAfter=4),
 'h3':ParagraphStyle('h3',fontName='GuideBold',fontSize=12,leading=16,textColor=ocean,spaceBefore=13,spaceAfter=7),
 'fine':ParagraphStyle('fine',fontName='Guide',fontSize=9,leading=12,textColor=muted,spaceAfter=7),
 'warn':ParagraphStyle('warn',fontName='Guide',fontSize=10.3,leading=14,textColor=HexColor('#7A2E1B'),spaceAfter=7),
}
def content(el):
 return ''.join(str(c) for c in el.contents)
def para(el,style='body'):
 return Paragraph(content(el),styles[style])
soup=BeautifulSoup((root/'src/pruvodce.html').read_text(),'html.parser')
flow=[]
for pi,sec in enumerate(soup.select('section.pg')):
 if pi:flow.append(PageBreak())
 for el in sec.find_all(recursive=False):
  if 'top' in el.get('class',[]) or 'foot' in el.get('class',[]):continue
  if el.name in ('h1','h3'):flow.append(para(el,el.name))
  elif el.name=='p':flow.append(para(el,'lead' if 'lead' in el.get('class',[]) else 'fine' if 'fine' in el.get('class',[]) else 'body'))
  elif 'q' in el.get('class',[]):
   block=[Paragraph(escape(el.select_one('.n').get_text())+'. '+escape(el.h2.get_text()),styles['h2'])]
   block += [para(p,'warn' if 'w' in p.get('class',[]) else 'body') for p in el.find_all('p',recursive=False)]
   flow.extend([KeepTogether(block),Spacer(1,3)])
  elif el.name=='table':
   rows=[[Paragraph(escape(c.get_text()),styles['fine']) for c in tr.find_all(['th','td'])] for tr in el.find_all('tr')]
   table=Table(rows,colWidths=[113,113,113,113],repeatRows=1,hAlign='LEFT')
   table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#E8F2EF')),('LINEBELOW',(0,0),(-1,-1),.5,HexColor('#CBD5D8')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),5),('VALIGN',(0,0),(-1,-1),'TOP')]))
   flow.extend([table,Spacer(1,8)])
  elif el.name=='ul':
   for li in el.find_all('li',recursive=False):flow.append(Paragraph('• '+escape(li.get_text()),styles['body']))
  elif 'box' in el.get('class',[]):
   box=Table([[para(el)]],colWidths=[452]);box.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,ocean),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),7)]));flow.extend([Spacer(1,9),box])
def decorate(c,doc):
 c.setFillColor(ocean);c.setFont('GuideBold',9);c.drawString(18*mm,282*mm,'DOMEKA · PRŮVODCE INVESTORA');c.drawRightString(192*mm,282*mm,f'Strana {doc.page} ze 2');c.setStrokeColor(ocean);c.line(18*mm,279*mm,192*mm,279*mm)
 p=Paragraph('Domeka je fiktivní projekt pro výběrový úkol. Údaje jsou modelové. Tento materiál není investičním doporučením ani prospektem.',styles['fine']);p.wrap(174*mm,30);p.drawOn(c,18*mm,12*mm)
out=root/'assets/Domeka-Pet-otazek-pred-nakupem-dluhopisu.pdf'
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=23*mm,bottomMargin=29*mm,title='Pět otázek před nákupem firemního dluhopisu',author='Domeka — modelový projekt').build(flow,onFirstPage=decorate,onLaterPages=decorate)
print(out)
