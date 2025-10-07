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


6. feedback untuk asdos -> sudah baik menjalankan tugasnya, terimakasih

7. saya sudah mengunggah hasil screenshot dengan membuat foldernya.

TUGAS 4
1. 
-> AuthenticationForm adalah formulir login bawaan dari django yang digunakan untuk mengelola proses login
kelebihan : 
    - tidak perlu membuat form login dari nol
    - mudah digunakan
    - terintegrasi dengan sistem auth django 
    - aman secara default

kekurangan : 
    - kurang fleksibel di tampilan default 
    - terbatas untuk username/password standar
    - tidak ada fitur tambahan seperti captcha atau OTP

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
-> autentikasi berfokus pada verifikasi identitas pengguna seperti contoh menyocokkan antar username dengan password pengguna sedangkan otorisasi menentukan apa yang boleh dilakukan oleh pengguna teratutentikasi. 

Bagaimana django mengimplementasikan kedua konsep tersebut?
-> autentikasi melalui django.contrib.auth dengan fungsi sperti login, dan logout. kalau otorisasi bisa menggunakan @login_required yang berfungsi hak yang bisa diakses user yang login.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
-> 
SESSION
Kelebihan session : 
    - lebih aman
    - bisa menyimpan data lebih besar dan kompleks daripda cookies
    - kontrol ada di server sehingga user tidak mudah untuk memanipulasi

Kekurangan session
    - beban dan konsumsi sumber daya server
    - manajemen lebih kompleks 
    - resiko kegagalan server

COOKIES
kelebihan cookies : 
    - fleksibel dan mudah diimplementasikan
    - mengurangi beban server karena data langsung disimpan di browser user
    - bisa untuk preferensi pengguna

kekurangn cookies :
    - kapasitas terbatas
    - kerentanan keamanan
    - dikirim pada tiap permintaan HTTP sehingga meningkatkan lalu lintas jaringan

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
-> tidak sepenuhnya aman
contoh : 
    - serangan Cross-site Scripting, penyerang bisa menyerang lewat cookie pengguna
    - cookie manipulation
    - insecure transport

Bagaimnana django menanganinya?
-> memastikan kode hanya dikirim lewat https, tidak lewat http biasa, mencegas XSS dengan membatasi akses cookie hanya oleh server, mengurangi risiko csrf dengan membatasi pengiriman cookie lints domain, dan django punya SignedCookieSession yang menandatangani cookie, sehingga user tidak bisa memanipulasi isinya tanpa terdeteksi.

5. 
    1. saya membuat fungsi registrasi pada views.py dan menambahkan import from django.contrib import messages. saya juga membuat register.html lalu import register pada urls.py dan tambahkan path url ke dalam url patterns untuk akses fungsi yang sudah diimpor tadi

    2. saya membuat fungsi login dengan menambahkan import from django.contrib.auth.forms import UserCreationForm, AuthenticationForm from django.contrib.auth import authenticate, login di views.py dan membuat fungsi login user untuk autentikasi pemngguna yang ingin login. saya juga membuat login.html lalu import login pada urls.py dan tambahkan path url ke dalam url patterns untuk akses fungsi yang sudah diimpor tadi

    3. saya membuat fungsi logout dengan memnambahkan import from django.contrib.auth import logout pada views.py dan menambahkan fungsi logout yang berguna mengarahkan pengguna ke halaman login dalam aplikasi Django. pada main.html saya membuat tombol logout ketika diklik akan menjalankan URL main:logout. lalu import from main.views import logout_user pada urls.py dan tambahkan path url ke dalam url patterns untuk akses fungsi yang sudah diimpor tadi

    4. mengaplikasikan decorator login_required untuk fungsi show_main dan show_product sehingga halaman utama dan product detail hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

    5. saya juga memperbarui kode login_user untuk menyimpan cookie yang bernama last_login. perbarui fungsi logout juga untuk mennghapus cookie last_login setelah melakukan logout. dan tambahkan informasi sesi terakhir login pada main.html

    6. saya juga menghubungkan product dengan user. setiap product akan terasosiasi dengan user

TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut
->  - !important selalu menang (kecuali ada !important lain dengan specificity lebih tinggi).
    - Inline style (style="") lebih tinggi dari CSS di file.
    - Specificity dihitung:
        ID = 100 poin
        Class/attribute/pseudo-class = 10 poin
        Elemen/pseudo-element = 1 poin 
    - Kalau specificity sama, aturan yang ditulis terakhir yang dipakai.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
-> Responsive design penting karena orang mengakses web dari berbagai perangkat dengan ukuran layar berbeda. Tanpa desain ini, tampilan bisa berantakan dan sulit digunakan. Contoh yang sudah responsif adalah YouTube, yang menyesuaikan layout di HP maupun laptop sehingga tetap nyaman. Sebaliknya, beberapa web forum lama tidak responsif, jadi kalau dibuka di HP harus zoom dan geser-geser. Jadi, responsive design memastikan web enak dipakai di semua perangkat.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!  
    - Margin: ruang di luar elemen. Jadi fungsinya untuk ngasih jarak antara elemen satu dengan elemen lain.
    - Border: garis yang ada di pinggir elemen, membungkus konten dan padding.
    - Padding: ruang di dalam elemen, antara konten (misalnya teks) dengan border.

Dalam CSS, ketiganya bisa diatur dengan properti margin, border, dan padding. Misalnya, jika kita menuliskan margin: 20px; border: 2px solid black; padding: 15px;, maka kotak akan memiliki jarak 20 piksel dari elemen lain, garis tepi hitam setebal 2 piksel, dan ruang kosong 15 piksel di dalam kotak sebelum kontennya.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
->
    - Flexbox adalah sistem layout CSS untuk mengatur elemen dalam satu arah (horizontal atau vertikal). Cocok dipakai untuk      membuat barisan menu, tombol, atau card yang fleksibel dan rapi.
    - Grid Layout adalah sistem dua dimensi yang membagi halaman menjadi baris dan kolom, ideal untuk layout kompleks seperti     halaman dengan header, sidebar, dan konten utama.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    1. saya memilih menggunakan tailwind ke aplikasi. Tailwind CSS memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek
    2. saya juga menambahkan fitur edit product untuk mengedit product dengan membuat berkas html baru yaitu edit_product.html dan import di urls.py dan tambahkan path url. lalu perbarui tombol edit di loop product_list pada main.html
    3. saya juga menambahkan fitur delete product untuk menghapus product dan import di urls.py dan tambahkan path url. lalu perbarui tombol delete di loop product_list pada main.html
    4. lalu saya menambahkan navigation bar 
    5. konfigurasi static files 
    6. Styling pada Aplikasi dengan Tailwind dan External CSS dengan menambahkan global.css di /static/css lalu hubungkan global.css dan script Tailwind ke base.html
    7. lalu styling navbar sekreatif mungkin
    8. lalu styling halaman login, register, dll.
    9. kita buat no-product.png ke direktori static/image. ambil suatu gambar agar jika user belom ada product dan ke my product akan memunculkan gambar belom ada product
    10. saya juga styling halaman product_detail, create_product, dan edit product.

TUGAS 6
1. Perbedaan antara synchronous request dan asynchronous request
-> Synchronous request membuat browser menunggu respons dari server sebelum melanjutkan aktivitas lain, sehingga halaman akan berhenti sementara. Sebaliknya, asynchronous request memungkinkan browser tetap aktif karena proses permintaan dan respons berjalan di latar belakang tanpa menghentikan interaksi pengguna.

2. Cara kerja AJAX di Django (alur request–response)
-> AJAX di Django bekerja dengan cara JavaScript mengirim permintaan ke server tanpa bikin halaman ke-refresh. Server Django lalu memproses data itu dan kirim balik hasilnya dalam bentuk JSON. Setelah itu, JavaScript langsung menampilkan hasilnya di halaman, jadi kelihatan seperti datanya muncul otomatis.

3. Keuntungan menggunakan AJAX dibandingkan render biasa di Django
-> Dengan AJAX, website jadi lebih cepat dan tidak perlu bolak-balik reload halaman. Jadi kalau menambah produk atau update data, hasilnya langsung muncul tanpa nunggu lama. Hal ini membuat pengguna merasa website lebih ringan dan enak dipakai.

4. Cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django
-> Untuk menjaga keamanan, Django menggunakan token CSRF (Cross-Site Request Forgery) yang wajib disertakan pada setiap permintaan POST. token ini memastikan bahwa permintaan benar-benar berasal dari situs yang sah dan bukan dari pihak luar yang berbahaya.

5. Dampak AJAX terhadap pengalaman pengguna (User Experience)
-> AJAX membuat pengalaman pengguna lebih baik, karena interaksi menjadi cepat dan real-time. pengguna dapat melihat perubahan atau pembaruan data langsung tanpa harus menunggu pemuatan ulang seluruh halaman, sehingga website terasa lebih modern dan interaktif.