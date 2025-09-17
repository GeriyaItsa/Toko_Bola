TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step ->
buat repositori di github
buat folder dan aktifkan virtual environment
buat virtual environment dan install django
buat projek django baru
buat file requirements.txt yang berisi dependencies -> file requirements.txt berisi daftar paket yang dipakai proyek python. fungsinya agar mudah untuk install semua kebutuhan cukup dengan satu perintah, jadi orang lain atau server bisa langsung jalankan projek tanpa ribet.
lalu konfigurasi environmetn variables dan proyek -> untuk menyimpan pengaturan penting aplikasi, seperti nama database, password, api key, atau mode produksi/development, di luar kode program. dengan begitu, kode bisa tetap sama tapi jalan di lingkungan berbeda tanpa harus diubah-ubah. selain itu lebih aman karena data sensitif tidak ditulis langsung di dalam kode.
buat file .env.prod untuk production deployment isi data data sesuai yang sudah di kirim di gmail ui
buat .gitignore juga berkas berkas yang harus diabaikan oleh git agar tidak perlu dilacak dan tidak dipush ke repositori github
selanjutnya, create new project pada pws dan pergi ke raw editor dan isi sesuai dengan file .env.prod yg sudah dibuat
setelah itu tambah allowed host dengan url deployment pws
lalu buat aplikasi main dan ke installed apss
dan buat folder templates yang di dalammnya berisi berkas main.html yg berguna untuk template dan website nantinya
setelah itu membuat model produk di models.py dan jalankan migrasi
setelah itu hubungkan view dengan template
modifikasi template sesuai tugas yg diminta
lalu routing sambungkan proyjek ke aplikasi main
jika semuanya sudah, push kode ke git dan juga pws

2. <img width="568" height="449" alt="image" src="https://github.com/user-attachments/assets/18aa60d6-4342-4a3e-b740-8adc9e70628a" />

3. fungsi settings.py adalah mengatur informasi dasar proyek, mengatur aplikasi yang digunakan, mengatur template, mengatur allowed host, basis data dan lainnya.

4. cara kerja migrasi data di django -> migrasi di dfjango itu cara untuk bikin database selalu sama dengan model yang kita buat di kode. kalau nambah atau ubah model, kita jalankan makemigrations untuk bikin rencana perubahan, lalu migrate untuk benar-benar mengubah database. django menyatat semua migrasi biar tidak double.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
-> karena framework ini lengkap, terstruktur, dan pakai python yang mudah dipahami. dengan django, kita bisa belajar konsep dasar pengembangan software seperti database, autentikasi, dan arsitektur aplikasi tanpa harus bikin semuanya dari nol.

5. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
-> aman terkendali

TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
-> Agar data bisa diakses oleh pengguna atau sistem lain, memastikan pertukaran data yang konsisten, mendukung integrasi antar sistem, efisiensi dan kecepatan, dan keamanan data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
-> JSON lebih hemat bandwidth karena tidak perlu menulis banyak tag seperti XML, mudah dibaca, integrasi lebih cepat untuk API modern, dan native di java. jadi menurut saya lebih baik JSON karena lebih ringkas, mudah, dan cepat.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
-> di django, method is_valid() digunakan untuk mengecek apakah data dari form sudah sesuai aturan validasi. saat form dikirim, datanya ditampung dalam objek form, lalu form.is_valid() akan memeriksa apakah tiap field terisi dengan benar (misalnya tipe data atau panjang teks), menjalankan validasi tambahan, dan mengembalikan True jika valid atau False jika ada kesalahan. method ini penting karena hanya data yang valid yang aman diproses lebih lanjut, seperti disimpan ke database atau dikirim ke layanan lain. jika tidak ada, maka data yang salah format atau kosong bisa masuk dan menimbulkan bug maupun masalah keamanan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
-> csrf_token adalah pelindung dari serangan CSRF (Cross-Site Request Forgery). token ini berupa kode acak yang unik untuk setiap pengguna dan disisipkan ke dalam form yang mengirim data dengan metode POST. saat form dikirim, server akan mengecek apakah tokennya cocok dengan yang sudah diberikan. kalau tidak cocok, request ditolak. kalau tidak ada csrf_token, server tidak bisa membedakan mana permintaan asli dari pengguna dan mana yang dibuat oleh orang jahat. penyerang bisa bikin website palsu yang diam-diam mengirim permintaan ke server menggunakan akun kita yang sedang login. akibatnya bisa terjadi aksi berbahaya tanpa disadari. jadi, csrf_token penting untuk menjaga keamanan data dan mencegah serangan.

5. 
 - membuat direktori templates yang berisi base.html lalu ditambah / saya sesuaikan ke setting.py
 - lalu saya membuat forms.py pada direktori main. lalu isi field sesuai dengan models.
 - lalu saya menambahkan fungsi di views.py untuk melihat objek dalam format xml, json, xml by id, dan json by id serta untuk menambahkan dan menampilkan product
 - lalu pada bagian urls.py import fungsi-fungsi yang sudah dibuat kemudian ditambah ke path URL dalam variabel urlpatterns.
 - dalam main.html update kode di dalam blok content untuk menampilkan data product serta tombol "Add Product"
 - tambah dua berkas dalam direktori main/templates untuk halaman form input dan detail berita. yaitu create_product.html dan product_detail.html
 - setelah itu di settings.py saya tambahkan entri url proyek pws pada CSRF_TRUSTED_ORIGINS


6. feedback untuk asdos -> sudah baik menjalankan tugasnya, terimakasih.

7. saya sudah mengunggah hasil screenshot dengan membuat foldernya.