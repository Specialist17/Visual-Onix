# Yacc example

import ply.yacc as yacc

import sys

# Get the token map from the lexer.  This is required.
from VisualOnixLex import tokens

f = open('VisualOnixTest.html','w')
#=======================================================================
#                           Grammar Rules
#=======================================================================

#BNF

def p_expression_createhtml(p):
            'expression :  CREATEHTML'

            f.write("<HTML> \n <style>body{background-image: url(\"cuadriculado.jpg\");} td,table,tr{width:100%; height:150px;}</style> <BODY><center><table><tr><td style=\"background-image:url(banner.jpg)\"><h1>Welcome to Visual Onix</h1></td></tr></table></center><svg width=\"100000\" height=\"100000\">")
            print ("WHOO")


def p_expression_circle(p):

        'expression : CIRCLE term NUMBER NUMBER NUMBER term term'

        f.write("<circle id=\""+ str(p[2]) +"\" cx=\"" + str(p[3]) + "\" cy=\"" + str(p[4]) + "\" r=\"" + str(p[5]) + "\" stroke=\"" + str(p[6]) + "\" stroke-width=\"4\" fill=\"" + str(p[7]) + "\" />")


def p_expression_rectangle(p):

        'expression : RECT NUMBER NUMBER NUMBER NUMBER term term'

        f.write("<rect x=\"" + str(p[2]) + "\" y=\"" + str(p[3]) + "\" width=\"" + str(p[4]) + "\" height=\"" + str(p[5]) + "\" stroke=\"" + str(p[6]) + "\" stroke-width=\"4\" fill=\"" + str(p[7]) + "\" />")

def p_expression_ellipse(p):

        'expression : ELLIPSE NUMBER NUMBER NUMBER NUMBER term term'

        f.write("<ellipse cx=\"" + str(p[2]) + "\" cy=\"" + str(p[3]) + "\" rx=\"" + str(p[4]) + "\" ry=\"" + str(p[5]) + "\" stroke=\"" + str(p[6]) + "\" stroke-width=\"4\" fill=\"" + str(p[7]) + "\" />")

def p_expression_line(p):

        'expression : LINE NUMBER NUMBER NUMBER NUMBER term term'

        f.write("<line x1=\"" + str(p[2]) + "\" y1=\"" + str(p[3]) + "\" x2=\"" + str(p[4]) + "\" y2=\"" + str(p[5]) + "\" stroke=\"" + str(p[6]) + "\" stroke-width=\"4\" fill=\"" + str(p[7]) + "\" />")

def p_expression_polygon(p):

        '''expression : POLYGON NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER term term
                        | POLYGON NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER term term
                        | POLYGON NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER term term
                        | POLYGON NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER term term
                        | POLYGON NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER term term
                        | POLYGON NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER NUMBER COMA NUMBER  term term'''
        if len(p) == 13:
            f.write("<polygon points=\"" + str(p[2]) + str(p[3]) + str(p[4])+ " " + str(p[5]) + str(p[6]) + str(p[7]) + " " + str(p[8]) + str(p[9]) + str(p[10]) + "\" stroke=\"" + str(p[11]) + "\" stroke-width=\"4\" fill=\"" + str(p[12]) + "\" />")
        elif len(p) == 16:
            f.write("<polygon points=\"" + str(p[2]) + str(p[3]) + str(p[4])+ " " + str(p[5]) + str(p[6]) + str(p[7]) + " " + str(p[8]) + str(p[9]) + str(p[10]) + " " + str(p[11]) + str(p[12]) + str(p[13]) + "\" stroke=\"" + str(p[14]) + "\" stroke-width=\"4\" fill=\"" + str(p[15]) + "\" />")
        elif len(p) == 19:
            f.write("<polygon points=\"" + str(p[2]) + str(p[3]) + str(p[4])+ " " + str(p[5]) + str(p[6]) + str(p[7]) + " " + str(p[8]) + str(p[9]) + str(p[10]) + " " + str(p[11]) + str(p[12]) + str(p[13]) + " " + str(p[14]) + str(p[15]) + str(p[16]) + "\" stroke=\"" + str(p[17]) + "\" stroke-width=\"4\" fill=\"" + str(p[18]) + "\" />")
        elif len(p) == 22:
            f.write("<polygon points=\"" + str(p[2]) + str(p[3]) + str(p[4])+ " " + str(p[5]) + str(p[6]) + str(p[7]) + " " + str(p[8]) + str(p[9]) + str(p[10]) + " " + str(p[11]) + str(p[12]) + str(p[13]) + " " + str(p[14]) + str(p[15]) + str(p[16]) + " " + str(p[17]) + str(p[18]) + str(p[19]) + "\" stroke=\"" + str(p[20]) + "\" stroke-width=\"4\" fill=\"" + str(p[21]) + "\" />")
        elif len(p) == 25:
            f.write("<polygon points=\"" + str(p[2]) + str(p[3]) + str(p[4])+ " " + str(p[5]) + str(p[6]) + str(p[7]) + " " + str(p[8]) + str(p[9]) + str(p[10]) + " " + str(p[11]) + str(p[12]) + str(p[13]) + " " + str(p[14]) + str(p[15]) + str(p[16]) + " " + str(p[17]) + str(p[18]) + str(p[19]) + " " + str(p[20]) + str(p[21]) + str(p[22]) + "\" stroke=\"" + str(p[23]) + "\" stroke-width=\"4\" fill=\"" + str(p[24]) + "\" />")
        else:
            f.write("<polygon points=\"" + str(p[2]) + str(p[3]) + str(p[4])+ " " + str(p[5]) + str(p[6]) + str(p[7]) + " " + str(p[8]) + str(p[9]) + str(p[10]) + " " + str(p[11]) + str(p[12]) + str(p[13]) + " " + str(p[14]) + str(p[15]) + str(p[16]) + " " + str(p[17]) + str(p[18]) + str(p[19]) + " " + str(p[20]) + str(p[21]) + str(p[22]) + " " + str(p[23]) + str(p[24]) + str(p[25]) + "\" stroke=\"" + str(p[26]) + "\" stroke-width=\"4\" fill=\"" + str(p[27]) + "\" />")

def p_expression_text(p):

        'expression : TEXT NUMBER NUMBER term STRINGVALUE'

        f.write("<text x=\"" + str(p[2]) + "\" y=\"" + str(p[3]) + "\" fill=\"" + str(p[4]) + "\" " + str(p[5]) + "/text>")

def p_expression_end(p):
            'expression : END'
            f.write("</svg></BODY></HTML>")
            f.close()
            sys.exit()

def p_animate_draw(p):
    'expression : ANIMATE term DRAW'

    f.write("<style type=\"text/css\"> #"+ str(p[2]) +"{background-color: #fff;stroke-width: 4;stroke-dasharray: 4000;stroke-dashoffset: 4000 ;animation: offset 2s linear forwards, fill 2s 2s forwards;}@keyframes offset{0%{fill-opacity: 0;}100%{stroke-dashoffset: 0;fill-opacity: 0;} }@keyframes fill{0%{fill: #231F20;fill-opacity: 0;} }</style>")

def p_animate_moveright(p):
    'expression : ANIMATE term MOVERIGHT'

    f.write("<style type=\"text/css\"> #"+ str(p[2]) +"{background-color: #fff;stroke-width: 4;cx: 200; ;animation: offset 2s linear forwards, fill 2s 2s forwards;}@keyframes offset{0%{cx: 300;}100%{cx: 800;fill-opacity: 0;} }@keyframes fill{0%{fill: #231F20;fill-opacity: 0;} }</style>")




# ------------------------------------------------------------
# Expression rules that convert the input of other rules.
# ------------------------------------------------------------
def p_term_ID(p):
            'term : ID'
        #    p[0] = variable_check(p[1])
            p[0] = p[1]
            print ("p_expression_ID")

        #    print (variable_check(p[1]))

def p_expression_term(p):
            'expression : term'
            p[0] = p[1]
            print ("p_expression_term")


#=======================================================================
#                           Implementation
#=======================================================================

parser = yacc.yacc()

while True:
   try:
       s = input('Visual Onix ->')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

