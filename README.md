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
