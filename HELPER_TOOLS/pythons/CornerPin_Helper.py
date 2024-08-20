
import nuke

def cornerpin_helper():
    node = nuke.selectedNode()
    
    n_class = node.Class()



    
    if n_class == 'CornerPin2D':
    
        node.addKnob(nuke.Tab_Knob('Reference Frame'))   
        node.addKnob(nuke.Int_Knob('ref_frame', 'Reference Frame'))
    
        node.addKnob(nuke.PyScript_Knob('current_frame', 'Set To Current Frame','nuke.thisNode().knob(\'ref_frame\').setValue(nuke.frame())'))
    
    
    
    
        node['from1'].setExpression('to1(ref_frame)')
        node['from2'].setExpression('to2(ref_frame)')
        node['from3'].setExpression('to3(ref_frame)')
        node['from4'].setExpression('to4(ref_frame)')
    
        
    
        node.knob('ref_frame').setValue(int(nuke.frame()))

    else:
        pass  

