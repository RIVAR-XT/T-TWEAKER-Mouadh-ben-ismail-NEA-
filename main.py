
import winreg as abit
import win32gui
import win32con
import subprocess
import time
import os
import shutil
import powerplan

beigen = time.time()

class custom():
    def __init__(self) -> None:
        #paths
        self.explorerad = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        self.pathcolor = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        self.pathtask = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Accent"
        self.pathacc = r"Software\Microsoft\Windows\CurrentVersion\Themes\Accent"
        self.comm = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Communications"
        self.chat = r"Software\Policies\Microsoft\Windows\Windows Chat"
        self.search = r"Software\Policies\Microsoft\Windows"
        self.seapa = r"Software\Microsoft\Windows\CurrentVersion\Search"
      
        #name of file to change
        self.APalette = r"AccentPalette"
        self.SCMenu = r"StartColorMenu"
        self.fileforcolorsys = r"SystemUsesLightTheme"
        self.fileforcolorapp = r"AppsUseLightTheme"
        self.taskbarAL = r"TaskbarAl"
        self.cp = r"ColorPrevalence"
        self.ac = r"AccentColor"
        #the values
        self.lightSCMenu = int("FF000000", 16 )
        self.on = 0
        self.off = 1
        self.darkAPalette =bytes([
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])
        self.darkSCMenu = int("00000000")
        self.lightAPalette = bytes([
            0x6b, 0x6b, 0x6b, 0xff, 0x59, 0x59, 0x59, 0xff, 
    0x4c, 0x4c, 0x4c, 0xff, 0x3f, 0x3f, 0x3f, 0xff,
    0x33, 0x33, 0x33, 0xff, 0x26, 0x26, 0x26, 0xff,
    0x14, 0x14, 0x14, 0xff, 0x88, 0x17, 0x98, 0x00 
])
        

    #Option to change from dark to light(turn off dark color after transition on menu iccon bug fix)
    def changedark(self):

         with abit.CreateKey(abit.HKEY_CURRENT_USER , self.pathcolor) as fil:
             abit.SetValueEx(fil , self.fileforcolorsys , 0 , abit.REG_DWORD , self.on)
             abit.SetValueEx(fil , self.fileforcolorapp , 0 , abit.REG_DWORD , self.on)

         with abit.CreateKey(abit.HKEY_CURRENT_USER , self.pathtask) as filler:
             abit.SetValueEx(filler , self.APalette , 0 , abit.REG_BINARY , self.darkAPalette)
             abit.SetValueEx(filler , self.SCMenu , 0 , abit.REG_DWORD , self.darkSCMenu)

         win32gui.SendMessage(win32con.HWND_BROADCAST , win32con.WM_SETTINGCHANGE , 0 , "ImmersiveColorSet" )


    def changelight(self):

        with abit.CreateKey(abit.HKEY_CURRENT_USER , self.pathcolor) as fil:
             abit.SetValueEx(fil , self.fileforcolorsys , 0 , abit.REG_DWORD , 1)
             abit.SetValueEx(fil , self.fileforcolorapp , 0 , abit.REG_DWORD , 1)

        with abit.CreateKey(abit.HKEY_CURRENT_USER , self.pathtask) as filler:
             abit.SetValueEx(filler , self.APalette , 0 , abit.REG_BINARY , self.lightAPalette)
             abit.SetValueEx(filler , self.SCMenu , 0 , abit.REG_DWORD , self.lightSCMenu)  

        win32gui.SendMessage(win32con.HWND_BROADCAST , win32con.WM_SETTINGCHANGE , 0 , "ImmersiveColorSet" )


#change windows st mid or left
    def changeleft(self):
        with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced") as ex :
            abit.SetValueEx(ex , self.taskbarAL , 0 , abit.REG_DWORD , 0)
        
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Environment")

    def changemid(self):
        with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced") as waita :
            abit.SetValueEx(waita , self.taskbarAL , 0 ,abit.REG_DWORD , 1)

        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Environment")


    def enable_animation(self):
        
            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Control Panel\Desktop") as rd :
               abit.SetValueEx(rd , "MenuShowDelay" , 0 , abit.REG_SZ , "400")
               abit.SetValueEx(rd , "DragFullWindows" , 0 , abit.REG_SZ ,"1")
               abit.SetValueEx(rd , "FontSmoothing" , 0 , abit.REG_SZ , "2")
        
            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Control Panel\Desktop\WindowMetrics") as rw :
               abit.SetValueEx(rw , "MinAnimate" , 0 , abit.REG_SZ , "1")
            
            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects") as an1:
                 abit.SetValueEx(an1 , "VisualFXSetting" , 0 , abit.REG_DWORD , 0 )
            

            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\DWM") as key8 :
                abit.SetValueEx(key8 , "Animations" , 0 , abit.REG_DWORD , 1)
                abit.SetValueEx(key8 , "EnableAeroPeek" , 0 , abit.REG_DWORD , 1 )
                abit.SetValueEx(key8 , "AlwaysHibernateThumbnails" , 0 , abit.REG_DWORD , 1)

            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced") as tan:
                abit.SetValue(tan , "TaskbarAnimations" , 0 , abit.REG_DWORD , 1)
                abit.SetValueEx(tan , "IconsOnly" , 0, abit.REG_DWORD , 0)
                abit.SetValueEx(tan , "ListviewAlphaSelect" , 0 , abit.REG_DWORD , 1)
                abit.SetValueEx(tan , "ListviewShadow" , 0 , abit.REG_DWORD , 1)
            

            win32gui.SendMessage(win32con.HWND_BROADCAST , win32con.WM_SETTINGCHANGE , 0 , "Environment ")



    def remove_animation(self):

            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Control Panel\Desktop") as rd :
               abit.SetValueEx(rd , "MenuShowDelay" , 0 , abit.REG_SZ , "0")
               abit.SetValueEx(rd , "DragFullWindows" , 0 , abit.REG_SZ ,"0")
               abit.SetValueEx(rd , "FontSmoothing" , 0 , abit.REG_SZ , "0")
        
            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Control Panel\Desktop\WindowMetrics") as rw :
               abit.SetValueEx(rw , "MinAnimate" , 0 , abit.REG_SZ , "0")
            
            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects") as an1:
                 abit.SetValueEx(an1 , "VisualFXSetting" , 0 , abit.REG_DWORD , 3 )
            

            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\DWM") as key8 :
                abit.SetValueEx(key8 , "Animations" , 0 , abit.REG_DWORD , 0)
                abit.SetValueEx(key8 , "EnableAeroPeek" , 0 , abit.REG_DWORD , 0 )
                abit.SetValueEx(key8 , "AlwaysHibernateThumbnails" , 0 , abit.REG_DWORD , 0)

            with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced") as tan:
                abit.SetValue(tan , "TaskbarAnimations" , 0 , abit.REG_DWORD , 0)
                abit.SetValueEx(tan , "IconsOnly" , 0, abit.REG_DWORD , 1)
                abit.SetValueEx(tan , "ListviewAlphaSelect" , 0 , abit.REG_DWORD , 0)
                abit.SetValueEx(tan , "ListviewShadow" , 0 , abit.REG_DWORD , 0)
            

            win32gui.SendMessage(win32con.HWND_BROADCAST , win32con.WM_SETTINGCHANGE , 0 , "Environment ")
#start of performance tweaks
# bloatwear
    def rbloat(self):
        allowlist = [
            '*WindowsCalculator*',
            '*Office.OneNote*',
            '*Microsoft.net*',
            '*MicrosoftEdge*',
            '*WindowsStore*',
            '*WindowsTerminal*',
            '*WindowsNotepad*',
            '*Paint*'
        ]
        def pwex(command):
             result = subprocess.run(["powershell", "-Command", command] , capture_output=True , text=True , check=True)
             return result.stdout.strip()
                

        command = f"Get-AppxPackage | Select-Object -ExpandProperty Name"
        packo = pwex(command)
        packages = packo.splitlines()
        

        for d in allowlist :
             command = f"(Get-AppxPackage -Name '{d}').Dependencies | ForEach-Object {{ '*' + $_.Name + '*' }}"
             depout = pwex(command)
             d = depout.splitlines()

             for dep in d :
                if dep and not dep in allowlist:
                    allowlist.append(dep)
            
        for app in packages :
            match = any(app.startswith(item.replace('*', '')) for item in allowlist)
            if not match :
                possibletoremoveout = pwex(f"(Get-AppxPackage -Name '{app}' -AllUsers).NonRemovable -eq $false")
                if possibletoremoveout == "True" :
                 subprocess.run(["powershell", "-Command", f"Get-AppxPackage -AllUsers -Name '{app}' -PackageTypeFilter Bundle | Remove-AppxPackage -AllUsers"])

        #dissable suggest 
        with abit.CreateKey(abit.HKEY_CURRENT_USER, r"Software\Policies\Microsoft\Windows") as key_path:
            abit.CreateKey(key_path, "Explorer")
            
        with abit.CreateKey(abit.HKEY_CURRENT_USER, r"Software\Policies\Microsoft\Windows\Explorer") as b:
                abit.SetValueEx(b, "DisableSearchBoxSuggestions", 0, abit.REG_DWORD, 1)
            
        #disable feed
        with abit.CreateKey(abit.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows") as key_path2:
                abit.CreateKey(key_path2, "Windows Search")
            
        with abit.CreateKey(abit.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search") as b1:
                abit.SetValueEx(b1, "EnableFeeds", 0, abit.REG_DWORD, 0)

        # adjust cloud features
        with abit.CreateKey(abit.HKEY_LOCAL_MACHINE , r"Software\Policies\Microsoft\Windows" ) as keypath3 :
                abit.CreateKey(keypath3 , "CloudContent")
            
        with abit.CreateKey(abit.HKEY_LOCAL_MACHINE , r"Software\Policies\Microsoft\Windows\CloudContent") as b2 :
                abit.SetValueEx(b2 , "DisableCloudOptimizedContent" , 0 , abit.REG_DWORD , 1)
                abit.SetValueEx(b2 , "DisableConsumerAccountStateConten" , 0 , abit.REG_DWORD , 1)
                abit.SetValueEx(b2 , "DisableWindowsConsumerFeatures" , 0 , abit.REG_DWORD ,1)
    
        # adjust task
        with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced") as keypath3 :
                abit.SetValueEx(keypath3 , "TaskbarMn" , 0 , abit.REG_DWORD , 0)

        # adjust meett icon
        with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Policies") as keypath4 :
                abit.CreateKey(keypath4 , "Explorer")

        with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer") as b3 :
                abit.SetValueEx(b3 , "HideSCAMeetNow" , 0 , abit.REG_DWORD , 1)

        with abit.CreateKey(abit.HKEY_CURRENT_USER , r"Software\Microsoft\Windows\CurrentVersion\Search") as keypath5 :
                abit.SetValueEx(keypath5 , "SearchboxTaskbarMode" , 0 ,abit.REG_DWORD , 1)


        # Notify system about the changes
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Environment")
    
#start apps
    def stapps(self):
       with abit.OpenKey(abit.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, abit.KEY_ALL_ACCESS) as ru:
            try:
                 keylist =[]
                 right = 0
                 while True:
                    try:
                      name , value , type = abit.EnumValue(ru, right)
                      keylist.append(name)
                      right += 1
                    except WindowsError :  
                         break
                    
                    
                 for key in keylist:
                      try:
                        abit.DeleteKey(ru, key)
                      except Exception as e:
                           print(f"Error deleting key: {key}, {e}")


                 win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Environment")
            except Exception as e:
                  print(e)

#temp files
    def removetempfiles(self):
            temp_dirs = [r"C:\WINDOWS\Temp", os.path.expanduser("~") + r"\AppData\Local\Temp"]
            
            for temp_dir in temp_dirs:
                try:
                    for root, dirs, files in os.walk(temp_dir, topdown=False):
                        for file in files:
                            file_path = os.path.join(root, file)
                            try:
                                os.unlink(file_path)
                            except Exception as e:
                                print(f"Error deleting file {file_path}: {e}")
                        
                        for dir in dirs:
                            dir_path = os.path.join(root, dir)
                            try:
                                shutil.rmtree(dir_path)
                            except Exception as e:
                                print(f"Error deleting directory {dir_path}: {e}")
                
                except Exception as e:
                    print(f"Error accessing directory: {temp_dir}, {e}")

# mouse acc
    def rmouseacc(self):
        with abit.CreateKey(abit.HKEY_CURRENT_USER, r"Control Panel\Mouse") as mouse:
        # Turn off mouse acceleration
           abit.SetValueEx(mouse, "MouseSpeed", 0, abit.REG_SZ, "0")
           abit.SetValueEx(mouse, "MouseThreshold1", 0, abit.REG_SZ, "0")
           abit.SetValueEx(mouse, "MouseThreshold2", 0, abit.REG_SZ, "0")

    # Notify the system about the changes
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Mouse")

    def onmouseacc(self):
                with abit.CreateKey(abit.HKEY_CURRENT_USER, r"Control Panel\Mouse") as mouse:
        # Turn off mouse acceleration
                   abit.SetValueEx(mouse, "MouseSpeed", 0, abit.REG_SZ, "1")
                   abit.SetValueEx(mouse, "MouseThreshold1", 0, abit.REG_SZ, "6")
                   abit.SetValueEx(mouse, "MouseThreshold2", 0, abit.REG_SZ, "10")

    # Notify the system about the changes
                win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "Mouse")
    

    #change power plan to high 
    def powerhigh(self):
        powerplan.change_current_scheme_to_high()
    def powerbalanced(self):
        powerplan.change_current_scheme_to_balanced()
    def powerlow(self):
        powerplan.change_current_scheme_to_low()

#backup section or restore point 
    def createarestorepoint(self):
     descre = input("Enter description for the restore point: ")
     elamr = f'Checkpoint-Computer -Description "{descre}" -RestorePointType "MODIFY_SETTINGS"'
     hi =subprocess.run(["powershell", "-Command", elamr] , 
     capture_output=True,
     text=True,
     shell=True)
     if hi.returncode == 0 :
        print("Restore point created successfully") 
     else:
        print(f"Failed to create restore point {hi.stderr.strip()}")


  

    def restorepoint(self):
        subprocess.run("rstrui.exe")


        

        





         
