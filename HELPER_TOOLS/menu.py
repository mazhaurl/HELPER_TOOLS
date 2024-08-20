import nuke
import sys
import os
import webbrowser
import backdrop_helper
import platform
import RGB_SPLIT_HELPER
import AUTO_PROJECT_HELPER_01

from nukescripts import panels
import Backdrop_Helper_Toolkit

import backdrop_mini


# .nuke dir

#change your dir here

Win_Dir = 'C:/Users/shuvo/.nuke' 
MacOSX_Dir = 'mac'
Linux_Dir = "/home/shuvo/.nuke"



if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	Dir = None



#Gizmos and Pyton

GizmosMenu = nuke.menu('Nodes').addMenu('Helper_Tools', icon=dir+"\HELPER_TOOLS\icons\helper_icon_01.png")
GizmosMenu.addCommand('TECH_CHECK_HELPER', 'nuke.createNode("TECH_CHECK_HELPER")')
GizmosMenu.addCommand('ABERRATION_HELPER', 'nuke.createNode("ABERRATION_HELPER")')

GizmosMenu.addCommand("WRITE_HELPER", 'nuke.nodePaste(dir+"/HELPER_TOOLS/gizmos/WRITE_HELPER_1.3.nk")')

GizmosMenu.addCommand("CameraShake_Helper", 'nuke.nodePaste(dir+"/HELPER_TOOLS/gizmos/CameraShake_Helper.nk")')

GizmosMenu.addCommand("ContactSheet_Helper", 'nuke.nodePaste(dir+"/HELPER_TOOLS/gizmos/ContactSheet_Helper.nk")')

GizmosMenu.addCommand('RGB_SPLIT','RGB_SPLIT_HELPER.my_shuffleSplit()' )

GizmosMenu.addCommand('Backdrop_Helper','backdrop_helper.backdrop_helper()','shift+B', shortcutContext=2  )

GizmosMenu.addCommand('PROJECT_HELPER','AUTO_PROJECT_HELPER_01.AUTO_PROJECT_HELPER()','shift+P', shortcutContext=2 )




panels.registerWidgetAsPanel('Backdrop_Helper_Toolkit.backdrop_helper_toolkit', 'Backdrop Helper Toolkit', 'www.shuvofx.com')

panels.registerWidgetAsPanel('backdrop_mini.backdrop_mini', 'Backdrop_Helper_MINI', 'www.shuvofx.com')