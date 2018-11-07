import mysql.connector
import json



### Fungsi untuk kirim ke database ###

### Gerbang Masuk ###
def MQTT_Topic_GerbangMasuk(jsonData):
    json_Dict = json.loads(jsonData)
    dataMasuk = json_Dict['data_Masuk'] 
        
    # Koneksi dan kirim data ke Database
    connection = mysql.connector.connect(host='192.168.xxx.xxx',
                             database='ooo',
                             user='xxx',
                             password='xxx')                 
    mycursor = connection.cursor()

    sql = "INSERT into gerbangMasuk (dataMasuk) values ('%s')" % dataMasuk
    
    mycursor.execute(sql)
    connection.commit()
    return

    print "Input anda masuk pada database"
    print ""


### Gerbang Keluar ###
def MQTT_Topic_GerbangKeluar(jsonData):
    json_Dict = json.loads(jsonData)
    dataKeluar = json_Dict['data_Keluar']

    # Koneksi dan kirim data ke Database
    connection = mysql.connector.connect(host='192.168.xxx.xxx',
                             database='ooo',
                             user='xxx',
                             password='xxx')                           
    mycursor = connection.cursor()

    sql = "INSERT into gerbangKeluar (dataKeluar) values ('%s')" % dataKeluar

    mycursor.execute(sql)
    connection.commit()
    return

    print "Input anda masuk pada database"
    print ""


def setor_Data(Topic, jsonData):
    if Topic == "parkir/pintuMasuk":
        # Parkir_GerbangMasuk(jsonData)
        MQTT_Topic_GerbangMasuk(jsonData)
    elif Topic == "parkir/pintuKeluar":
        # Parkir_GerbangKeluar(jsonData)
        MQTT_Topic_GerbangKeluar(jsonData)
