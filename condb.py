import mysql.connector 
from mysql.connector import Error

# Mengeksekusi query untuk mengelola database 
# Parameter database
nama_host = "localhost" 
user = "root"
password = ""

# Membuat koneksi ke server
myconn = mysql.connector.connect(host = nama_host, user = user, passwd = password)

# membuat object cursor
mycursor = myconn.cursor()

# Membuat query
query_membuat_db = "tugas_perpus"

# Mengeksekusi query
mycursor.execute(query_membuat_db)
# Parameter database
nama_host = "localhost" 
user = "root"
password = ""
db = "tugas_perpus" 

# membuat koneksi ke database
mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)

# membuat object cursor
mycursor = mydb.cursor()

# Membuat query
table_buku = """
create table list_buku(
	id_buku VARCHAR(10) NOT NULL,
	nama_buku VARCHAR(50) NOT NULL,
	kategori VARCHAR(50) NOT NULL,
	stock INT(6) NOT NULL,
	PRIMARY KEY (id_buku)
);
"""
table_user = """
create table list_user(
	id_user VARCHAR(10) NOT NULL,
	nama_user VARCHAR(50) NOT NULL,
	tgl_lahir date NOT NULL,
	pekerjaan VARCHAR(50) NOT NULL,
	alamat VARCHAR(50) NOT NULL,
	PRIMARY KEY (id_user)
);
"""
table_peminjaman = """
create table peminjaman(
	id_user VARCHAR(50) NOT NULL,
	id_buku VARCHAR(10) NOT NULL,
	nama_user VARCHAR(50) NOT NULL,
	tgl_pinjam date NOT NULL,
	tgl_pengembalian date NOT NULL
);
"""
mycursor.execute(table_buku)
mycursor.execute(table_user)
mycursor.execute(table_peminjaman)
mydb.commit()