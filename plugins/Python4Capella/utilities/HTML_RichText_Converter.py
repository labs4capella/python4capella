'''
Created on Aug 8, 2022

@author: slacrampe
'''
##########################################################
#The goal of this library is to convert HTML coming from the Capella description fields
#into text within Excel cells, while keeping as much as possible the original look
#It works with the XslxWriter library only
#
# The main entry point is HTML_RichText_Converter.WriteCell method
#
# KNOWN LIMITATIONS :Excel is not able to render HTML within a cell and we are limited by Excel with how we can change the font/color/etc... inside a single cell: 
# - URLs <A Href="https://www...."> and FILE links, as well as Images and link to model or diagram elements are not clickable (Excel limitation) but links are displayed blue and underligned+blod
# - The following Capella description window Styles are not managed: Special Container, Marker
# - The following HTML Styles attributes are not managed: background-color, background, border, padding, border-image, overflow, top, height, position, text-align, margin
# - The following HTML attributes are not managed: class, title, dir, height, width, xmlns, id, lang, unselectable, contenteditable, align, rel, target, alt, src, border, frameborder, allowfullscreen, longdesc
# - The following HTML attributes are not managed: div, svg, font, iframe, table, tbody
# Note: there may be other limitations.The Capella descriptions fields have a limited set of formatting options (Eclipse Nebula widget) but the end users may also do a copy-paste from a web browser, thus the actual HTML may be quite different from what is expected 
##########################################################
from io import StringIO
from html.parser import HTMLParser
import math

##########################################################
# Main entry point. Parameters:
# - HTML is the HTML string to be converted
# - cell_position is the cell position (string) in the Excel sheet (ex: "C2")  
# - workbook is the XslxWriter Workbook
# - worksheet is the XslxWriter Worksheet
# - cell_format is the XslxWriter Cell Format
##########################################################
class HTML_RichText_Converter():
    @staticmethod
    def write_cell(HTML, cell_position, workbook, worksheet, cell_format):
        segment =  HTML_RichText_Converter.convert(HTML, workbook)
        error = 0
        if segment != [] :
            # The write_rich_string method requires that the list (*segment) has at least 3 items (the first one is the default Format we add)
            if len(segment)>2:
                error = worksheet.write_rich_string(cell_position, *segment, cell_format)
            else:
                #We use the default write method, fetching position 1 in the segment (position 0 is the default format)
                error = worksheet.write(cell_position, segment[1], cell_format)
        if error == -1:
            print("ERROR While writing in a Cell: Row or column is out of worksheet bounds: " + cell_position) 
        if error == -2:
            print("ERROR While writing in a Cell: string is longer then 32 characters:")
        if error == -3:
            print("ERROR While writing in a Cell: 2 consecutive formats used.")
        if error == -4:
            print("ERROR While writing in a Cell: Empty String used") 
        if error == -5:
            print("ERROR While writing in a Cell: Insufficient parameters: ") 
        if error < 0:
            print(segment) 

##########################################################
# Calling the HTMLParser on the HTML String
# Returns a list of Format and Strings
##########################################################

    @staticmethod
    def convert(HTML, workbook):
        if HTML == None:
            return []
        parser = HTMLParserForXlsxWriter(workbook)
#        print(HTML)
        result = parser.feed(HTML)
#        print(result)
        return result

class HTMLParserForXlsxWriter(HTMLParser):
##########################################################
# Parser Initialization
##########################################################
    def __init__(self, workbook):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
        # Storing the current workbook (used to add Format)
        self.workbook = workbook
        #Style used to emulate HREF links
        self.hrefstyle = workbook.add_format({'font_color': 'blue','bold': 1,'underline':  1,'font_size':  12})
        #used to distinguish <UL> from <OL> when in <LI> (bullet list or numbered list)
        self.ulMode = False
        self.olMode = False
        self.liMode = False
        self.firstLi = True
        self.indentLevel=0
        self.ol_id = {}
        #Used for tables
        self.tableMode = False
        #used for indents
        self.indentStringSize = 7 #will create 7 spaces to imitate indents
        #Initialization of the default Font
        self.defaultFont = 'Arial'
        self.defaultFontSize = 11
        self.new_line = '\n'

##########################################################
#Main parser method            
##########################################################
    def feed(self, in_html):
        self.output = []
        self.__init_default_font()
        #Replacing <br/> tags by new lines as it reduces code complexity for the parser
        #Also removes \t that tends to mix things up with Excel. Finally, strip both ends
        content = in_html.replace("<br />", self.new_line).replace("\n\n",self.new_line).replace("\t",'').strip()        
        super(HTMLParserForXlsxWriter, self).feed(content)
        return self.output
    
##########################################################
# Handle information contained between tags
##########################################################
    def handle_data(self, data):
        #If we are rendering <li> or <table> tags then we ignore all \n \r and strip
        if (self.ulMode or self.olMode or self.tableMode):
            #Removing \t is needed again as it seems that the previous remove \t is not removing them all...
            data = data.replace('\r','').replace('\n', '').replace('\t','').strip()
        # We never append empty Strings as the write_rich_string prevents it
        if data != '':       
            #Appending the current calculated Font Style
            self.output.append(self.currentFont)
            self.output.append(data)

        #Reseting Font Style for next data and associated tags 
        self.__init_default_font()

##########################################################
# Most important method, managing HTML Tags
##########################################################
    def handle_starttag(self, tag, attrs):
#        print("processing Tag: " + tag + ' with Attr: '+ str(attrs))
        #####################################################################################################################
        # HTML TAG'S ATTRIBUTES MANAGEMENT  #
        #####################################################################################################################
        for attr in attrs:
            # Attribute style="......"
            if attr[0] == 'style' :
                #splitting the different styles attributes
                styleContentList = attr[1].split(";")
                #Removing the last split as it is generally empty
                styleContentList.pop(len(styleContentList)-1)
                for styleCt in styleContentList:
                    styleContent = styleCt.strip()
                    if styleContent.startswith("margin-left:") :
                        #We get the margin value
                        indent = int(styleContent[styleContent.index('margin-left:')+12:len(styleContent[1])-3])
                        #We divide it by 40 to increment using a scale of X spaces (X= indent value)
                        indent = int (indent/40) 
                        #We avoid it when inside LI/UL/OL tags as it is managed elsewhere
                        if tag != 'li' and tag!='ul' and tag!= 'ol':
                            self.output.append(' ' * (self.indentStringSize * indent))
                    elif styleContent.startswith("color:"):
                        color = self.__extractColor(styleContent)
                        self.currentFont.set_font_color(color)
                    elif styleContent.startswith("background-color:") or styleContent.startswith("background:"):
                        #TODO Make this an option, either we pass, either we color
                        #color = self.__extractColor(styleContent)                
                        #self.currentFont.set_font_color(color)
                        pass
                    elif styleContent.startswith("font-size:"):
                        #TODO Manage other sizes than px
                        if styleContent.find('px') != -1:
                            self.currentFont.set_font_size(math.trunc(float(styleContent[10:len(styleContent)-2])))
                    elif styleContent == "font-style: italic":
                        self.currentFont.set_italic()
                    elif styleContent.startswith("font-family:"):
                        font = styleContent[styleContent.index('font-family:')+12:len(styleContent)]
                        font = font.split(",")[0].strip()
                        self.currentFont.set_font_name(font.split(",")[0])
                    #These are tags that we know we do nothing about them
                    elif styleContent.startswith("padding:") or styleContent.startswith("border:") or styleContent.startswith("border-image:") or styleContent.startswith("overflow") or styleContent.startswith("top:") or styleContent.startswith("height:") or styleContent.startswith("position:") or styleContent.startswith("text-align:") or styleContent.startswith("margin:"):
                        pass
                    else:
                        #TODO Commented but should be added in a verbose mode
                        #print("HTMLParserForXlsxWriter: UNHANDLED STYLE: " +  attr[0] + ' with value: ' + styleContent + ' for TAG: '+tag)
                        pass
            elif attr[0] == 'href' :
                href=attr[1]
                #Emulate URLs, Files links, or link to model element or diagram using the self.hrefstyle
                if href != '': 
                    if href.startswith('http'): 
                        self.output.extend(['[url: ',self.hrefstyle,href,' ] '])
                    elif href.startswith('file') or href.startswith('local') :
                        self.output.extend(['[File: ',self.hrefstyle,href,' ] '])
                    elif href.startswith('hlink'):
                        self.output.extend(['[Link to Model Element or Diagram - ID=',self.hrefstyle,href,' ] '])
            #For HTML4 tag <Font color=...>
            elif attr[0] == 'color' :
                self.currentFont.set_font_color(attr[1])
            elif attr[0] == 'face' :
                self.currentFont.set_font_name(attr[1])
            elif attr[0] == 'size' :
                #TODO evaluate if we handle this case
                pass
            elif attr[0] == 'class':
                if attr[1] == 'strong':
                    self.currentFont.set_bold()
            elif attr[0] == 'title'or attr[0] == 'dir'or attr[0] == 'height' or attr[0] == 'width' or attr[0] == 'xmlns' or attr[0] == 'id' or attr[0] == 'lang' or attr[0] == 'unselectable' or attr[0] == 'contenteditable' or attr[0] == 'align' or attr[0] == 'rel' or attr[0] == 'target' or attr[0] == 'alt' or attr[0] == 'src' or attr[0] == 'border' or attr[0] == 'frameborder' or attr[0] == 'allowfullscreen' or attr[0] == 'longdesc':
                    pass       
            else:
                print("HTMLParserForXlsxWriter: UNHANDLED ATTR: " +  attr[0] + ' with value: ' + attr[1] + ' for TAG: '+tag)
        #####################################################################################################################
        # HTML TAG MANAGEMENT  #
        #####################################################################################################################
        if tag == 'li':
            self.liMode = True
            #We add a newline except on the first li of the first level
            if self.indentLevel > 1 or not self.firstLi:
                self.output.append(self.new_line)
            self.firstLi = False
            if self.ulMode:                 
                self.output.append(' ' * (self.indentStringSize * (self.indentLevel)) + '* ')
            else:
                self.ol_id[str(self.indentLevel)] = self.ol_id[str(self.indentLevel)] + 1
                self.output.append(' ' * (self.indentStringSize * (self.indentLevel)) + str(self.ol_id[str(self.indentLevel)]) + '. ')
        elif tag == 'ul' :
            self.ulMode = True
            self.indentLevel += 1
        elif tag == 'ol' :
            self.olMode = True
            self.indentLevel += 1
            self.ol_id[str(self.indentLevel)] = 0
        elif tag == 'u' or tag == 'ins':
            self.currentFont.set_underline()
        elif tag == 'strong' or tag == 'b' or tag == 'th':
            self.currentFont.set_bold()
        elif tag == 'del' :
            self.currentFont.set_font_strikeout()
        elif tag == 'q' :
            self.output.append('"')
        elif tag == 'em' or tag == 'address' or tag == 'var' or tag == 'cite' or tag == 'i' :
            self.currentFont.set_italic()
        elif tag == 'h1' :
            self.currentFont.set_bold()
            self.currentFont.set_font_size(int(self.defaultFontSize*2))
        elif tag == 'h2' :
            self.currentFont.set_bold()
            self.currentFont.set_font_size(int(self.defaultFontSize*1.5))
        elif tag == 'h3' :
            self.currentFont.set_bold()
            self.currentFont.set_font_size(int(self.defaultFontSize*1.17))
        elif tag == 'h4' :
            self.currentFont.set_bold()
            self.currentFont.set_font_size(int(self.defaultFontSize))
        elif tag == 'h5' :
            self.currentFont.set_bold()
            self.currentFont.set_font_size(int(self.defaultFontSize*0.83))
        elif tag == 'h6' :
            self.currentFont.set_bold()
            self.currentFont.set_font_size(int(self.defaultFontSize*0.67))
        elif tag == 'small' :
            self.currentFont.set_font_size(int(self.defaultFontSize*0.83))
        elif tag == 'big' :
            self.currentFont.set_font_size(int(self.defaultFontSize*1.17))
        elif tag == 'code' or tag == 'pre' or tag == 'tt' or tag == 'samp' or tag == 'kbd' :
            #Trying to mimic the "Monospace" Font
            self.currentFont.set_font_name('Courier New')
            pass
        #Dealing with <img src="" alt=""> tag/attributes    
        elif tag == 'img' :
            src=''
            alt=''
            for attr in attrs:
                if attr[0] == 'src' :
                    src = attr[1]
                elif attr[0] == 'alt' :
                    alt = attr[1]
            self.output.extend(['[image:' + alt + ' src=', self.hrefstyle,src ,' ] '])                  
        elif tag == 'table' :
            self.tableMode = True
        elif tag == 'span' :
            #TODO Look into what the SPAN tag does
            pass
        elif  tag == 'a' or tag == 'p' or tag == 'br' or tag== "div" or tag== "svg" or tag== "font" or tag== "iframe" or tag== "tbody" or tag== "tr" or tag== "td" or tag== "thead":
            pass
        else:
            print("HTMLParserForXlsxWriter: UNHANDLED TAG: "+tag)

##########################################################
# Managing closing of tags
##########################################################
    def handle_endtag(self, tag):
        if tag == 'ul' :
            self.indentLevel -=1
            if self.indentLevel == 0:
                self.ulMode = False
                self.firstLi = True
        elif tag == 'ol' :
            self.ol_id[str(self.indentLevel)] = 0
            self.indentLevel-=1
            if self.indentLevel == 0:
                self.olMode = False
                self.firstLi = True
        elif tag == 'li' :
            self.liMode = False
        elif tag == 'tr' :
            self.output.append(self.new_line)
        elif tag == 'th' or tag == 'td':
            self.output.append(' | ')
        elif tag == 'table' :
            self.tableMode = False
        elif tag == 'td' :
            self.output.append(' ' * self.indentStringSize)
        elif tag == 'p' or tag== "h1" or tag== "h2" or tag== "h3" or tag== "h4" or tag== "h5" or tag== "h6":
            #Adding a newline at the end of tags
            self.output.append(self.new_line)
        elif tag == 'q' :
            self.output.append('"')
    
##########################################################
# Extract the color from a Style attribute and transform it into the appropriate HTML Hexadecimal #000000 code 
##########################################################
    def __extractColor(self, styleContent): 
        pos = styleContent.find('rgb(')
        if pos != -1:
            #extract RGB values from HTML style="color:" attribute
            [r,g,b] = styleContent[pos+4:styleContent.find(')',pos)].split(",")
            #transform RGB int values to HTML Hexa color
            return "#{0:02x}{1:02x}{2:02x}".format(int(r),int(g),int(b))

##########################################################
# Initialize a new Default Font 
##########################################################
    def __init_default_font(self):
        self.currentFont = self.workbook.add_format()
        self.currentFont.set_font_size(int(self.defaultFontSize))
        self.currentFont.set_font_name(self.defaultFont)
