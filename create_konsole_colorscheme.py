def HtmlToRgb(colorstring):
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return "{}, {}, {}".format(r,g,b)

#===============================================================================
# copypasta of colorschemes and stuff here, use vim or something sensible to
# arrange everything... it's not ideal, but it's better than the alternative!
#===============================================================================


name = "pytest"
opacity = "0.9"

background=  "#2D2C28"
foreground=  "#A4A6AB"


colors = [  "#5B5955",
            "#C4756E",
            "#559A6A",
            "#9B8A4B",
            "#6A8DCA",
            "#B577AC",
            "#019BAA",
            "#DBDDE2",
            "#707277",
            "#F6A299",
            "#82C896",
            "#CAB775",
            "#98BBFB",
            "#E5A4DB",
            "#53CAD9",
            "#F7F9FF"]


#*colorBD:     #DBDDE2
#*colorIT:     #DBDDE2
#*colorUL:     #DBDDE2
#*cursorColor: #53CAD9




#===============================================================================
# actual printing of colorscheme done here 
#===============================================================================

print "[Background]"
print "Color={}".format(HtmlToRgb(background))
print "Transparency=false"
print 
print "[BackgroundIntense]"
print "Color={}".format(HtmlToRgb(background))
print "Transparency=false"



for i,color in enumerate(colors[:len(colors)/2]):
  print "[Color{}]".format(i)
  print "Color={}".format(HtmlToRgb(color))
  print "Transparency=false"
  print
  print "[Color{}Intense]".format(i)
  print "Color={}".format(HtmlToRgb(colors[i+len(colors)/2]))
  print "Transparency=false"
  print


print "[Foreground]"
print "Color={}".format(HtmlToRgb(foreground))
print "Transparency=false"
print 
print "[ForegroundIntense]"
print "Bold=true"
print "Color={}".format(HtmlToRgb(foreground))
print "Transparency=false"
print 
print "[General]"
print "Description={}".format(name)
print "Opacity={}".format(opacity)
print "Wallpaper="

