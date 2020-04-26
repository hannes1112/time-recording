#AWT
import sqlite3
import time
#print/7
#Note: skript html autoreload hinzufügen with aktuallisirungsrate as VAR

global aktuallisirungsrate
aktuallisirungsrate = 100
global start_sqplite_wiederholung
start_sqplite_wiederholung = 0
loop_AWT = 0
colums_int = 15 #Spalten
Firma = "SincoTec"

while start_sqplite_wiederholung == 0:
    loop_AWT = loop_AWT + 1
    start_time = time.time()

    path_DBST = '#'
    verbindung = sqlite3.connect (path_DBST)
    zeiger = verbindung.cursor()
    zeiger.execute("SELECT Name, Nachname, factor1, Tel, Ort, ID, Geburtstag_j, Geburtstag_m, Geburtstag_t, Notiz_show, OrtName, VonWert_1, BisWert_1, WasWert_1, ID_short FROM Dummydatabase2 ORDER BY Ort, factor1;")#Ort, factor1;
    inhalt = zeiger.fetchall()
    verbindung.close()

    print("AWT ---------------------------------------------------------")
    #print(inhalt)

    fobj = open("M_autoanwesenheitstafel.html","w")
    fobj.close()
    fobj = open("M_autoanwesenheitstafel.html","a")

    wiederholung = 0
    #print (inhalt[1][1])

    zeile1_1 ='<html><head><link rel="stylesheet" href="stylesheet.css"><title>Anwesenheitstafel</title><meta http-equiv="refresh" content="'
    zeile1_2 = str(aktuallisirungsrate)
    zeile1_3 ='"></head><body bgcolor="#FFFFE0"><body class="vbox viewport"><header>Anwesenheitstafel<font color="red">Aktualisierung in je '
    zeilel_4 = str(aktuallisirungsrate)
    zeilel_5 =' sek.</font></header>'

    #print(zeile1)
    fobj.write(zeile1_1 + zeile1_2 + zeile1_3 + zeilel_4 + zeilel_5)

    zeile2 ='<section class="hbox space-between" style="height: 240px">'
    #print(zeile2)
    fobj.write(zeile2)
    
    Var_birt = '''<img src="popupfenster/birthday.png" alt="G">'''
    Var_day = int((time.strftime("%d")))#01;31
    Var_month = int((time.strftime("%m")))#01;12
    print(type(Var_month))
    for arryinhalt in inhalt:
#Kerzen abfrage
        #if (arryinhalt[7]) == (Var_month) and str(arryinhalt[8]) == str(Var_day):
        #if str(arryinhalt[7]) == str(arryinhalt[8]):
            print("Geburtstag" + (arryinhalt[0]))
        #else:
            #print(type(str(arryinhalt[7])))
            arar = str(arryinhalt[8]) + str(arryinhalt[7])
            print(arar)
    #popupfenster/testpopup.html

            fenster_popup_bild_verzeichniss_name = "Fotos/"
            fenster_popup_bild = arryinhalt[0] + arryinhalt[1] + ".jpg"
            fenster_popup_bild_verzeichniss = fenster_popup_bild_verzeichniss_name + fenster_popup_bild

            fenster_popup_close_dalay = str(5000)#1000 = 1sek.
            popup_verzeichniss = "popupfenster/"
            fenster_popup_link = popup_verzeichniss + arryinhalt[0] + arryinhalt[1] + ".html"
            titel_popup_fenster ="Info:" + arryinhalt[0] + " " + arryinhalt[1] + Firma 

    #funktion in def legen ---!!
            fobj2 = open(fenster_popup_link,"w")
            fobj2.close()
            fobj2 = open(fenster_popup_link,"a")
            popup_fenster_inhalt_1 = "<html><head><title>" + titel_popup_fenster + "</title></head><body>" + '<link rel="stylesheet" href="stylesheet.css"><div align="center" class="fond"><script>setTimeout(function() {close();}, ' + fenster_popup_close_dalay + ');function close_window() {close();} </script><a href="#"><div class="principal"><div class="principal_petit"><div class="principal_img"><img src="' 
            popup_fenster_inhalt_2 = fenster_popup_bild_verzeichniss + '"' + """onerror="this.src=/Fotos'alternativ_ST.png';""" + ' alt="Missing Image" border="0" align="center" height="170" width="170px"/>' + """</div></div></div></a><div style=" padding:5px; color:#ffffff; font-weight:300; font-size:30px; font-family:""" + "'Roboto'" + ';padding-top:20px;"' + ">" + str(arryinhalt[0]) + " " + """<font style="font-weight:400;">""" + str(arryinhalt[1]) + """</font></div>"""
            popup_fenster_inhalt_3 = "<p>" + str(arryinhalt[8]) + "." + str(arryinhalt[7]) + "." + str(arryinhalt[6]) + "<br>" + str(arryinhalt[3]) + "<br>" + str(arryinhalt[10])
            popup_fenster_inhalt_4 = "<br>" + str(arryinhalt[13]) + "von" + str(arryinhalt[11]) + "bis" + str(arryinhalt[12]) + "</p>"
            popup_fenster_inhalt_5 = '<a href="#" style="text-decoration:none;" target="parent"><div style="  color:#ffffff; font-weight:300; font-size:20px; font-family:' + "'Roboto';" + '">Verbesserungsvorschlag einreichen</div></a><a href="javascript:close_window();">close</a></div></body></html>'
            fobj2.write(popup_fenster_inhalt_1 + popup_fenster_inhalt_2 + popup_fenster_inhalt_3 + popup_fenster_inhalt_4 + popup_fenster_inhalt_5)
            fobj2.close()
            
            #print(fenster_popup_bild)
            zeile3 ='<article class="flex' + str(arryinhalt[4]) + '"><div id="nichtmarkieren"><a target="popup" onclick="window.open' + """('', 'popup', 'width=580,height=600,scrollbars=no, toolbar=no,status=no,resizable=no,menubar=no,location=no,directories=yes,top=10,left=10')""" + '"href="' + fenster_popup_link + '" style="text-decoration: none" window.setTimeout("win.close()", 20);><span style="color:#000">' + str(arryinhalt[0]) + '<br>' + str(arryinhalt[1]) + '<br>' + str(arryinhalt[9]) + '<br>' + str(arryinhalt[3]) + '</span></a></div></article>'
            #Ort;Nachname;Name;Tel;
            #print(zeile3)
            fobj.write(zeile3)

            wiederholung += 1
            if wiederholung == colums_int:
                zeile4 =('</section><section class="hbox space-between" style="height: 240px">')
                #print(zeile4)
                fobj.write(zeile4)
                wiederholung = 0
            else:
                pass
    zeile5 =('</section><footer><a target="_blank" rel="noopener noreferrer" href="http://www.boothtml.de/" style="color:#FFFFFF">powerd by boothtml-Systeme</a></footer></body></html>')       
    #print(zeile5)
    fobj.write(zeile5)
    fobj.close()
    end_time = time.time()
    print("AWT " + "%.10f seconds" % (end_time - start_time))
    print("AWT Anwesenheitstafel abgerufen von 'SincoTecUserInfo2.db' erfolgreich aktuallisiert - delay " + str(aktuallisirungsrate) + "sek.")
    print("AWT " + time.strftime("%d.%m.%Y %H:%M:%S") + " //W. " + str(loop_AWT))
    print("AWT ---------------------------------------------------------")
    time.sleep(aktuallisirungsrate)



