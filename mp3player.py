from playsound import playsound
import wx
import sys 
# sys.exit()

# playsound('Infiltrate.mp3')
app = wx.App()
scrsize = wx.GetDisplaySize()
window = wx.Frame(None, title="MP3 Player", pos=(((scrsize[0]/2)-200),((scrsize[1]/2)-200)))
window.SetMinSize(size=(400, 400))
# window.Maximize(True)
mainpanel = wx.Panel(window)
filepath = "No File"
ststxt = wx.StaticText(mainpanel, label="No File", pos = (100, 50))
netstreamtxt = wx.StaticText(mainpanel, label="OR", pos = (100, 200))
netstreamtxtboxtxt = wx.StaticText(mainpanel, label="Network URL", pos = (60, 260))
def openFile(*args):
        filedialog = wx.FileDialog(mainpanel,"Choose the file or file location")
        if filedialog.ShowModal() == wx.ID_CANCEL:
                print("Nothing...")
                wx.MessageBox('No file was chosen', 'Alert', wx.OK)
        else:
                pathOfFile = filedialog.GetPath()
                playBtnnet.Disable()
                global filepath
                filepath = pathOfFile
                print(filepath)
                ststxt.SetLabel("File :" + str(filepath))
                window.SetSize(size=(600, 400))
                openBtn.Disable()
                global playBtn
                playBtn = wx.Button(mainpanel, -1, "Play", pos = (250, 100))
                playBtn.Bind(wx.EVT_BUTTON, playthis)
                print(filepath)
txtareanetwork = wx.TextCtrl(mainpanel, -1, "", pos = (150, 250), size=(200, 40))

def playthis(*args):
        print("Attempting to play...")
        print(filepath)
        if txtareanetwork.GetValue() != "":
                global killBtnnet
                killBtnnet = wx.Button(mainpanel, -1, "Kill The Network Beat", pos = (150, 150))
                killBtnnet.Bind(wx.EVT_BUTTON, killTheBeat)
                openBtn.Disable()
                playsound(str(txtareanetwork.GetValue()))
                print("Playing network...")
                print(txtareanetwork.GetValue())
        elif filepath == "No File":
                print("No Files")
        else:
                playBtn.Disable()
                global killBtn
                killBtn = wx.Button(mainpanel, -1, "Kill The Beat", pos = (150, 150))
                killBtn.Bind(wx.EVT_BUTTON, killTheBeat)
                playsound(str(filepath))
                playBtn.Enable()

def killTheBeat(*args):
        sys.exit()
        quit()

global playBtn
playBtnnet = wx.Button(mainpanel, -1, "Play URL", pos = (250, 300))
playBtnnet.Bind(wx.EVT_BUTTON, playthis)
openBtn = wx.Button(mainpanel, -1, "Open MP3", pos = (150, 100))
openBtn.Bind(wx.EVT_BUTTON, openFile)
window.Show()   
app.MainLoop()
