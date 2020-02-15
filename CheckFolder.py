import ctypes,os
SPI_SETDESKWALLPAPER = 20 
BoogPic=os.path.abspath("Resources\Boog_bg.jpg")
NeedToFill=os.path.abspath("Resources\NeedToFill.png")
PathToCheck='./Puns'
if(len(os.listdir(PathToCheck))!=0):
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,  BoogPic, 3)
else:
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,  NeedToFill, 3)