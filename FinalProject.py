#!/usr/bin/python
# -*- coding: utf-8 -*-



import cgi

def htmlTop():
    print '''Content-type:text/html\n\n
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title> mAd LiBs </title>
            </head>
            <body>'''

def htmlTail():
    print '''</body>
        </html>'''


def main():
    htmlTop()
    print '<h1>  Angry LIBs</h1>'
    print '''There once was a unicorn that was
      <form style = "display:inline;">
         <input type="text" one="oone" placeholder = "adj" style = "display:inline;">
    </form> '''



    htmlTail()

main()


 
<form method="post" action="N.py">
            Adjective(singular; describe an object) <input type="text"
                                                one="oone"
                                                placeholder="adjective"
                                                autofocus= required ="required">”
<br>
Noun(singular; this will be the protagonist) <input type="text"
                                                one="oone"
                                                placeholder="adjective"
                                                autofocus= required ="required">”



</p> '
    htmlTail()

main()



NCS
#!/usr/bin/python

import cgi

def htmlTop():
    print '''Content-type:text/html\n\n\
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title>NCS MadLibs.</title>
        </head>
        <body>
            <form method="post" action="NCShtml.py">
                Please enter your first name <input type="text"
                                                name="word"
                                                placeholder="e.g. Jacket"
                                                autofocus= required ="required">
                <br>
                Please enter your first name <input type="text"
                                                name="word"
                                                placeholder="e.g. Fight"
                                                autofocus= required ="required">
                <br>
                Please enter your first name <input type="text"
                                                name="word"
                                                placeholder="e.g. Majestic"
                                                autofocus= required ="required">
                <br>
                <input type="submit" name="submitname" value="Submit Name">
            </form>
        '''
    
def htmlTail():
    print '''</body>
        </html>'''

def main():
    formData = cgi.FieldStorage()
    htmlTop()
    print 'This is the story <em>{}</em> <em>{}</em> <em>{}</em>.'.format(formData.getvalue('word'))
    htmlTail()

if __name__=='__main__':
    try:
        main()
    except:
        cgi.print_exception()

(SECTION 2)
<!DOCTYPE html>

<html>
   <head>
      <meta charset="utf-8"/>
      <title>Name Form</title>
    </head>

    <body>
        <form method="post" action="processnameCGI.py">
            Please enter your first name <input type="text"
                                                name="firstname"
                                                placeholder="e.g. Lily"
                                                autofocus= required ="required">
            <br>
            <input type="submit" name="submitname" value="Submit Name">
        </form>

    </body>

(SECTION 3)
#!/usr/bin/python

import cgi

def htmlTop():
    print '''Content-type:text/html\n\n\
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title>Name Form.</title>
        </head>
        <body>
        '''

def htmlTail():
    print '''</body>
        </html>'''

def main():
    formData = cgi.FieldStorage()
    htmlTop()
print 'Hello <em>{story goes here}</em>!'.format(formData.getvalue('firstname'))
    htmlTail()

if __name__=='__main__':
    try:
        main()
    except:
        cgi.print_exception()


(SECTION 4)












Clarence’s Stuff

‘’’<p><form method="post" action="NCS.py">
            Adj <input type="text"
                                                one="oone"
                                                placeholder="adjective"
                                                autofocus= required ="required">
      <input type="submit" name="submitone" value="Submit One"></p>’’’






Ze MadLib

A gigantic contest in which you already may be a ___(noun,singular). Anyone, and we mean anyone, can enter this ___(adjective) 
contest. Just follow these ___(adjective) rules. Write down in ___(number) words or less why you think ___(your Mother’s name) 
should be elected ___(noun) Of The Year. Remember he/she does not know that you think so ___(adverb) of her. First prize will be
a deluxe, three-speed ___(piece of technology) plus a year’s supply of ___(food item). Second prize is a twenty one 
foot ___(noun). Third prize is a full-color ___(noun) plus a set of ___(animal,plural). Each entry must be accompanied by a 
stamped, self-addressed ___(extraterrestrial being). The decision will be final and in the event of a tie, 
duplicate ___(noun,plural) will be awarded.

