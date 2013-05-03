def html_to_rgb(colorstring):
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return "{}, {}, {}".format(r,g,b)



def rgb_to_html(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple





#===============================================================================
# copypasta of colorschemes and stuff here, use vim or something sensible to
# arrange everything... it's not ideal, but it's better than the alternative!
#===============================================================================

background=        "#252627"
foreground=        "#D8D8D8"
#*cursorColor:       #999999
#*colorBD:           #ffffff
#*colorUL:           #99cc66

colors= [  "#3E3E3E",
           "#CF516E",
           "#799351",
           "#ccc855",
           "#6FA5C7",
           "#b374a7",
           "#75a692",
           "#BBBBBB",
           "#525252",
           "#E87B94",
           "#8fa966",
           "#d1c78e",
           "#A4c9e0",
           "#d1a3c8",
           "#89bca7",
           "#EEEEEE"]

name = "pytest"
opacity = "0.9"
#background=  "#2D2C28"
#foreground=  "#A4A6AB"
#colors = [  "#5B5955",
            #"#C4756E",
            #"#559A6A",
            #"#9B8A4B",
            #"#6A8DCA",
            #"#B577AC",
            #"#019BAA",
            #"#DBDDE2",
            #"#707277",
            #"#F6A299",
            #"#82C896",
            #"#CAB775",
            #"#98BBFB",
            #"#E5A4DB",
            #"#53CAD9",
            #"#F7F9FF"]


#*colorBD:     #DBDDE2
#*colorIT:     #DBDDE2
#*colorUL:     #DBDDE2
#*cursorColor: #53CAD9




#===============================================================================
# actual printing of colorscheme done here 
#===============================================================================

print "[Background]"
print "Color={}".format(html_to_rgb(background))
print "Transparency=false"
print 
print "[BackgroundIntense]"
print "Color={}".format(html_to_rgb(background))
print "Transparency=false"



for i,color in enumerate(colors[:len(colors)/2]):
  print "[Color{}]".format(i)
  print "Color={}".format(html_to_rgb(color))
  print "Transparency=false"
  print
  print "[Color{}Intense]".format(i)
  print "Color={}".format(html_to_rgb(colors[i+len(colors)/2]))
  print "Transparency=false"
  print


print "[Foreground]"
print "Color={}".format(html_to_rgb(foreground))
print "Transparency=false"
print 
print "[ForegroundIntense]"
print "Bold=true"
print "Color={}".format(html_to_rgb(foreground))
print "Transparency=false"
print 
print "[General]"
print "Description={}".format(name)
print "Opacity={}".format(opacity)
print "Wallpaper="

