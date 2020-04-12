import wx
import cv2
import numpy as np
import pyautogui


app = wx.App()
window = wx.Frame(None, title="Recorder")
window.SetMinSize(size=(200,200))


SCREEN_SIZE = wx.GetDisplaySize()
# Get Display Dimensions
#fourccodec = cv2.VideoWriter_fourcc(*"XVID")
#Define coded
out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
#Save target to save the file
# Detect Resolution
print(str(wx.GetDisplaySize()[0]) + "x" + str(wx.GetDisplaySize()[1]))

mainpanel = wx.Panel(window)

def record(*args):
	while True:
	    # make a screenshot
	    img = pyautogui.screenshot()
	    # convert these pixels to a proper numpy array to work with OpenCV
	    frame = np.array(img)
	    # convert colors from BGR to RGB
	    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	    # write the frame
	    out.write(frame)
	    # show the frame
	    cv2.imshow("screenshot", frame)
	    # if the user clicks q, it exits
	    if cv2.waitKey(1) == ord("q"):
	        break
	cv2.destroyAllWindows()
	out.release()
	
recordbtn = wx.Button(mainpanel, -1, "Record", pos = (100, 50), size = (100, 30))
recordbtn.Bind(wx.EVT_BUTTON, record)
# recordbtnn = wx.Button(mainpanel, -1, "Stop and Kill", pos = (100, 150), size = (100, 30))
# recordbtnn.Bind(wx.EVT_BUTTON, stoprecord)
window.Show()
app.MainLoop()