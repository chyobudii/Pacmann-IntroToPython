import mysql.connector
from datetime import date

fine_per_day =5.0  #global variable

def clear():
    for _ in range(1):
        print

def add_book():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    
    clear()

    id_buku = input('Masukan Kode Buku :')
    nama_buku = input('Masukan Nama Buku : ')
    kategori = input('Kategori Buku : ')
    stock  = input('Stock buku : ')
    copies  = int(input('Enter copies : '))
    sql = "insert into list_buku(id_buku, nama_buku, kategori, stock) values(%s,%s,%s,%s)"
    for _ in range(0, copies):
        cursor.execute(sql)
        conn.close()
        print('\n\nBuku telah ditambahkan')
        wait = input('\n\n\n Press any key to continue....')

def liat_buku():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    
    clear()
    
    sql = "select * from list_buku"
    cursor.exceute(sql)
    conn.close()           

def add_name():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    
    clear()

    id_user = input('Masukan Nomor ID : ')
    nama_user = input('Masukan Nama : ')
    tgl_lahir= input('Tanggal Lahir(YYYY-MM-DD) : ')
    pekerjaan = input('Pekerjaan : ')
    alamat = input('Masukan alamat : ')
    sql = "insert into list_user(id_user, nama_user, tgl_lahir, pekerjaan, alamat) values(%s, %s,%s,%s,%s)"
    cursor.execute(sql)
    conn.close()
    print('\n\nUser telah ditambahkan')
    wait = input('\n\n\n Press any key to continue....')

def liat_user():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    
    clear()
    
    sql = "select * from list_user"
    cursor.exceute(sql)
    conn.close()   
    wait = input('\n\n\n Press any key to continue....')

def minjem():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    
    clear()
    
    id_buku = input('Enter ID Buku : ')
    id_user = input('Enter ID User :')
   
    
    result = status_buku(id_buku)
    result1 = status_user(id_user)
    #print(result1)
    today = date.today()
    if len(result1) == 0:
        if result == 'available':
            sql = 'insert into peminjaman(id_buku, id_user, tgl_peminjaman) values('+id_buku+','+id_user+',"'+str(today)+'");'
            sql_book = 'update book set status="issue" where id ='+id_buku+ ';'
            cursor.execute(sql)
            cursor.execute(sql_book)
            print('\n\n\nBuku dipinjam')
        else:
            print('\n\nBook tersedia. status :',result1)
    else:
        if len(result1)<1:
            sql = 'insert into peminjaman(b_id, m_id, doi) values('+id_buku+','+id_user+',"'+str(today)+'");'
            sql_book = 'update book set status="issue" where id ='+id_buku+';'
            cursor.execute(sql)
            cursor.execute(sql_book)
            print('\n\n\nBuku dipinjam')
        else:
            print('\n\nBuku sudah dipinjam')

        conn.close()
        wait = input('\n\n\n Press any key to continue....')

def liat_pinjam():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    
    clear()
    
    sql = "select * from peminjaman"
    cursor.exceute(sql)
    conn.close()   
    wait = input('\n\n\n Press any key to continue....')

def balikin():
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    global fine_per_day
    clear()
    
    id_buku = input('Enter ID Buku : ')
    id_user = input('Enter ID User :')
    today = date.today()
    result = status_buku(id_buku, id_user)
    if result==None:
        print('Buku tersedia')
    else:
        sql='update list_buku set status ="available" where id ='+id_buku+';'
        din = (today - result[3]).days
        fine = din * fine_per_day 
        sql1 = 'update list_buku set tgl_pengembalian ="'+str(today)+'" , fine='+str(fine)+' where id_buku='+id_buku +' and id_user='+id_user+' and tgl_peminjaman is NULL;' 
        
        cursor.execute(sql)
        cursor.execute(sql1)
        print('\n\nBuku telah dikembalikan')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def cari_buku(field):
    conn = mysql.connector.connect(host="localhost", database="tugas_perpus", user="root", password="")
    cursor = conn.cursor()
    clear()
    
    msg ='Enter '+ field +' Value :'
    judul = input(msg)
    sql ='select * from list_buku where '+ field + ' like "%'+ title +'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for : ',field,' :' ,title)
    for record in records:
        print(record)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def main_menu():
    while True:
        clear()
        print(' L I B R A R Y    M E N U')
        print("\n1.  Daftar User Baru")
        print('\n2.  Daftar Buku Baru')
        print('\n3.  Peminjaman')
        print('\n4.  Tampilkan Daftar Buku')
        print('\n5.  Tampilkan Daftar User')
        print('\n6.  Tampilkan Daftar Peminjaman')
        print('\n7.  Cari Buku')
        print('\n8.  Pengembalian')
        print('\n9.  Exit')
        print('\n\n')
        pilihan = int(input('Masukan Nomor Tugas ...: '))
        
        if pilihan == 1:
            add_name()
        if pilihan == 2:
            add_book()
        if pilihan == 3:
            minjem()
        if pilihan == 4:
            liat_buku()
        if pilihan == 5:
            liat_user()
        if pilihan == 6:
            liat_pinjam()
        if pilihan == 7:
            cari_buku()
        if pilihan == 8:
            balikin()
        if pilihan == 9:
            add_member()
            break


if __name__ == "__main__":
    main_menu()
