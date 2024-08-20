
import nuke
import nukescripts
import os

import re

def AUTO_PROJECT_HELPER():
    try: 
        #ProjectName
        p = nuke.Panel('AUTO_PROJECT_HELPER')
        
        
        #File Path
        
        p.addClipnameSearch('Import Shot', '')
        
        p.addFilenameSearch('Set Project Dir', '')
        
        #Folder Structure
        
        
        
        
        
        
        #Panel Size
        p.setWidth(600)
        p.show()
        
        #get shotPath
        shot_path = p.value('Import Shot')
        
        
        
        
        
        
        project_path = p.value('Set Project Dir')
        
        
        #shot_dir = os.path.dirname(shot_path)
        
        Project_dir = os.path.dirname(project_path)
        
        
        #Creating Folder
    
    
        os.makedirs(Project_dir +'/PRECOMP')
        
        os.makedirs(Project_dir +'/RENDER')
        
        os.makedirs(Project_dir +'/ASSETS')
        
        os.makedirs(Project_dir +'/OTHERS')
        

    
    
    
    
        #Shot Importing
        
        filelist = [shot_path]
        
        if filelist != None:
            for f in filelist:
                readShot = nuke.createNode("Read", "file {" + f + "}", inpanel = False)
        
        
        
        
        path = re.split(' ',shot_path)
        
        
        
        
        
        #save V00
        
        #get Shot Name
        split_path = re.split('/',shot_path)
        
        
        fileName_with_extension = split_path[len(split_path)-1].split('.')
        
        
         
        shotName = fileName_with_extension[:1]
        
        
        shot_name_str = shotName[0]

        bad_chars = [';', '#']
        
        for i in bad_chars:
            shot_name_str = shot_name_str.replace(i, '')

        print(shot_name_str)
        
        
        
        
        shot_N_V = (shot_name_str +'_COMP_v000.nk')
        
        
        
        #backdrop Adding
        
        
        
        
        readShot['selected'].setValue(True)
        
        currentSelNode = nuke.selectedNode()
        
        Xw = currentSelNode['xpos'].getValue()
        Yw = currentSelNode['ypos'].getValue()
        
        if currentSelNode == nuke.selectedNode():
            backdrop = nukescripts.autoBackdrop()
            backdrop['label'].setValue('PlateA')
            backdrop['bdwidth'].setValue( 500 )
            backdrop['bdheight'].setValue( 500 )
            backdrop['xpos'].setValue( Xw - 225 )
            backdrop['ypos'].setValue( Yw - 200 )
        
        
        
        #project Settings

        readnode= nuke.toNode('Read1')
        
        firstFrame=readnode['first'].getValue()
        lastFrame=readnode['last'].getValue()

        width = readnode.width()
        height = readnode.height()
        pixelAspect = readnode.pixelAspect()
        
        formatName='%sx%s_Resolution' % (width, height)
        
        nuke.addFormat('%d %d %d %s' %(width, height, pixelAspect, formatName))



        
        
        root= nuke.root()
        
        root['first_frame'].setValue(firstFrame)
        root['last_frame'].setValue(lastFrame)
        
        root['format'].setValue(formatName)
        
        #SaceScript
        
        
        nkPath = os.path.join(Project_dir, shot_N_V)
        
        nuke.scriptSave(nkPath)
        nuke.scriptSaveAs(nkPath, overwrite=1) 
            
    except:
        
        pass

