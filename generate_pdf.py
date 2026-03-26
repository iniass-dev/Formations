# -*- coding: utf-8 -*-
"""
Génération du support de formation Odoo 18 RH en PDF
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_DIR = r'C:\Windows\Fonts'
FONT_REGULAR = FONT_DIR + r'\arial.ttf'
FONT_BOLD    = FONT_DIR + r'\arialbd.ttf'
FONT_ITALIC  = FONT_DIR + r'\ariali.ttf'
FONT_BOLDITALIC = FONT_DIR + r'\arialbi.ttf'

# ─── Palette de couleurs ─────────────────────────────────────────────────────
ODOO_PURPLE   = (113, 75, 168)   # violet Odoo
ODOO_DARK     = (40,  30,  60)   # titres sombres
ACCENT_BLUE   = (52, 120, 190)   # sous-titres / liens
LIGHT_BG      = (248, 246, 252)  # fond des encadrés
TABLE_HEADER  = (113, 75, 168)   # en-tête tableau
TABLE_ROW_ALT = (243, 240, 250)  # ligne alternée
WHITE         = (255, 255, 255)
GRAY_TEXT     = (100, 100, 110)
WARN_BG       = (255, 248, 230)
WARN_BORDER   = (230, 170, 50)
TIP_BG        = (230, 248, 240)
TIP_BORDER    = (50, 180, 120)
DARK_TEXT     = (30, 25, 45)
LIGHT_GRAY    = (220, 215, 230)


class OdooFormationPDF(FPDF):

    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=22)
        self.set_margins(18, 18, 18)
        self._module_num = 0
        self._toc = []
        self.add_font('Arial', style='',   fname=FONT_REGULAR)
        self.add_font('Arial', style='B',  fname=FONT_BOLD)
        self.add_font('Arial', style='I',  fname=FONT_ITALIC)
        self.add_font('Arial', style='BI', fname=FONT_BOLDITALIC)
        
    # ─── En-tête de page ──────────────────────────────────────────────────
    def header(self):
        if self.page_no() == 1:
            return
        self.set_fill_color(*ODOO_PURPLE)
        self.rect(0, 0, 210, 10, 'F')
        self.set_y(2.5)
        self.set_font('Arial', 'B', 8)
        self.set_text_color(*WHITE)
        self.cell(0, 5, 'Formation Odoo 18 -- Gestion RH : Employés, Départements et Contrats',
                  align='C')
        self.set_text_color(*DARK_TEXT)
        self.ln(10)

    # ─── Pied de page ─────────────────────────────────────────────────────
    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-14)
        self.set_draw_color(*LIGHT_GRAY)
        self.set_line_width(0.3)
        self.line(18, self.get_y(), 192, self.get_y())
        self.ln(1.5)
        self.set_font('Arial', '', 7.5)
        self.set_text_color(*GRAY_TEXT)
        self.cell(0, 5, f'Page {self.page_no()}', align='C')

    # ─── Page de garde ────────────────────────────────────────────────────
    def cover_page(self):
        self.add_page()
        # Fond haut
        self.set_fill_color(*ODOO_PURPLE)
        self.rect(0, 0, 210, 110, 'F')
        # Motif déco (cercles transparents)
        self.set_draw_color(150, 120, 200)
        self.set_line_width(0.4)
        for r, x, y in [(55, 170, 20), (40, 15, 80), (30, 140, 90)]:
            self.ellipse(x - r, y - r, r * 2, r * 2, 'D')

        # Logo / titre principal
        self.set_y(28)
        self.set_font('Arial', 'B', 36)
        self.set_text_color(*WHITE)
        self.cell(0, 14, 'ODOO 18', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font('Arial', '', 16)
        self.cell(0, 8, 'Support de Formation', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)
        # Ligne blanche
        self.set_draw_color(*WHITE)
        self.set_line_width(0.6)
        cx = 105
        self.line(cx - 55, self.get_y(), cx + 55, self.get_y())
        self.ln(5)
        self.set_font('Arial', 'B', 22)
        self.multi_cell(0, 10,
            'Gestion des Employés,\nDépartements et Contrats',
            align='C')

        # Bloc info
        self.set_y(118)
        self.set_fill_color(*LIGHT_BG)
        self.rect(30, 116, 150, 52, 'F')
        self.set_draw_color(*ODOO_PURPLE)
        self.set_line_width(0.5)
        self.rect(30, 116, 150, 52)

        self.set_y(120)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(*ODOO_PURPLE)
        self.cell(0, 7, 'Informations sur la formation', align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

        infos = [
            ('Public cible',   'Responsables RH, Assistants RH, Gestionnaires'),
            ('Niveau',         'Débutant à intermédiaire'),
            ('Durée',          '1 journée -- 7 heures'),
            ('Prérequis',      'Navigation de base dans Odoo'),
            ('Version',        'Odoo 18.0'),
        ]
        self.set_font('Arial', '', 10)
        for label, val in infos:
            self.set_x(38)
            self.set_text_color(*ODOO_DARK)
            self.set_font('Arial', 'B', 10)
            self.cell(42, 6.5, label + ' :')
            self.set_font('Arial', '', 10)
            self.set_text_color(*DARK_TEXT)
            self.cell(0, 6.5, val, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Objectifs
        self.set_y(180)
        self.set_fill_color(*ODOO_PURPLE)
        self.rect(18, self.get_y(), 174, 8, 'F')
        self.set_font('Arial', 'B', 12)
        self.set_text_color(*WHITE)
        self.cell(0, 8, '  Objectifs de la formation', align='L',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        objectifs = [
            'Créer et organiser la structure hiérarchique des départements',
            'Créer et gérer les fiches employés complètes',
            'Établir et suivre les contrats de travail (CDI, CDD)',
            'Utiliser les filtres, regroupements et vues pour analyser les données RH',
            'Archiver, réactiver et corriger des enregistrements',
        ]
        self.set_font('Arial', '', 10.5)
        self.set_text_color(*DARK_TEXT)
        for obj in objectifs:
            self.set_x(22)
            self.set_text_color(*ODOO_PURPLE)
            self.cell(6, 7, '>')
            self.set_text_color(*DARK_TEXT)
            self.cell(0, 7, obj, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Pied de garde
        self.set_y(262)
        self.set_fill_color(*ODOO_DARK)
        self.rect(0, 262, 210, 35, 'F')
        self.set_font('Arial', '', 9)
        self.set_text_color(*WHITE)
        self.set_y(270)
        self.cell(0, 6, 'Version 1.0  --  Mars 2026', align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(180, 160, 220)
        self.cell(0, 5,
            'Basé sur la documentation officielle Odoo 18 -- odoo.com/documentation/18.0',
            align='C')

    # ─── Plan de la journée ───────────────────────────────────────────────
    def planning_page(self):
        self.add_page()
        self.section_title('Plan de la journée')

        planning = [
            ('09h00 - 09h30', 'Présentation de l\'interface RH',          '30 min'),
            ('09h30 - 11h00', 'Module 1 -- Les Départements',               '1h30'),
            ('11h00 - 12h30', 'Module 2 -- Les Employés',                   '1h30'),
            ('12h30 - 13h30', 'Pause déjeuner',                            '--'),
            ('13h30 - 15h30', 'Module 3 -- Les Contrats',                   '2h00'),
            ('15h30 - 16h30', 'Module 4 -- Recherche et rapports',          '1h00'),
            ('16h30 - 17h00', 'Exercice de synthèse + Questions/Réponses', '30 min'),
        ]
        cols = [38, 120, 22]
        headers = ['Horaire', 'Contenu', 'Durée']

        # En-tête du tableau
        self.set_fill_color(*TABLE_HEADER)
        self.set_text_color(*WHITE)
        self.set_font('Arial', 'B', 10)
        for i, (h, w) in enumerate(zip(headers, cols)):
            self.cell(w, 9, '  ' + h, border=0, fill=True,
                      new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.ln(9)

        self.set_font('Arial', '', 10)
        for idx, (h, c, d) in enumerate(planning):
            fill = idx % 2 == 1
            if h == '12h30 - 13h30':
                self.set_fill_color(230, 240, 255)
                self.set_text_color(*ACCENT_BLUE)
                self.set_font('Arial', 'I', 10)
            else:
                self.set_fill_color(*TABLE_ROW_ALT if fill else WHITE)
                self.set_text_color(*DARK_TEXT)
                self.set_font('Arial', '', 10)
            self.cell(cols[0], 8.5, '  ' + h, border=0, fill=True,
                      new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.cell(cols[1], 8.5, '  ' + c, border=0, fill=True,
                      new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font('Arial', 'B', 10)
            self.cell(cols[2], 8.5, d, border=0, fill=True, align='C',
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

        # Modules résumés (cartes)
        self.set_text_color(*DARK_TEXT)
        self.set_font('Arial', 'B', 11)
        self.cell(0, 8, 'Les 4 modules de la formation', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

        modules = [
            ('1', 'Départements',           'Structure hiérarchique de l\'entreprise',  ODOO_PURPLE),
            ('2', 'Employés',               'Fiches complètes et gestion des départs',   ACCENT_BLUE),
            ('3', 'Contrats',               'CDI, CDD, workflow et suivi',              (50, 160, 110)),
            ('4', 'Recherche & Rapports',   'Filtres, graphiques et exports',           (190, 100, 50)),
        ]

        x_start = self.get_x()
        y_start = self.get_y()
        card_w = 84
        card_h = 32
        gap = 6

        for i, (num, title, desc, color) in enumerate(modules):
            col = i % 2
            row = i // 2
            cx = x_start + col * (card_w + gap)
            cy = y_start + row * (card_h + gap)
            # Fond carte
            self.set_fill_color(248, 246, 252)
            self.rect(cx, cy, card_w, card_h, 'F')
            # Barre couleur gauche
            self.set_fill_color(*color)
            self.rect(cx, cy, 6, card_h, 'F')
            self.rect(cx + 3, cy, 3, card_h, 'F')
            # Numéro
            self.set_font('Arial', 'B', 20)
            self.set_text_color(*color)
            self.set_xy(cx + 9, cy + 4)
            self.cell(14, 10, num)
            # Titre
            self.set_font('Arial', 'B', 11)
            self.set_text_color(*ODOO_DARK)
            self.set_xy(cx + 24, cy + 6)
            self.cell(58, 7, title)
            # Description
            self.set_font('Arial', '', 8.5)
            self.set_text_color(*GRAY_TEXT)
            self.set_xy(cx + 24, cy + 16)
            self.multi_cell(58, 5, desc)

    # ─── Titre de section principale (module) ─────────────────────────────
    def module_title(self, num, title):
        self.add_page()
        self._module_num += 1
        self._toc.append((title, self.page_no()))
        # Bandeau violet plein
        self.set_fill_color(*ODOO_PURPLE)
        self.rect(0, 10, 210, 55, 'F')
        # Numéro grand (semi-transparent simulé avec couleur plus claire)
        self.set_font('Arial', 'B', 60)
        self.set_text_color(160, 130, 210)
        self.set_xy(130, 12)
        self.cell(60, 50, str(num))
        # Texte MODULE
        self.set_font('Arial', '', 11)
        self.set_text_color(200, 185, 230)
        self.set_xy(18, 20)
        self.cell(0, 8, f'MODULE {num}')
        # Titre
        self.set_font('Arial', 'B', 24)
        self.set_text_color(*WHITE)
        self.set_xy(18, 30)
        self.cell(0, 14, title)
        self.set_text_color(*DARK_TEXT)
        self.set_y(75)

    # ─── Titre de section (sous-module) ───────────────────────────────────
    def section_title(self, title, with_line=True):
        self.ln(3)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(*ODOO_PURPLE)
        self.cell(0, 9, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        if with_line:
            self.set_draw_color(*ODOO_PURPLE)
            self.set_line_width(0.5)
            self.line(self.get_x(), self.get_y(), self.get_x() + 174, self.get_y())
        self.ln(3)
        self.set_text_color(*DARK_TEXT)

    # ─── Sous-titre ───────────────────────────────────────────────────────
    def sub_title(self, title):
        self.ln(2)
        self.set_fill_color(*LIGHT_BG)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(*ODOO_DARK)
        self.cell(0, 7.5, '  ' + title, fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)
        self.set_text_color(*DARK_TEXT)

    # ─── Paragraphe ───────────────────────────────────────────────────────
    def para(self, text, indent=0):
        self.set_font('Arial', '', 10.5)
        self.set_text_color(*DARK_TEXT)
        if indent:
            self.set_x(self.get_x() + indent)
        self.multi_cell(0, 6.5, text)
        self.ln(1)

    # ─── Point de liste ───────────────────────────────────────────────────
    def bullet(self, text, level=0):
        indent = 6 + level * 5
        sym = '-' if level == 0 else '-'
        self.set_font('Arial', '', 10.5)
        self.set_text_color(*ODOO_PURPLE)
        self.set_x(self.l_margin + indent)
        self.cell(5, 6.5, sym)
        self.set_text_color(*DARK_TEXT)
        self.multi_cell(0, 6.5, text)

    # ─── Encadré "Remarque" ───────────────────────────────────────────────
    def note_box(self, text, kind='info'):
        self.ln(2)
        bg = WARN_BG if kind == 'warn' else TIP_BG
        border = WARN_BORDER if kind == 'warn' else TIP_BORDER
        icon = '[!]' if kind == 'warn' else '[i]'
        label = 'Attention' if kind == 'warn' else 'Remarque'

        self.set_fill_color(*bg)
        self.set_draw_color(*border)
        self.set_line_width(0.4)

        x0 = self.get_x()
        y0 = self.get_y()
        # Mesurer la hauteur
        self.set_font('Arial', '', 10)
        lines = self.multi_cell(150, 6, text, dry_run=True, output='LINES')
        h = max(14, len(lines) * 6 + 10)

        self.rect(x0, y0, 174, h, 'FD')
        self.set_fill_color(*border)
        self.rect(x0, y0, 4, h, 'F')

        self.set_xy(x0 + 8, y0 + 3)
        self.set_font('Arial', 'B', 10)
        self.set_text_color(*border)
        self.cell(20, 6, f'{icon}  {label} :')
        self.set_font('Arial', '', 10)
        self.set_text_color(*DARK_TEXT)
        self.set_xy(x0 + 8, y0 + 9)
        self.multi_cell(160, 6, text)
        self.ln(3)

    # ─── Chemin de navigation ─────────────────────────────────────────────
    def nav_path(self, path):
        self.ln(1)
        self.set_fill_color(235, 230, 248)
        self.set_font('Arial', 'B', 9.5)
        self.set_text_color(*ODOO_PURPLE)
        self.cell(0, 7.5, '   [+]  ' + path, fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)
        self.set_text_color(*DARK_TEXT)

    # ─── Étapes numérotées ────────────────────────────────────────────────
    def steps(self, items):
        self.set_font('Arial', '', 10.5)
        for i, item in enumerate(items, 1):
            self.set_x(self.l_margin + 4)
            self.set_fill_color(*ODOO_PURPLE)
            self.set_font('Arial', 'B', 9)
            self.set_text_color(*WHITE)
            # Petit badge numéroté
            y = self.get_y()
            self.rect(self.get_x(), y + 0.8, 6, 5.5, 'F')
            self.set_xy(self.get_x(), y + 0.8)
            self.cell(6, 5.5, str(i), align='C')
            self.set_font('Arial', '', 10.5)
            self.set_text_color(*DARK_TEXT)
            self.set_xy(self.l_margin + 12, y)
            self.multi_cell(0, 6.5, item)

    # ─── Tableau générique ────────────────────────────────────────────────
    def table(self, headers, rows, col_widths=None, row_h=8):
        if col_widths is None:
            w = 174 // len(headers)
            col_widths = [w] * len(headers)

        # En-tête
        self.set_fill_color(*TABLE_HEADER)
        self.set_text_color(*WHITE)
        self.set_font('Arial', 'B', 9.5)
        for h, w in zip(headers, col_widths):
            self.cell(w, 9, '  ' + h, fill=True,
                      new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.ln(9)

        # Lignes
        self.set_font('Arial', '', 9.5)
        for idx, row in enumerate(rows):
            self.set_fill_color(*TABLE_ROW_ALT if idx % 2 else WHITE)
            self.set_text_color(*DARK_TEXT)
            max_lines = 1
            # calcul hauteur ligne
            for cell, w in zip(row, col_widths):
                lines = self.multi_cell(w, row_h, '  ' + str(cell),
                                        dry_run=True, output='LINES')
                max_lines = max(max_lines, len(lines))
            h_row = max_lines * row_h
            if self.get_y() + h_row > self.page_break_trigger:
                self.add_page()
                # ré-afficher en-tête
                self.set_fill_color(*TABLE_HEADER)
                self.set_text_color(*WHITE)
                self.set_font('Arial', 'B', 9.5)
                for hh, w in zip(headers, col_widths):
                    self.cell(w, 9, '  ' + hh, fill=True,
                              new_x=XPos.RIGHT, new_y=YPos.TOP)
                self.ln(9)
                self.set_fill_color(*TABLE_ROW_ALT if idx % 2 else WHITE)
                self.set_text_color(*DARK_TEXT)
                self.set_font('Arial', '', 9.5)

            y0 = self.get_y()
            for cell, w in zip(row, col_widths):
                self.set_xy(self.get_x(), y0)
                self.multi_cell(w, row_h, '  ' + str(cell), fill=True)
                self.set_xy(self.get_x() + w, y0)
            # avancer après la ligne
            max_h = h_row
            self.set_xy(self.l_margin, y0 + max_h)
        self.ln(3)

    # ─── Encadré exercice ─────────────────────────────────────────────────
    def exercise_box(self, num, title, duration, content_fn):
        self.ln(4)
        # Bandeau titre exercice
        self.set_fill_color(*ODOO_DARK)
        self.set_text_color(*WHITE)
        self.set_font('Arial', 'B', 11)
        self.cell(0, 10,
                  f'   Exercice {num} -- {title}   ({duration})',
                  fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # Cadre contenu
        y_start = self.get_y()
        x_start = self.get_x()
        self.set_draw_color(*ODOO_DARK)
        self.set_line_width(0.3)
        # Appel du contenu
        content_fn()
        y_end = self.get_y()
        self.rect(x_start, y_start, 174, y_end - y_start)
        self.ln(3)


# ═══════════════════════════════════════════════════════════════════════════════
# CONTENU
# ═══════════════════════════════════════════════════════════════════════════════

def build_pdf():
    pdf = OdooFormationPDF()
    pdf.set_lang('fr')

    # ── Page de garde ──────────────────────────────────────────────────────────
    pdf.cover_page()

    # ── Planning ───────────────────────────────────────────────────────────────
    pdf.planning_page()

    # ══════════════════════════════════════════════════════════════════════════
    # INTRO : Interface RH
    # ══════════════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title('Présentation de l\'interface RH')

    pdf.sub_title('Accéder au module Employés')
    pdf.steps([
        'Cliquer sur l\'icône grille d\'applications (en haut à gauche d\'Odoo)',
        'Sélectionner l\'application Employés dans la liste des modules',
        'Le module s\'ouvre sur la vue Kanban (cartes employés)',
    ])
    pdf.ln(2)

    pdf.sub_title('Les vues disponibles')
    pdf.table(
        ['Icône', 'Vue', 'Utilisation'],
        [
            ['=', 'Liste', 'Voir plusieurs enregistrements sous forme de tableau'],
            ['#', 'Kanban', 'Vue par cartes (vue par défaut pour les employés)'],
            ['G', 'Graphique', 'Analyse visuelle : histogramme, camembert, courbe'],
            ['C', 'Calendrier', 'Planification : absences, entretiens, échéances'],
        ],
        col_widths=[12, 25, 137],
    )

    pdf.sub_title('Le menu Configuration RH')
    pdf.para('Aller dans Employés > Configuration pour accéder aux paramètres :')
    items = [
        'Départements -- structure organisationnelle de l\'entreprise',
        'Postes -- catalogue des intitulés de fonctions',
        'Types de contrats -- CDI, CDD, Stage, Alternance, etc.',
        'Plans d\'activités -- modèles de suivi RH automatisés',
    ]
    for it in items:
        pdf.bullet(it)

    # ══════════════════════════════════════════════════════════════════════════
    # MODULE 1 -- DÉPARTEMENTS
    # ══════════════════════════════════════════════════════════════════════════
    pdf.module_title(1, 'Les Départements')

    pdf.para(
        'Un département regroupe des employés autour d\'une même fonction dans '
        'l\'entreprise (ex : Comptabilité, Informatique, Commercial). '
        'Odoo permet de créer une hiérarchie : un département peut contenir '
        'des sous-départements.'
    )

    pdf.sub_title('Exemple de structure hiérarchique')
    pdf.set_fill_color(240, 236, 252)
    pdf.set_draw_color(*LIGHT_GRAY)
    pdf.rect(pdf.get_x(), pdf.get_y(), 174, 38, 'FD')
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(*ODOO_DARK)
    lines = [
        'Entreprise SA',
        '+-- Direction Generale',
        '+-- Finance',
        '|   +-- Comptabilite',
        '|   +-- Controle de gestion',
        '+-- Informatique',
        '    +-- Developpement',
    ]
    for line in lines:
        pdf.set_x(pdf.l_margin + 4)
        pdf.cell(0, 5.5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(*DARK_TEXT)
    pdf.set_font('Arial', '', 10.5)
    pdf.ln(3)

    # 1.1 Créer un département
    pdf.section_title('1.1 Créer un département')
    pdf.nav_path('Employés > Configuration > Départements > Nouveau')
    pdf.table(
        ['Champ', 'Description', 'Obligatoire'],
        [
            ['Nom', 'Intitulé du département', 'Oui'],
            ['Responsable', 'L\'employé qui dirige ce département', 'Non'],
            ['Département parent', 'Pour créer une hiérarchie (sous-département)', 'Non'],
            ['Société', 'La société à laquelle appartient ce département', 'Oui (auto)'],
        ],
        col_widths=[38, 112, 24],
    )

    pdf.para('Étapes de création :')
    pdf.steps([
        'Aller dans Employés > Configuration > Départements',
        'Cliquer sur Nouveau',
        'Saisir le Nom du département',
        '(Optionnel) Sélectionner un Responsable parmi les employés existants',
        '(Optionnel) Choisir un Département parent si c\'est un sous-département',
        'Cliquer sur Enregistrer',
    ])
    pdf.note_box(
        'Le responsable d\'un département doit être un employé déjà créé dans Odoo. '
        'Si vous créez les départements avant les employés, laissez ce champ vide '
        'et revenez-y ensuite.',
        kind='warn',
    )

    # 1.2 Archiver
    pdf.section_title('1.2 Archiver un département')
    pdf.para(
        'Archiver permet de désactiver un département sans le supprimer. '
        'Les données historiques et les employés sont conservés.'
    )
    pdf.steps([
        'Ouvrir la fiche du département',
        'Cliquer sur le menu Action (* engrenage) > Archiver',
        'Confirmer dans la fenêtre de dialogue',
    ])
    pdf.note_box(
        'Pour retrouver un département archivé : activer le filtre Archivé '
        'dans la barre de recherche de la liste.',
    )

    # 1.3 Voir les employés d'un département
    pdf.section_title('1.3 Voir les employés d\'un département')
    pdf.para(
        'Depuis la fiche d\'un département, le bouton Employés (en haut à droite) '
        'indique le nombre d\'employés et ouvre directement leur liste filtrée.'
    )

    # EXERCICE 1
    def ex1_content():
        pdf.set_x(pdf.l_margin + 4)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(*DARK_TEXT)
        pdf.ln(2)
        pdf.para('Créer les 6 départements suivants pour la société Formation SA :')
        pdf.table(
            ['Département', 'Département parent', 'Responsable'],
            [
                ['Direction Générale', '(aucun)', 'Laisser vide'],
                ['Ressources Humaines', 'Direction Générale', 'Laisser vide'],
                ['Finance', 'Direction Générale', 'Laisser vide'],
                ['Comptabilité', 'Finance', 'Laisser vide'],
                ['Informatique', 'Direction Générale', 'Laisser vide'],
                ['Développement', 'Informatique', 'Laisser vide'],
            ],
            col_widths=[55, 65, 54],
        )
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(*TIP_BORDER)
        pdf.cell(0, 7, '  [OK] Vérification attendue :',
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(*DARK_TEXT)
        pdf.bullet('6 lignes dans la liste des départements')
        pdf.bullet('Le département Comptabilité affiche Finance comme parent')
        pdf.ln(2)

    pdf.exercise_box('1', 'Créer la structure de l\'entreprise', '20 minutes', ex1_content)

    # ══════════════════════════════════════════════════════════════════════════
    # MODULE 2 -- EMPLOYÉS
    # ══════════════════════════════════════════════════════════════════════════
    pdf.module_title(2, 'Les Employés')

    pdf.para(
        'La fiche employé centralise toutes les informations d\'un collaborateur : '
        'identité, poste, coordonnées professionnelles, informations privées, '
        'et historique des contrats. Elle est organisée en plusieurs onglets.'
    )

    pdf.section_title('2.1 Onglet "Informations sur le travail"')
    pdf.para('C\'est l\'onglet principal, affiché en premier à l\'ouverture de la fiche.')
    pdf.table(
        ['Champ', 'Description', 'Obligatoire'],
        [
            ['Nom', 'Nom complet de l\'employé', 'Oui'],
            ['Poste', 'Fonction officielle (ex : Développeur)', 'Non'],
            ['Titre du poste', 'Intitulé personnalisé sur les documents', 'Non'],
            ['Département', 'Département de rattachement', 'Non'],
            ['Responsable', 'Le manager direct (autre employé)', 'Non'],
            ['Coach', 'Référent pour l\'intégration', 'Non'],
            ['Email professionnel', 'Adresse email de l\'entreprise', 'Non'],
            ['Téléphone pro', 'Numéro au bureau', 'Non'],
        ],
        col_widths=[44, 106, 24],
    )

    pdf.section_title('2.2 Onglet "Informations privées"')
    pdf.note_box('Accès réservé aux gestionnaires RH -- ces données sont confidentielles.')
    pdf.table(
        ['Champ', 'Description'],
        [
            ['Date de naissance', 'Pour calculer l\'âge et les droits légaux'],
            ['Genre', 'Homme / Femme / Autre'],
            ['Situation familiale', 'Célibataire, Marié(e), Divorcé(e)…'],
            ['Nombre d\'enfants à charge', 'Impact sur le calcul de la paie'],
            ['Numéro d\'identification', 'Numéro de carte d\'identité'],
            ['Niveau d\'études', 'Primaire, Secondaire, Licence, Master, Doctorat'],
            ['Adresse privée', 'Domicile de l\'employé (carnet d\'adresses)'],
        ],
        col_widths=[60, 114],
    )

    pdf.section_title('2.3 Onglet "Paramètres RH"')
    pdf.table(
        ['Champ', 'Description'],
        [
            ['Type d\'employé', 'Employé / Étudiant / Freelance / Autre'],
            ['Utilisateur lié', 'Compte Odoo associé (connexion au portail)'],
            ['Fuseau horaire', 'Utile pour les équipes internationales'],
            ['Coût horaire', 'Utilisé dans les feuilles de temps'],
        ],
        col_widths=[50, 124],
    )

    pdf.section_title('2.4 Créer un employé -- Pas à pas')
    pdf.nav_path('Employés > Employés > Nouveau')
    pdf.steps([
        'Saisir le Nom de l\'employé (grand champ en haut)',
        'Ajouter sa Photo en cliquant sur le cadre image (haut à droite)',
        'Renseigner le Poste, le Département, et le Responsable',
        'Saisir l\'email professionnel et le téléphone',
        'Cliquer sur l\'onglet Informations privées',
        'Renseigner la date de naissance, l\'adresse privée, la situation familiale',
        'Cliquer sur l\'onglet Paramètres RH',
        'Associer un utilisateur Odoo si l\'employé doit se connecter',
        'Cliquer sur Enregistrer',
    ])

    pdf.section_title('2.5 Archiver un employé (départ)')
    pdf.para(
        'Quand un employé quitte l\'entreprise, il ne faut pas le supprimer '
        '(risque de perte de données historiques). Il faut l\'archiver.'
    )
    pdf.steps([
        'Ouvrir la fiche de l\'employé',
        'Cliquer sur le menu Action (*) > Archiver',
        'Odoo demande un motif de départ : Démission / Fin de contrat / Licenciement / Retraite / Autre',
        'Saisir la date de départ',
        'Confirmer',
    ])
    pdf.note_box(
        'L\'employé archivé disparaît de la liste principale mais reste '
        'accessible via le filtre Archivé. Toutes ses données sont préservées.',
    )

    # EXERCICE 2
    def ex2_content():
        pdf.ln(2)
        pdf.para('Créer les 6 employés suivants (utiliser les départements de l\'exercice 1) :')
        pdf.table(
            ['Nom', 'Poste', 'Département', 'Responsable'],
            [
                ['Sophie Laurent', 'Directrice Générale', 'Direction Générale', '(aucun)'],
                ['Marc Dupont', 'Responsable RH', 'Ressources Humaines', 'Sophie Laurent'],
                ['Julie Chen', 'Responsable Finance', 'Finance', 'Sophie Laurent'],
                ['Paul Morin', 'Comptable', 'Comptabilité', 'Julie Chen'],
                ['Léa Bernard', 'Chef de projet IT', 'Développement', 'Sophie Laurent'],
                ['Antoine Petit', 'Développeur', 'Développement', 'Léa Bernard'],
            ],
            col_widths=[38, 40, 50, 46],
            row_h=7,
        )
        pdf.para('Ensuite, affecter les responsables aux départements :')
        pdf.bullet('Ressources Humaines → Marc Dupont')
        pdf.bullet('Finance → Julie Chen')
        pdf.bullet('Développement → Léa Bernard')
        pdf.ln(1)
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(*TIP_BORDER)
        pdf.cell(0, 7, '  [OK] Vérification : fiche Antoine Petit → Responsable = Léa Bernard, Département = Développement',
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(*DARK_TEXT)
        pdf.ln(1)

    pdf.exercise_box('2', 'Créer les employés', '30 minutes', ex2_content)

    # ══════════════════════════════════════════════════════════════════════════
    # MODULE 3 -- CONTRATS
    # ══════════════════════════════════════════════════════════════════════════
    pdf.module_title(3, 'Les Contrats')

    pdf.para(
        'Le contrat de travail dans Odoo enregistre la relation contractuelle entre '
        'l\'entreprise et l\'employé : type de contrat, dates, salaire. '
        'Chaque employé peut avoir plusieurs contrats successifs, '
        'mais un seul contrat actif à la fois.'
    )

    pdf.section_title('3.1 Les statuts d\'un contrat')
    pdf.table(
        ['Statut', 'Signification'],
        [
            ['Nouveau', 'Contrat créé mais pas encore validé (brouillon)'],
            ['En cours', 'Contrat actif -- l\'employé travaille sous ce contrat'],
            ['Expiré', 'La date de fin est passée (CDD terminé automatiquement)'],
            ['Annulé', 'Contrat annulé avant son démarrage'],
        ],
        col_widths=[35, 139],
    )

    # Schéma workflow
    pdf.set_fill_color(240, 236, 252)
    pdf.set_draw_color(*LIGHT_GRAY)
    y0 = pdf.get_y()
    pdf.rect(pdf.l_margin, y0, 174, 22, 'FD')
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*ODOO_PURPLE)
    pdf.set_xy(pdf.l_margin + 4, y0 + 4)
    pdf.cell(0, 6, 'Cycle de vie d\'un contrat :')
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*ODOO_DARK)
    pdf.set_xy(pdf.l_margin + 8, y0 + 11)
    pdf.cell(0, 6, 'Nouveau  -->  En cours  -->  Expire')
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(*GRAY_TEXT)
    pdf.set_xy(pdf.l_margin + 8 + 73, y0 + 15)
    pdf.cell(0, 5, '+-->  Annule')
    pdf.set_text_color(*DARK_TEXT)
    pdf.set_font('Arial', '', 10.5)
    pdf.ln(26)

    pdf.section_title('3.2 Créer un contrat')
    pdf.nav_path('Fiche employé > bouton Contrats > Nouveau')
    pdf.table(
        ['Champ', 'Description', 'Obligatoire'],
        [
            ['Référence', 'Nom du contrat (ex : CDI - Marc Dupont 2024)', 'Oui'],
            ['Employé', 'Sélectionné automatiquement depuis la fiche', 'Oui'],
            ['Type de contrat', 'CDI, CDD, Alternance, Stage…', 'Oui'],
            ['Date de début', 'Date de prise de poste', 'Oui'],
            ['Date de fin', 'Obligatoire pour un CDD -- vide pour un CDI', 'Non'],
            ['Salaire brut mensuel', 'Rémunération mensuelle en euros', 'Oui'],
            ['Responsable RH', 'La personne RH en charge du suivi', 'Non'],
            ['Notes', 'Avantages, primes, clauses particulières…', 'Non'],
        ],
        col_widths=[44, 106, 24],
    )
    pdf.note_box(
        'CDI (Durée Indéterminée) : laisser la date de fin vide.\n'
        'CDD (Durée Déterminée) : la date de fin est obligatoire.',
        kind='warn',
    )

    pdf.section_title('3.3 Créer et confirmer un contrat -- Pas à pas')
    pdf.steps([
        'Ouvrir la fiche de l\'employé concerné',
        'Cliquer sur le bouton Contrats (en haut à droite de la fiche)',
        'Cliquer sur Nouveau',
        'Vérifier que le champ Employé est correct',
        'Saisir la Référence du contrat (ex : CDI - Antoine Petit - 2025)',
        'Choisir le Type de contrat (CDI, CDD…)',
        'Saisir la Date de début',
        'Pour un CDD : saisir la Date de fin',
        'Saisir le Salaire brut mensuel',
        'Cliquer sur Enregistrer',
        'Cliquer sur Confirmer → le statut passe à En cours',
    ])

    pdf.note_box(
        'Une fois confirmé, le salaire et les dates ne sont plus modifiables directement. '
        'Pour corriger, cliquer sur Remettre en brouillon, modifier, puis reconfirmer.',
        kind='warn',
    )

    pdf.section_title('3.4 Gérer un CDD qui se termine')
    pdf.para(
        'Quand la date de fin d\'un CDD est atteinte, Odoo passe automatiquement '
        'le contrat en statut Expiré. Trois options s\'offrent alors :'
    )
    pdf.bullet('Renouveler le CDD : créer un nouveau contrat avec une nouvelle date de début')
    pdf.bullet('Transformer en CDI : créer un nouveau contrat CDI sans date de fin')
    pdf.bullet('Ne pas renouveler : archiver l\'employé')
    pdf.ln(2)

    # EXERCICE 3
    def ex3_content():
        pdf.ln(2)
        pdf.para('Créer un contrat pour chaque employé de l\'exercice 2, puis le confirmer :')
        pdf.table(
            ['Employé', 'Type', 'Date début', 'Date fin', 'Salaire brut'],
            [
                ['Sophie Laurent', 'CDI', '01/01/2022', '--', '6 000 €'],
                ['Marc Dupont', 'CDI', '01/03/2022', '--', '3 800 €'],
                ['Julie Chen', 'CDI', '01/06/2022', '--', '4 200 €'],
                ['Paul Morin', 'CDD', '01/01/2024', '31/12/2024', '2 800 €'],
                ['Léa Bernard', 'CDI', '15/09/2023', '--', '4 500 €'],
                ['Antoine Petit', 'CDD', '01/03/2024', '28/02/2025', '3 200 €'],
            ],
            col_widths=[42, 16, 28, 28, 30],
            row_h=7,
        )
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(*TIP_BORDER)
        pdf.para('[OK] Vérification : Paul Morin et Antoine Petit ont des contrats Expirés. Les 4 autres sont En cours.')
        pdf.set_text_color(*DARK_TEXT)
        pdf.ln(1)

    pdf.exercise_box('3', 'Créer les contrats', '30 minutes', ex3_content)

    # ══════════════════════════════════════════════════════════════════════════
    # MODULE 4 -- RECHERCHE ET RAPPORTS
    # ══════════════════════════════════════════════════════════════════════════
    pdf.module_title(4, 'Recherche, Analyse et Rapports')

    pdf.section_title('4.1 Filtres avancés')
    pdf.para('La barre de recherche offre des filtres rapides prédéfinis :')
    pdf.table(
        ['Filtre', 'Résultat'],
        [
            ['Mon équipe', 'Uniquement vos subordonnés directs'],
            ['Archivé', 'Employés ou contrats désactivés'],
            ['En cours', 'Contrats actifs uniquement'],
            ['Date de fin définie', 'Isoler les CDD (date de fin renseignée)'],
        ],
        col_widths=[55, 119],
    )
    pdf.para('Exemple -- Tous les CDD actifs :')
    pdf.steps([
        'Aller dans la liste des contrats',
        'Cliquer sur la barre de recherche > Filtres > En cours',
        'Ajouter > Date de fin est définie',
    ])

    pdf.section_title('4.2 Regroupements')
    pdf.para('Regrouper les employés par département puis par responsable :')
    pdf.steps([
        'Liste des employés > Barre de recherche',
        'Regrouper par > Département',
        'Regrouper par > Responsable',
    ])
    pdf.note_box('On peut combiner plusieurs niveaux de regroupement pour créer des vues croisées.')

    pdf.section_title('4.3 Vue graphique -- Analyse des effectifs')
    pdf.steps([
        'Aller dans Employés > Employés',
        'Cliquer sur l\'icône Graphique (en haut à droite)',
        'Choisir le type : Barres / Camembert / Courbe',
        'Sélectionner la mesure : Nombre d\'employés',
        'Regrouper par : Département ou Poste',
    ])

    pdf.section_title('4.4 Exporter les données')
    pdf.steps([
        'Aller dans la liste souhaitée (employés, contrats…)',
        'Cocher les enregistrements à exporter (ou tout sélectionner avec la case en-tête)',
        'Cliquer sur Action > Exporter',
        'Choisir les colonnes à inclure',
        'Choisir le format : Excel (.xlsx) ou CSV',
        'Cliquer sur Exporter',
    ])

    # EXERCICE 4
    def ex4_content():
        pdf.ln(2)
        actions = [
            ('1', 'Lister tous les employés du département Développement',
             'Barre de recherche > filtrer par Département = Développement'),
            ('2', 'Effectifs par département en camembert',
             'Vue Graphique > Regrouper par Département > Type Camembert'),
            ('3', 'Identifier les contrats expirés',
             'Liste des contrats > Filtre > Expiré → vous devez voir Paul Morin et Antoine Petit'),
            ('4', 'Exporter la liste des employés en Excel',
             'Colonnes : Nom, Département, Poste, Email, Date de début de contrat'),
        ]
        for num, obj, method in actions:
            pdf.set_font('Arial', 'B', 10)
            pdf.set_text_color(*ACCENT_BLUE)
            pdf.set_x(pdf.l_margin + 4)
            pdf.cell(0, 7, f'{num}. {obj}', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_font('Arial', 'I', 9.5)
            pdf.set_text_color(*GRAY_TEXT)
            pdf.set_x(pdf.l_margin + 10)
            pdf.multi_cell(0, 6, method)
            pdf.ln(1)
        pdf.set_text_color(*DARK_TEXT)

    pdf.exercise_box('4', 'Analyse et recherche', '20 minutes', ex4_content)

    # ══════════════════════════════════════════════════════════════════════════
    # EXERCICE DE SYNTHÈSE
    # ══════════════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.set_fill_color(*ODOO_PURPLE)
    pdf.rect(0, 10, 210, 18, 'F')
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(*WHITE)
    pdf.set_y(14)
    pdf.cell(0, 10, '  Exercice de synthèse -- 30 minutes',
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(*DARK_TEXT)
    pdf.ln(8)

    pdf.sub_title('Contexte')
    pdf.set_fill_color(235, 245, 255)
    pdf.set_draw_color(*ACCENT_BLUE)
    pdf.set_line_width(0.4)
    pdf.rect(pdf.l_margin, pdf.get_y(), 174, 30, 'FD')
    pdf.set_xy(pdf.l_margin + 4, pdf.get_y() + 3)
    pdf.set_font('Arial', 'B', 10.5)
    pdf.set_text_color(*ACCENT_BLUE)
    pdf.cell(0, 6, 'Nouvelle embauche chez Formation SA',
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(pdf.l_margin + 4)
    pdf.set_font('Arial', '', 10.5)
    pdf.set_text_color(*DARK_TEXT)
    pdf.multi_cell(166, 6.5,
        'Camille Renard rejoint l\'équipe le 1er avril 2025 en tant que '
        'Développeuse Full Stack dans le département Développement. '
        'Son responsable est Léa Bernard. Elle est embauchée en CDD de 6 mois '
        '(jusqu\'au 30 septembre 2025) à 3 400 € brut/mois. '
        'En cas de succès, le CDD sera renouvelé en CDI à 3 600 €/mois.')
    pdf.ln(6)

    pdf.sub_title('Travail à effectuer')
    tasks = [
        'Vérifier que le poste "Développeuse Full Stack" existe -- sinon le créer dans Configuration > Postes',
        'Créer la fiche employé de Camille Renard avec tous les champs obligatoires',
        'Email : c.renard@formationsa.fr | Téléphone : 01 23 45 67 89',
        'Créer son contrat CDD (01/04/2025 → 30/09/2025, salaire 3 400 €) et le confirmer',
        'Vérifier que Camille apparaît dans la liste du département Développement',
        'Simuler le renouvellement : créer un second contrat CDI au 01/10/2025 (salaire 3 600 €) et le confirmer',
    ]
    pdf.steps(tasks)
    pdf.ln(2)
    pdf.note_box('Résultat attendu : la fiche de Camille Renard affiche 2 contrats.', kind='info')

    # ══════════════════════════════════════════════════════════════════════════
    # BONNES PRATIQUES & FAQ
    # ══════════════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title('Bonnes pratiques RH dans Odoo')

    pdf.sub_title('À faire')
    dos = [
        'Créer les départements avant les employés',
        'Renseigner le responsable de chaque employé (active la hiérarchie et les workflows)',
        'Utiliser des types de contrats standardisés pour des rapports cohérents',
        'Archiver les employés qui partent plutôt que de les supprimer',
        'Vérifier régulièrement les contrats proches de l\'expiration',
        'Nommer les contrats de manière cohérente : "TYPE - Prénom Nom - Année"',
    ]
    for d in dos:
        pdf.bullet(d)
    pdf.ln(2)

    pdf.sub_title('À éviter')
    donts = [
        'Supprimer un employé qui a des données liées (pointages, notes de frais, contrats)',
        'Laisser un contrat en statut "Nouveau" une fois l\'employé en poste',
        'Créer plusieurs postes avec des noms légèrement différents (définir une nomenclature)',
        'Créer plusieurs comptes Odoo pour le même employé',
        'Modifier le salaire d\'un contrat confirmé sans le remettre en brouillon',
    ]
    for d in donts:
        pdf.bullet(d)
    pdf.ln(3)

    pdf.section_title('Questions fréquentes')
    faqs = [
        (
            'Peut-on supprimer un employé ?',
            'Oui, uniquement s\'il n\'a aucune donnée liée. Dans la pratique, '
            'il vaut toujours mieux archiver pour conserver l\'historique.',
        ),
        (
            'Un employé peut-il avoir plusieurs contrats actifs simultanément ?',
            'Non. Odoo affiche une alerte si vous confirmez un second contrat '
            'pendant qu\'un autre est déjà actif sur la même période.',
        ),
        (
            'Comment modifier le salaire d\'un contrat en cours ?',
            'Remettre le contrat en brouillon (bouton "Remettre en brouillon"), '
            'modifier le salaire, puis reconfirmer. Attention à l\'impact sur '
            'les calculs de paie déjà effectués.',
        ),
        (
            'Quelle différence entre "Poste" et "Titre du poste" ?',
            '"Poste" est la référence au catalogue des fonctions (ex : Développeur). '
            '"Titre du poste" est un intitulé libre qui apparaît sur les documents '
            '(ex : Développeur Python Senior).',
        ),
        (
            'Comment associer un utilisateur Odoo à un employé ?',
            'Fiche employé > onglet Paramètres RH > champ Utilisateur lié. '
            'Cela permet à l\'employé de se connecter et d\'accéder à ses congés, '
            'notes de frais, etc.',
        ),
    ]
    for q, a in faqs:
        pdf.set_fill_color(240, 236, 252)
        pdf.set_font('Arial', 'B', 10.5)
        pdf.set_text_color(*ODOO_PURPLE)
        pdf.set_x(pdf.l_margin + 2)
        pdf.cell(6, 7, 'Q')
        pdf.set_text_color(*ODOO_DARK)
        pdf.multi_cell(0, 7, q)
        pdf.set_font('Arial', '', 10.5)
        pdf.set_text_color(*DARK_TEXT)
        pdf.set_x(pdf.l_margin + 8)
        pdf.multi_cell(0, 6.5, a)
        pdf.ln(2)

    # ══════════════════════════════════════════════════════════════════════════
    # RÉCAPITULATIF DES CHEMINS
    # ══════════════════════════════════════════════════════════════════════════
    pdf.section_title('Récapitulatif des chemins de navigation')
    pdf.table(
        ['Action', 'Chemin dans Odoo 18'],
        [
            ['Créer un département', 'Employés > Configuration > Départements > Nouveau'],
            ['Créer un poste', 'Employés > Configuration > Postes > Nouveau'],
            ['Créer un employé', 'Employés > Employés > Nouveau'],
            ['Voir les contrats d\'un employé', 'Fiche employé > bouton Contrats'],
            ['Créer un contrat', 'Fiche employé > Contrats > Nouveau'],
            ['Archiver un employé', 'Fiche employé > Action > Archiver'],
            ['Voir les employés archivés', 'Employés > Filtre : Archivé'],
            ['Configurer les types de contrats', 'Employés > Configuration > Types de contrats'],
            ['Exporter des données', 'Liste > Sélectionner > Action > Exporter'],
        ],
        col_widths=[65, 109],
    )

    return pdf


# ── Génération ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    pdf = build_pdf()
    out = r'D:\DEV\Formations\Formation_Odoo18_RH_Employes_Departements_Contrats.pdf'
    pdf.output(out)
    print(f'PDF généré : {out}')
