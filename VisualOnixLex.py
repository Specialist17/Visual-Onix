
import ply.lex as lex

reserved = {'draw':'DRAW', 'stroke':'STROKE','strokewidth':'STROKEWIDTH',
            'circle': 'CIRCLE', 'rect': 'RECT',
            'polygon':'POLYGON','id':'ID',
            'line': 'LINE','svg' : 'SVG',
            'fill' : 'FILL', 'ellipse' : 'ELLIPSE', 'createhtml':'CREATEHTML' ,'text':'TEXT', 'id':'ID',
            'polyline':'POLYLINE','end':'END'}

# ------------------------------------------------------------
# List of token names. This are for general purpose use.
# ------------------------------------------------------------
tokens = [
   'POINTX',
   'POINTY',
   'RADIUSX',
   'RADIUSY',
   'RADIUS',
   'WIDTH',
   'HEIGHT',
   'CORNERRADIUSY',
   'CORNERRADIUSX',
   'BACKGROUND_COLOR',
   'EQUAL',
   'LPAREN',
   'RPAREN',
   'LBR',
   'RBR',
   'CONSTANTVALUE',
   'NUMBER',
   'SEMICOLON',
   'COLON',
   'STRINGVALUE'
]  + list(reserved.values())

# ------------------------------------------------------------
# Regular expression rules for simple parenthesis tokens.
# ------------------------------------------------------------

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL = r'\='
t_LBR = r'\{'
t_RBR = r'\}'
t_SEMICOLON = r'\;'
t_COLON = r'\,'
t_CONSTANTVALUE = r'[A-Z]{2,}'
t_STRINGVALUE = r'(\>(\\.|[^"])*\<)'
##t_NUMERICVALUE = r'^(\+|\-)?(?=\D*\d)([0-9])*\.([0-9])*$'


# ------------------------------------------------------------
# All remaining regular expressions
# ------------------------------------------------------------
def t_SVG(t):
    r'svg'
    t.value = 'svg'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_DRAW(t):
    r'draw'
    t.type = 'draw'
    return t

def t_CREATEHTML(t):
    r'CREATEHTML'
    t.type = 'CREATEHTML'
    return t

def t_STROKE(t):
    r'stroke'
    t.type = 'stroke'
    return t

def t_CIRCLE(t):
    r'circle'
    t.type = 'circle'
    return t

def t_RECT(t):
    r'rect'
    t.type = 'rect'
    return t

def t_ELLIPSE(t):
    r'ellipse'
    t.type = 'ellipse'
    return t

def t_POLYGON(t):
    r'polygon'
    t.type = 'polygon'
    return t

def t_POLYLINE(t):
    r'polyline'
    t.type = 'polyline'
    return t

def t_LINE(t):
    r'line'
    t.type = 'line'
    return t

def t_TEXT(t):
    r'text'
    t.type = 'text'
    return t

def t_FILL(t):
    r'fill'
    t.type = 'fill'
    return t

def t_POINTX(t):
    r'pointx'
    t.value = 'pointx'
    return t

def t_POINTY(t):
    r'pointy'
    t.type = 'pointy'
    return t

def t_RADIUSX(t):
    r'radiusx'
    t.type = 'radiusx'
    return t

def t_RADIUSY(t):
    r'radiusy'
    t.type = 'radiusy'
    return t

def t_RADIUS(t):
    r'radius'
    t.type = 'radius'
    return t

def t_WIDTH(t):
    r'width'
    t.type = 'width'
    return t

def t_HEIGHT(t):
    r'height'
    t.type = 'height'
    return t

def t_CORNERRADIUSX(t):
    r'cornerradiusx'
    t.type = 'cornerradiusx'
    return t

def t_CORNERRADIUSY(t):
    r'cornerradiusy'
    t.type = 'cornerradiusy'
    return t

def t_STROKEWIDTH(t):
    r'strokewidth'
    t.type = 'strokewidth'
    return t

def t_BACKGROUND_COLOR(t):
    r'BACKGROUND_COLOR'
    t.value = 'BACKGROUND_COLOR'
    return t


# ------------------------------------------------------------
# Regular expression rule for tracking line numbers.
# ------------------------------------------------------------
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ------------------------------------------------------------
# A string containing ignored characters (spaces and tabs)
# ------------------------------------------------------------
t_ignore  = ' \t'

# ------------------------------------------------------------
# Code to lower case all reserved words.
# ------------------------------------------------------------
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

# ------------------------------------------------------------
# Regular expression rule for error handling.
# ------------------------------------------------------------
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# ------------------------------------------------------------
# Build the lexer
# ------------------------------------------------------------
lexer = lex.lex()
