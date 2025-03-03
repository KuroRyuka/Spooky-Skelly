'''
Importaciones
'''
#Importaciones:
from ..core import *
from ..banners import *
from ..menutxt import *
from .simpleTools import *
from .tools import *
from ..colors import *


#Clase para todos los submenus:
class submenu:

    '''
    MENU GENERAL PARA ACCEDER A SUBMENUS
    '''
    def cmenu(self, b, m):
        #Preparacion para el menu
        cmenu=core()
        prompt=cmenu.prompt("Spooky💀Skelly#~ ")
        cmenu.clearTerminal()
        b=cmenu.banner(b)
        #Se hace un bucle tipico de un menu
        option=0
        while option < 99:
            cmenu.clearTerminal()
            print(b)
            print(m)
            #Hacemos el try except debido a que si meten un valor de tipo string este fallaria y no seguiria el programa.
            try:
                option=int(input(prompt))

                #Esta opcion es para el submenu de Information Gathering
                if option==1:
                    #Si ha metido como numero el 1
                    #Llamaremos al metodo de Information Gathering
                    self.infogathermenu(banners.bannerInfo,menuTxt.msgInfo)
                    
                #Esta opcion es para el submenu de Analysis
                elif option==2:
                    #Si ha metido como numero el 2
                    #Llamaremos al metodo de Dictionary Creation
                    self.analysis(banners.bannerAnalysis,menuTxt.msgAnalysis)
                
                #Esta opcion es para el submenu de Dictionary Creation
                elif option==3:
                    #Si ha metido como numero el 3
                    #Llamaremos al metodo de Password Attacks Offline
                    self.diccreation(banners.bannerDictionary,menuTxt.msgDicc)
                
                #Esta opcion es para el submenu de Password Attacks Online
                elif option==4:
                    #Si ha metido como numero el 4
                    #Llamaremos al metodo de Password Attacks Online
                    self.socialenginering(banners.bannerSocial,menuTxt.msgSocial)

                #Esta opcion es para Exit the tool
                elif option==99:
                    print("Saliendo de la herramienta...")
                    os.system("rm -rf ./ins-tools/*")
                    os.system("rm -rf .server")
                    os.system("rm -rf lib")
                    os.system("rm -rf package.json")
                    os.system("mv reports/* ./logs/analysis/hostspider/")
                    os.system("rm -rf wordlist*.txt")
                    os.system("rm -rf AdminHack.sh")
                    os.system("rm -rf src")
                    cmenu.ptc()
                    exit()
            except ValueError:
                option=0
                print("Fallo al meter los datos, Intentalo de nuevo.")
            except KeyboardInterrupt:
                self.cmenu(banners.banner, menuTxt.msgIndex)
    
    '''
    MENU INFOGATHERING
    SUBMENUS DE INFOGATHERING
    '''

    #Menu para information gathering.
    def infogathermenu(self, b, m):
        #Se hace un bucle tipico de un menu
        #Creamos los objetos mediante el constructor
        info=core()
        sTool=simpleTool()
        prompt=info.prompt("InfoGather#~ ")
        b=info.banner(b)
        #Borramos la pantalla del terminal
        info.clearTerminal()
        #Comenzamos el bucle que haria el menu.
        option=0
        while option < 99:
            info.clearTerminal()
            print(b)
            print(m)
            #Hacemos el try except debido a que si meten un valor de tipo string este fallaria y no seguiria el programa.
            try:
                option=int(input(prompt))
                #Esta opcion es para el Ping
                # [1] Ping
                if option==1:
                    sTool.ping()
                    info.ptc()

                #Esta opcion es para el Whois
                # [2] Whois
                elif option==2:
                    sTool.whois()
                    info.ptc()

                #Esta opcion es para el Traceroute
                # [3] Tracceroute
                elif option==3:
                    sTool.trace()
                    info.ptc()

                #Esta opcion es para el Nslookup
                # [4] Nslookup
                elif option==4:
                    sTool.nslookup()
                    info.ptc()

                #Esta opcion es para la mezcla de Ping, Whois, Traceroute y Nslookup
                # [5] Ping + Whois + Tracceroute + Nslookup
                elif option==5:
                    sTool.allinone()
                    info.ptc()

                #Para borrar los registros.
                # [6] Delete All Logs
                elif option==6:
                    info.deletelogs("info")
                    info.ptc()

                #Esta opcion es para Exit the tool
                # [99] Go back to Main Menu
                elif option==99 or option > 8:
                    self.cmenu(banners.banner, menuTxt.msgIndex)
            except ValueError:
                option=0
                print("Fallo al meter los datos, Intentalo de nuevo.")
            except KeyboardInterrupt:
                self.infogathermenu(banners.bannerInfo,menuTxt.msgInfo)
  
    '''
    MENU Dictionary Creation
    '''
    def diccreation(self, b, m):
        #Se hace un bucle tipico de un menu
        #Creamos los objetos mediante el constructor
        dic=core()
        cuppTool=tool("cupp")
        #crunchTool=tool("crunch")
        prompt=dic.prompt("DicCreation#~ ")
        b=dic.banner(b)
        #Borramos la pantalla del terminal
        dic.clearTerminal()
        #Comenzamos el bucle que haria el menu.

        #Se hace un bucle tipico de un menu
        option=0
        while option < 99:
            dic.clearTerminal()
            print(b)
            print(m)
            #Hacemos el try except debido a que si meten un valor de tipo string este fallaria y no seguiria el programa.
            try:
                option=int(input(prompt))
                #Esta opcion es para el CuPP
                # [1] CuPP
                if option==1:
                    cuppTool.run()
                    dic.ptc()
                #Esta opcion es para el Crunch
                # [2] Crunch
                #elif option==2:
                #    crunchTool.run()

                #Para borrar los registros.
                # [3] Delete All Logs
                elif option==2:
                    dic.deletelogs("dic")
                    dic.ptc()

                #Esta opcion es para Exit the tool
                # [99] Go back to Main Menu
                elif option==99:
                    self.cmenu(banners.banner, menuTxt.msgIndex)
            except ValueError:
                option=0
                print("Fallo al meter los datos, Intentalo de nuevo.")
            except KeyboardInterrupt:
                self.diccreation(banners.bannerDictionary,menuTxt.msgDicc)
    
    '''
    MENU ANALYSIS
    MENU NMAP
    '''
    def analysis(self, b, m):
        #Se hace un bucle tipico de un menu
        #Creamos los objetos mediante el constructor
        analysis=core()
        netTool=tool("netdiscover")
        spiderTool=tool("spider")
        adminTool=tool("adminHack")
        prompt=analysis.prompt("Analysis#~ ")
        b=analysis.banner(b)
        #Borramos la pantalla del terminal
        analysis.clearTerminal()
        #Comenzamos el bucle que haria el menu.
        option=0
        while option < 99:
            analysis.clearTerminal()
            print(b)
            print(m)
            #Hacemos el try except debido a que si meten un valor de tipo string este fallaria y no seguiria el programa.
            try:
                option=int(input(prompt))
                #Esta opcion es para el NMAP
                # [1] Nmap
                if option==1:
                    self.nmapMenu()
                    analysis.ptc()

                #Esta opcion es para el netDiscover
                # [2] Netdiscover
                elif option==2:
                    netTool.run()
                    analysis.ptc()

                #Esta opcion es para el HostSpider
                # [3] HostSpider
                elif option==3:
                    spiderTool.run()
                    analysis.ptc()

                #Esta opcion es para el AdminHack
                # [4] AdminHack
                elif option==4:
                    adminTool.run()
                    analysis.ptc()

                #Esta opcion es para Exit the tool
                # [99] Go back to Main Menu
                elif option==99 or option > 8:
                    self.cmenu(banners.banner, menuTxt.msgIndex)
            except ValueError:
                option=0
                print("Fallo al meter los datos, Intentalo de nuevo.")
            except KeyboardInterrupt:
                self.analysis(banners.bannerAnalysis,menuTxt.msgAnalysis)
    

    #Menu para la herramienta de nmap.
    def nmapMenu(self):
        nmap=core()
        nmap.exDirect("./logs/info/")
        #Variable para mostrar por pantalla el prompt
        prompt=nmap.prompt("Nmap#~ ")
        option=0
        nmap.clearTerminal()
        #Comenzamos el bucle para realizar el menu de nmap
        while option < 99:
            nmap.clearTerminal()
            print(banners.bannerNmap)
            print(menuTxt.msgNmap)
            option= int(input(prompt))
            print("Introduce el objetivo que deseas analizar: ")        
            #Hacemos el try except debido a que si meten un valor de tipo string este fallaria y no seguiria el programa.
            try:
                if option == 1:
                    #Para crear ficheros con la hora exacta a la que se hizo la prueba.
                    logPath = "./logs/info/nmap-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"
                    #Pedimos un valor mediante un mensaje de texto.
                    target=nmap.intro(prompt)
                    #Para crear el directorio para despues poder abrirlo e introducirle el banner.
                    os.system("touch " + logPath)
                    with open(logPath, "a") as txt:
                        txt.write(banners.bannerNmap)
                        txt.write('\n')
                    #Creamos el comando que queremos hacer
                    command="nmap -sV " + target + " | tee -a " + logPath
                    os.system(command)
                    nmap.ptc()
                elif option == 2:
                    #Para crear ficheros con la hora exacta a la que se hizo la prueba.
                    logPath = "./logs/info/nmap-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"
                    #Pedimos un valor mediante un mensaje de texto.
                    target=nmap.intro(prompt)  
                    #Para crear el directorio para despues poder abrirlo e introducirle el banner.
                    os.system("touch " + logPath)
                    with open(logPath, "a") as txt:
                        txt.write(banners.bannerNmap)
                        txt.write('\n')
                    #Creamos el comando que queremos hacer
                    command="nmap -Pn " + target + " | tee -a " + logPath
                    os.system(command)
                    nmap.ptc()
                elif option == 3:
                    #Para crear ficheros con la hora exacta a la que se hizo la prueba.
                    logPath = "./logs/info/nmap-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"
                    #Pedimos un valor mediante un mensaje de texto.
                    target=nmap.intro(prompt)
                    #Para crear el directorio para despues poder abrirlo e introducirle el banner.
                    os.system("touch " + logPath)
                    with open(logPath, "a") as txt:
                        txt.write(banners.bannerNmap)
                        txt.write('\n')
                    #Creamos el comando que queremos hacer
                    command="nmap -A " + target + " | tee -a " + logPath
                    #Lo ejecutamos mediante el os.system
                    os.system(command)
                    nmap.ptc()
                elif option==99 or option > 8:
                    self.infogathermenu(banners.bannerInfo,menuTxt.msgInfo)
            except KeyboardInterrupt:
                self.nmapMenu()

    '''
    MENU SOCIAL ENGINERING
    '''
    def socialenginering(self, b, m):
        #Se hace un bucle tipico de un menu
        #Creamos los objetos mediante el constructor
        social=core()
        delvedTool=tool("delvedleak")
        little=tool("littlebrother")
        pyphisher=tool("pyphisher")
        #grab=tool("grab")
        prompt=social.prompt("SocialEnginering#~ ")
        b=social.banner(b)
        #Borramos la pantalla del terminal
        social.clearTerminal()

        #Se hace un bucle tipico de un menu
        option=0
        while option < 99:
            social.clearTerminal()
            print(b)
            print(m)
            #Hacemos el try except debido a que si meten un valor de tipo string este fallaria y no seguiria el programa.
            try:
                option=int(input(prompt))
                #Esta opcion es para el pyphisher
                # [1] pyphisher
                if option==1:
                    pyphisher.run()
                    social.ptc()

                #Esta opcion es para el delved
                # [2] delved
                elif option==2:
                    delvedTool.run()
                    social.ptc()

                #Esta opcion es para el LittleBrother
                # [3] LittleBrother
                elif option==3:
                    little.run()
                    social.ptc()
                
                    '''
                    #Esta opcion es para el Grab
                    # [4] Grab
                    elif option==4:
                        grab.run()
                        social.ptc()
                    '''
                
                #Esta opcion es para borrar los logs que no se necesitan ya.
                # [5] 
                elif option==4:
                    social.deletelogs("social")
                    social.ptc()

                #Esta opcion es para Exit the tool
                elif option==99 or option > 6:
                    self.cmenu(banners.banner, menuTxt.msgIndex)
            except ValueError:
                option=0
                print("Fallo al meter los datos, Intentalo de nuevo.")
            except KeyboardInterrupt:
                self.socialenginering(banners.bannerSocial,menuTxt.msgSocial)
