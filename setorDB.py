import mysql.connector
import json

#######################################
### Fungsi untuk kirim ke database 
#######################################

### Gerbang Masuk ###
def MQTT_Topic_GerbangMasuk(jsonData):
    json_Dict = json.loads(jsonData)
    username = json_Dict['data_Masuk'] 
        
    #Koneksi dan kirim data ke Database
    connection = mysql.connector.connect(host='localhost',
                             database='coba_login',
                             user='david',
                             password='admin')                 
    mycursor = connection.cursor()

    sql = "INSERT into gerbangMasuk (username) values ('%s')" % username
    
    mycursor.execute(sql)
    connection.commit()
    return

    print "Input anda masuk pada database"
    print ""


### Gerbang Keluar ###
def MQTT_Topic_GerbangKeluar(jsonData):
    json_Dict = json.loads(jsonData)
    username = json_Dict['data_Keluar']

    #Koneksi dan kirim data ke Database
    connection = mysql.connector.connect(host='localhost',
                             database='coba_login',
                             user='',
                             password='')                           
    mycursor = connection.cursor(True)

    sql = "INSERT into gerbangKeluar (username) values ('%s')" % username

    mycursor.execute(sql)
    connection.commit()
    # return

    print "Input anda masuk pada database"

    sql_up = "UPDATE users set saldo = saldo - 5000 where users.username='%s' " % username
    mycursor.execute(sql_up)
    connection.commit()
    # return

    print "Input anda masuk pada database - Saldo berkurang"
    print ""


def setor_Data(Topic, jsonData):
    if Topic == "parkir/pintuMasuk":
        #Parkir_GerbangMasuk(jsonData)
        MQTT_Topic_GerbangMasuk(jsonData)
    elif Topic == "parkir/pintuKeluar":
        #Parkir_GerbangKeluar(jsonData)
        MQTT_Topic_GerbangKeluar(jsonData)

