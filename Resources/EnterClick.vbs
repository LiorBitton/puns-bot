WScript.Sleep(4000)
set shl = createobject("wscript.shell")
shl.SendKeys "{Down}"
WScript.Sleep(250)
shl.SendKeys "{Enter}"