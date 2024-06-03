from typing import Optional
import time
import threading
import c4d

doc: c4d.documents.BaseDocument  # The active document
op: Optional[c4d.BaseObject]  # The active object, None if unselected

def main():
    currentDocument = c4d.documents.GetActiveDocument()
    activeView = currentDocument.GetActiveBaseDraw()
    baseContainer = c4d.BaseContainer()
    while c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SPACE, baseContainer):
        if baseContainer.GetInt32(c4d.BFM_INPUT_VALUE)==0:
            break
        if baseContainer.GetInt32(c4d.BFM_INPUT_VALUE)==1:
            MoveTest(activeView,baseContainer)

def MoveTest(activeBaseDraw,baseContainer):
    editorCam = activeBaseDraw.GetEditorCamera()
    editorCamPos = editorCam.GetAbsPos()
    moveVector = c4d.Vector(0,0,0)
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_UP, baseContainer):
        if baseContainer.GetInt32(c4d.BFM_INPUT_VALUE)==1:
            moveVector = c4d.Vector(0,0,50)
            moveVector = editorCam.GetMg().MulV(moveVector)
            editorCam.SetAbsPos(editorCamPos + moveVector)
            c4d.EventAdd() # Calls and Updates Main Thread
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_DOWN, baseContainer):
        if baseContainer.GetInt32(c4d.BFM_INPUT_VALUE)==1:
            moveVector = c4d.Vector(0,0,-50)
            moveVector = editorCam.GetMg().MulV(moveVector)
            editorCam.SetAbsPos(editorCamPos + moveVector)
            c4d.EventAdd()            
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_LEFT, baseContainer):
        if baseContainer.GetInt32(c4d.BFM_INPUT_VALUE)==1:
            moveVector = c4d.Vector(-50,0,0)
            moveVector = editorCam.GetMg().MulV(moveVector)
            editorCam.SetAbsPos(editorCamPos + moveVector)
            c4d.EventAdd()            
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_RIGHT, baseContainer):
        if baseContainer.GetInt32(c4d.BFM_INPUT_VALUE)==1:
            moveVector = c4d.Vector(50,0,0)
            moveVector = editorCam.GetMg().MulV(moveVector)
            editorCam.SetAbsPos(editorCamPos + moveVector)
            c4d.EventAdd()            

if __name__ == '__main__':
    main()