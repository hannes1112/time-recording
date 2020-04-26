import mysql.connector
import time
import datetime
import re
import pyttsx3

engine = pyttsx3.init()

mydb = mysql.connector.connect(
  host="#",#
  user="#",
  passwd="#",
  database="#"
)
mycursor = mydb.cursor()

print("verbunden")

while True:
    id_var = input("Gebe ID ein:")
    #id_var = str(100)

    sql = ("SELECT firstname, surname, logstatus, bday, bmonth, be_read, gender, hours_per_week, location, day_hours FROM users WHERE longid = " + id_var)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.commit()

    if mycursor.rowcount == 1:
        print("validiert", mycursor.rowcount)
        f_n_qu_var = myresult[0][0]
        s_n_qu_var = myresult[0][1]
        l_s_qu_var = myresult[0][2] 
        b_d_qu_var = myresult[0][3]
        b_m_qu_var = myresult[0][4]
        r_r_qu_var = myresult[0][5]
        g_g_qu_var = myresult[0][6]
        h_w_qu_var = myresult[0][7]
        l_l_qu_var = myresult[0][8]
        d_h_qu_var = myresult[0][9]

        if g_g_qu_var == 0:
            g_g_qu_var = "Frau"
        elif g_g_qu_var == 1:
            g_g_qu_var = "Herr"
        else:
            g_g_qu_var = " "
            
        print("-----------------")
        time_current = datetime.datetime.now()#geburtstag überprüfung
        
        print(str(time_current.strftime("%m")[1]), str(b_m_qu_var), str(time_current.strftime("%m")), str(b_m_qu_var))
        print(str(time_current.strftime("%d")[1]), str(b_d_qu_var), str(time_current.strftime("%d")), str(b_d_qu_var))
        if  str(time_current.strftime("%m")[1]) == str(b_m_qu_var) or str(time_current.strftime("%m")) == str(b_m_qu_var) and \
            str(time_current.strftime("%d")[1]) == str(b_d_qu_var) or str(time_current.strftime("%d")) == str(b_d_qu_var):
                geb_var = "Alles gute zum Geburststag!"
        else:
            geb_var = "test"
            
        print = str(geb_var)
        sql = ("SELECT massage_id, message, by_col, status, time FROM message WHERE to_col = " + id_var)
        mycursor.execute(sql)
        myresult_2 = mycursor.fetchall()
        mydb.commit()


        beg_var = "hallo", g_g_qu_var, f_n_qu_var, s_n_qu_var, geb_var
        engine.say(beg_var)
        engine.runAndWait()

        i = 0
        n_n = 1
        for x in myresult_2:#Nachrichten überprüfung                           

            sql = ("SELECT firstname, surname FROM users WHERE shortid = " + str(myresult_2[i][2]))
            mycursor.execute(sql)
            myresult_3 = mycursor.fetchall()
            mydb.commit()

            split_var = re.split(':|-| ',str(myresult_2[i][4]))
            print=str(split_var[2]) + str(time_current.strftime("%d"))
            
            if str(split_var[1]) == str(time_current.strftime("%m")) or str(split_var) == str(time_current.strftime("%m")) and \
               str(split_var[2]) == str(time_current.strftime("%d")) or str(split_var) == str(time_current.strftime("%d")):
                        #date_of_mes = "Heute"
                        print("hallo")#(date_of_mes)
                    
            date_of_mes = "ihuzg"#split_var[1] +" "+ split_var[2]
            print(str(date_of_mes))

            if mycursor.rowcount == 1:#user zuordnung
                mes_var = "Nachricht: " + str(date_of_mes) + str(n_n) + "; von " + str(myresult_3[0][1]) + " " + str(myresult_3[0][0]) + " :" + str(myresult_2[i][1])
            else:
                mes_var = "Nachricht: " + str(date_of_mes) + str(n_n) + "; von unbekannt :" + str(myresult_2[i][1])

            #print(mes_var)
            engine.say(mes_var)
            engine.runAndWait()
     
            i += 1
            n_n += 1
    else:        
        engine.say("Nutzer existieer mehrfach, eingabe fehlerhaft")
        engine.runAndWait()
    engine.say("eingeloggt")
    engine.runAndWait()
    
"""       
if __name__ == "__main__":
    evaluating_messages()
    final()
    user_querry()
""" 
