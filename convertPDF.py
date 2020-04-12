#!/usr/bin/env python3
import wx
import subprocess


app = wx.App()
window = wx.Frame(None, title="Convert To PDF")
window.SetMinSize(size=(700,200))
window.Maximize(True)
mainpanel = wx.Panel(window)
fontModern= wx.Font(12, wx.MODERN, wx.ITALIC, wx.NORMAL)
def openFileDialog(*args):
	filedialog = wx.FileDialog(mainpanel,"Choose the file or file location")
	if filedialog.ShowModal() == wx.ID_CANCEL:
		print("Nothing...")
		wx.MessageBox('No file was chosen', 'Alert', wx.OK)

	else:
		pathname = filedialog.GetPath()
		textone.SetLabel("File : " + pathname)
		openFileDialogbtn.Disable()
		subprocess.Popen(["libreoffice", "--convert-to", "pdf", pathname + ""])
		print("Done Process")
		openFileDialogbtn.Disable()
		textone.SetLabel("File : Done Converting to PDF")
		openFileDialogbtn.Enable()
		# libroffice --convert-to pdf myfile.docx
		# the command only works for linux with libre installed


textone = wx.StaticText(mainpanel,label="Convert to pdf using this mini tool for linux", pos = (100, 100), size = (200, 100))
openFileDialogbtn = wx.Button(mainpanel, -1, "Convert To PDF", pos = (100, 200), size= (150, 50))
openFileDialogbtn.Bind(wx.EVT_BUTTON,openFileDialog)

textone.SetFont(fontModern)
window.Show(True)
app.MainLoop()
