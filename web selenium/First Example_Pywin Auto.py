from pywinauto.application import Application
import time

app = Application(backend="uia").start("notepad.exe")
time.sleep(2)
app.UntitleNotepad.type_keys("%FX")
time.sleep(2)
app.UntitleNotepad.menu_select("File->SaveAs")
app.SaveAs.ComboBox5.select("UTF-8")
