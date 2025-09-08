"# sp-sportswear" 

Dalam pembuatan project ini, saya memulai dari membuat project Django terlebih dahulu. Hal ini sudah pernah diterapakan sebelumnya saat melakukan tutorial, diawali dengan melakukan instalasi git dan membuat direktori baru yang nantinya akan kita gunakan untuk menambahkan project kita ke dalam github. Setelah menambahkan project tersebut ke dalam direktori yang sudah kita hubungkan dengan github menggunakan git remote add (link git), saya melakukan commit dan push agar project tersebut dapat ditambahkan ke Github. Setelah berhasil dihubungkan, saya lanjut melakukan instalasi django, dengan membuat requirements seperti yang disarankan pada tutorial 0, isi requirements tersebut berisi hal-hal yang diperlukan untuk melakukan instalasi django. Untuk instalasinya sendiri tidak terlalu rumit dan hanya memerlukan waktu sementara. Setelah itu, jalankan django-admin startproject (namaFilenya) . untuk membuat project django.

Setelah melakukan instalasi django, saya membuat file .env. 
env berupa environment variables yang disimpan di luar kode program, dan ini digunakan untuk menyimpan informasi konfigurasi seperti crendetial database, API Keys, atau pengaturan environment. Hal ini dapat memungkinkan kode yang sama dapat berjalan di environment berbeda tanpa perlu mengubah kode kita. (disini kita juga buat .env.prod dengan production = true, aplikasi akan menggunakan database PostGre SQL) 
disini, tidak boleh lupa untuk mengubah settings.py agar bisa load env dari .env filenya.


Step ke-3 yang saya lakukan setelah berhasil menambahkan project ke dalam git dan set-up selesai, saya hubungkan dengan PWS dengan tata-cara yang sebelumnya diberikan pada tutorial 0 (menambahkan ALLOWED_HOST). Tujuan ini adalah agar kita bisa menggunakan PWS tersebut sebagai host (kita dapat view project kita). 

Setelah saya selesai melakukan set-up baik itu menghubungkan dengan PWS dan Github. Saya baru mulai membuat aplikasi dengan nama main pada proyek saya dengan nama toko SP Sportswear. Tentunya disini kita ingin membuat aplikasi berbeda dengan football-news yang sebelumnya pernah dibuat pada tutorial 1. Karena aplikasi ini berupa aplikasi mengenai sportswear/bola, kita akan mengubah model-model (mengubah nama class menjadi product karena akan menjual barang dan bukan berita) sebelumnya yang berhubungan dengan football news menjadi pakaian-pakaian olahraga yang dapat diinginkan pengguna. Model-model yang saya gunakan disini ada,  jersey, sweater, baju, celana, sepatu, tas, sleeve, kaos kaki, lainnya(apabila tidak ada kategori). Lalu, saya menambahkan nama sebagai nama item, harga/price sebagai harga item, description untuk deskripsi item, thumbnail untuk gambar item, kategori untuk membagi-bagi kategori item, terakhir is_featured untuk menampilkan barang-barang unggulan sportswear yang ada.


Ada beberapa alasan untuk penggunaan tipe data tertentu, misalnya:
nama, category => CharField => tipe data yang ideal untuk menyimpan teks pendek
deskripsi => TextField => tipe data yang ideal untuk menyimpan teks panjang
price => IntegerField => tipe data yang ideal untuk menyimpan angka (bulat)
thumbnail => URLField => tipe data khusus untuk menyimpan url, disini untuk gambar.
is_featured => BooleanField => tipe data yang paling efisien untuk mewakili kondisi biner


Setelah mengubah model-modelnya, saya menambahkan html pada templates, yang nanti akan melakukan routing dengan menggunakan views.py
html tersebut berupa main.html yang berisi "Main" sesuai tugas 1, karena disini yang ingin saya buat adalah aplikasi main, yang dilanjutkan dengan nama saya dan kelas saya, tentunya kedepannya hal ini akan berubah dan bertambah banyak. Main pointnya disini adalah melakukan routing dimana kita dapat menggunakan views.py untuk menampilkan main.html, contohnya disini adalah mengubah nama, yang sebelumnya "Matthew Nathanael" menjadi {{ name }}, disini akan terjadi perubahan tampilan pada website. Walaupun ketika di run pada main.html langsung, perubahan tersebut tidak akan terlihat. Namun, ketika kita jalankan di view project, akan berubah, hal tersebut karena 'routing' yang dilakukan oleh views.py yang berhasil mengubah {{ name }} tersebut menjadi nama saya.



