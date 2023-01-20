import json
import numbers
#import sys, os

#Globals
gDebug = False
gBulletDecor = "*"
# Disable
#def blockPrint(): sys.stdout = open(os.devnull, 'w')
# Restore
#def enablePrint(): sys.stdout = sys.__stdout__

def test():
    if gDebug: print("Package is Linked & Working")

#Root Level
def doc(content, carryForward=None):
    if gDebug: print("Parsing Doc: " + json.dumps(content))
    text=""
    for c in content:
        text += parse(c)
        pass
    return text

#Top Level
def blockquote(content, carryForward=None):
    if gDebug: print("Parsing BlockQuote: " + json.dumps(content))
    text=""
    for c in content:
        text += parse(c)
    return text

def paragraph(content, carryForward=None):
    if gDebug: print("Parsing Paragraph: " + json.dumps(content))
    text=""
    for c in content:
        text += parse(c)
    return text+"\n"

def bulletList(content, carryForward=None):    
    if gDebug: print("Parsing Bulletlist: " + json.dumps(content))
    text="\n"
    #carryForward=1
    carryForward=gBulletDecor
    for c in content:
        text += parse(c, carryForward)
        #carryForward += 1
    return text

def orderedList(content, carryForward=None):
    if gDebug: print("Parsing OrderedList: " + json.dumps(content))
    text="\n"
    carryForward=1
    for c in content:
        text += parse(c, carryForward)
        carryForward += 1
    return text

def codeBlock(content, carryForward=None):
    if gDebug: print("Parsing CodeBlock: " + json.dumps(content))
    text=""
    for c in content:
        text += parse(c)
    return text

def heading(content, carryForward=None):
    if gDebug: print("Parsing Heading: " + json.dumps(content))
    text=""
    for c in content:
        text += parse(c)
    return text+" \n"

#Child Level
def listItem(content, carryForward):
    if gDebug: print("Parsing ListItem: " + json.dumps(content))
    text=""
    for c in content:
        text += ((str(carryForward)+". ") if isinstance(carryForward, numbers.Number) else carryForward+" ")+parse(c)+'\n'
        #text += "* "+parse(c)+', '
    return text


#Inline Level
def text(obj, carryForward=None):
    if gDebug: print("Parsing Text: " + json.dumps(obj))
    text=obj['text']
    if obj.get('marks'):
        #Search for Marks
        for m in obj.get("marks"):
            try: text += parse(m)                          #Since marks are not in 'switcher' this will throw error which will be handled in next line and as a result, we'll get a blank
            except:
                if gDebug: print("Unable to parse Marks") 
                pass
    return text

def link(attrs, carryForward=None):
    if gDebug: print("Parsing Link")
    return " ("+attrs.get("href")+")"

def mention(attrs, carryForward=None):
    if gDebug: print("Parsing Mention")
    return attrs.get("text")

def emoji(attrs, carryForward=None):
    if gDebug: print("Parsing Emoji")
    return attrs.get("text")

def hardBreak(data=None, carryForward=None):
    if gDebug: print("Parsing HardBreak")
    return '\n'

#Driver Dependencies
switcher = {
    "doc": (doc, 'content'),
    "blockquote": (blockquote, 'content'),
    "paragraph": (paragraph, 'content'),
    "text": (text, 'self'),
    "hardBreak": (hardBreak, ''),
    "bulletList": (bulletList, 'content'),
    "orderedList": (orderedList, 'content'),
    "listItem": (listItem, 'content'),
    "codeBlock": (codeBlock, 'content'),
    "heading": (heading, 'content'),
    "link": (link, 'attrs'),
    "mention": (mention, 'attrs'),                              #Available only with type="text"
    "emoji": (emoji, 'attrs')                                   #Available only with type="text"        
}
replacers = ["\n\n\n\n\n", "\n\n\n\n", "\n\n\n", "\n\n"]


#Driver Functions
def parse(adf, carryForward=None):    
    type=switcher.get(adf['type'])                              #Get the ADF Type | Ex: "paragraph"
    fn=type[0]                                                  #Get the Function | Ex: paragraph()
    data=adf if type[1]=="self" else adf.get(type[1], None)     #Get the data to parse | Ex: "content" or "attrs" or "text"
    try: 
        result=fn(data, carryForward)                           #Ex: listItem(adf["content"], 1)                
        return result
    except:
        if gDebug: print("Unable to Parse: " + type)
        return ''

def startParsing(adf, debug=False, runReplacers=True, bulletDecor=None):
    global gDebug, gBulletDecor
    if bulletDecor: gBulletDecor=bulletDecor
    gDebug=debug                                                #Check Debug before Start    
    result = parse(adf)                                         #Do the Parsing
    if runReplacers:                                            #Run Replacers
        for r in replacers:        
            result=result.replace(r, '\n')    
    return result                                               #Return result
