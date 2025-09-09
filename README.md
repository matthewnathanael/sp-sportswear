"# sp-sportswear" 

Dalam pembuatan project ini, saya memulai dari membuat project Django terlebih dahulu. Hal ini sudah pernah diterapakan sebelumnya saat melakukan tutorial, diawali dengan melakukan instalasi git dan membuat direktori baru yang nantinya akan kita gunakan untuk menambahkan project kita ke dalam github. Setelah menambahkan project tersebut ke dalam direktori yang sudah kita hubungkan dengan github menggunakan git remote add (link git), saya melakukan commit dan push agar project tersebut dapat ditambahkan ke Github. Setelah berhasil dihubungkan, saya lanjut melakukan instalasi django, dengan membuat requirements seperti yang disarankan pada tutorial 0, isi requirements tersebut berisi hal-hal yang diperlukan untuk melakukan instalasi django. Untuk instalasinya sendiri tidak terlalu rumit dan hanya memerlukan waktu sementara. Setelah itu, jalankan django-admin startproject (namaFilenya) . untuk membuat project django.


Setelah melakukan instalasi django, saya membuat file .env. 
env berupa environment variables yang disimpan di luar kode program, dan ini digunakan untuk menyimpan informasi konfigurasi seperti crendetial database, API Keys, atau pengaturan environment. Hal ini dapat memungkinkan kode yang sama dapat berjalan di environment berbeda tanpa perlu mengubah kode kita. (disini kita juga buat .env.prod dengan production = true, aplikasi akan menggunakan database PostGre SQL) 
disini, tidak boleh lupa untuk mengubah settings.py agar bisa load env dari .env filenya.


Step ke-3 yang saya lakukan setelah berhasil menambahkan project ke dalam git dan set-up selesai, saya hubungkan dengan PWS dengan tata-cara yang sebelumnya diberikan pada tutorial 0 (menambahkan ALLOWED_HOST). Tujuan ini adalah agar kita bisa menggunakan PWS tersebut sebagai host (kita dapat view project kita). 

Setelah saya selesai melakukan set-up baik itu menghubungkan dengan PWS dan Github. Saya baru mulai membuat aplikasi dengan nama main pada proyek saya dengan nama toko SP Sportswear. Tentunya disini kita ingin membuat aplikasi berbeda dengan football-news yang sebelumnya pernah dibuat pada tutorial 1. Karena aplikasi ini berupa aplikasi mengenai sportswear/bola, kita akan mengubah model-model (mengubah nama class menjadi product karena akan menjual barang dan bukan berita) sebelumnya yang berhubungan dengan football news menjadi pakaian-pakaian olahraga yang dapat diinginkan pengguna. Sebelum mengubah model, saya mengaktifkan env terlebih dahulu agar dapat memungkinkan kode yang sama dapat berjalan di env berbeda. Model-model yang saya gunakan disini ada,  jersey, sweater, baju, celana, sepatu, tas, sleeve, kaos kaki, lainnya(apabila tidak ada kategori). Lalu, saya menambahkan nama sebagai nama item, harga/price sebagai harga item, description untuk deskripsi item, thumbnail untuk gambar item, kategori untuk membagi-bagi kategori item, terakhir is_featured untuk menampilkan barang-barang unggulan sportswear yang ada.


Ada beberapa alasan untuk penggunaan tipe data tertentu, misalnya:
nama, category => CharField => tipe data yang ideal untuk menyimpan teks pendek
deskripsi => TextField => tipe data yang ideal untuk menyimpan teks panjang
price => IntegerField => tipe data yang ideal untuk menyimpan angka (bulat)
thumbnail => URLField => tipe data khusus untuk menyimpan url, disini untuk gambar.
is_featured => BooleanField => tipe data yang paling efisien untuk mewakili kondisi biner

Setelah selesai membuat model, saya lanjut membuat HTML template yaitu main.html. Halaman ini berisi konten dasar untuk Tugas 1, termasuk teks "Main" serta nama dan kelas saya. Tujuannya adalah untuk menampilkan halaman ini melalui routing.
Untuk melakukan routing, saya menggunakan file urls.py dan views.py. Di sini, urls.py bertugas menentukan jalur URL, sementara views.py bertanggung jawab untuk memproses permintaan dan mengirimkan respons.

Sebagai contoh, di views.py, saya mendefinisikan sebuah fungsi yang akan merender main.html. Dalam fungsi tersebut, saya melewatkan data dinamis, seperti nama saya, ke dalam template. Teks "{{ name }}" yang ada di main.html kemudian akan diganti secara otomatis menjadi nama saya, yaitu "Matthew Nathanael", saat halaman dirender. Perubahan ini tidak akan terlihat jika main.html dibuka langsung, karena proses penggantian data tersebut hanya terjadi saat halaman diakses melalui routing yang diatur oleh urls.py dan views.py di dalam proyek. Tentunya hal tersebut hanya bisa dilakukan apabila konfigurasi routing url sudah dilakukan (mengubah urls.py pada direktori main dan url.py pada direktori sp-sportswear dan disambungkan pada main.urls)

Setelah proses routing sudah selesai, saya melakukan deployment pada PWS yang sebelumnya sudah saya hubungkan, project tersebut akan saya tambahkan dengan menggunakan
git add . 
git commit -m "Second Commit: Tugas 2 Individu - Finishing" (jika sudah tidak ada perubahan)
git push origin master
git push pws master 
Dengan melakukan step-step berikut, saya sudah berhasil membuat aplikasi main.


# Bagan request client ke web aplikasi berbasis Django
![alt text](image.png) reference: https://www.biznetgio.com/news/django
Pada bagan tersebut kita dapat melihat alur dari request client ke web,
di mana client disini akan melakukan request atau membuat permintaan yang nantinya akan diterima oleh URL, yang kemudian akan diarahkan ke views yang sesuai. Lalu, views akan berinteraksi dengan model untuk mengelola data di database, dan memilih template untuk menghasilkan halaman web yang dikirimkan kembali sebagai respons ke client.
Untuk fungsi dari masing-masing komponen:
Client -> sebagai pengguna (yang melakukan request ke server web)
URL -> melakukan checking yang diminta ke fungsi yang tepat didalam views (url akan mencari kecocokkan)
Views -> berinteraksi dengan model(mengambil data dari database) dan memilih template yang digunakan untuk menampilkan respons kepada clientnya
Model  -> struktur data aplikasinya, biasa mewakili tabel (digunakan untuk membaca/menulis oleh views)
Template -> file html, disini contohnya seperti main.html yang dibuat, berisi markup statis, dapat menampilkan data dinamis yang dikirimkan oleh Views (seperti yang ada pada main.html {{ class }} )


# Fungsi settings.py pada projek django
Selama proses pembuatan aplikasi tersebut, settings.py berperan penting dalam konfigurasi proyek Django. Dengan memodifikasi settings.py kita dapat menambahkan allowed_host, menggunakan env, mendefinisi detail ke database, dapat mencantumkan semua aplikasi (digunakan django untuk mengetahui model, template) jadi untuk mengubah perilaku proyek django memang perlu melakukan modifikasi pada settings.py

# Cara kerja migrasi database di Django
Migrasi database di Django adalah cara untuk memperbarui skema database agar sesuai dengan perubahan pada model Django. Proses ini terdiri dari membuat migrasi dan menerapkan migrasi

manage.py makemigrations -> memindahkan models.py, membuat file migration baru di directory migration -> gunanya agar dapat mengetahui perubahan pada model (belum diapply ke database)
manage.py migrate ->  django akan membaca file dan eksekusi SQL (membuat kolom baru pada table), mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data

# Kelebihan Framework Django
Django sering direkomendasikan sebagai framework permulaan untuk pengembangan, terutama untuk orang-orang yang ingin fokus ke web-developing.
Django menyediakan semua yang developer butuhkan untuk membangun suatu aplikasi web. Ketika menggunakan framework Django, tidak memerlukan untuk download-download atau install banyak hal untuk fungsi dasar, sangat mudah untuk digunakan. Django sudah memiliki fitur-fitur bawaan yang membuat pengguna/pengembang web tidak perlu kesusahan menginstall dari tempat lain. Selain itu, dari segi security/keamanan, Django sudah memiliki keamanan yang sangat kuat berbeda dengan PHP, secara bawaan framework ini sudah bisa melindungi dari beberapa serangan umum sperti SQLi, XSS dan lain-lain.
Selain itu, Django juga menerapkan pola desain MTV, yang dimana sangat mirip dengan MVC, struktur ini memisahkan logika aplikasi dengan rapi. Tentunya hal ini akan sangat baik bagi pemula agar bisa membangun kebiasaaan koding yang baik (separation of concerns)

# Feedback 
Untuk tutorial 1, menurut saya sudah lumayan cukup mudah untuk di mengerti, karena secara online mungkin beberapa masih ada yang kesusahan, tetapi sudah sangat membantu dengan penjelasan-penjelasan yang diberikan.
 