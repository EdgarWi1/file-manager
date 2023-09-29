# FILE-MANAGER

> Ini adalah repository **Kelompok X** mata kuliah Projek Perangkat Lunak B

## Persiapan
Perlu *di-ingat* untuk menginstall **python** dan **npm** terlebih dahulu. Kalau sudah, install **yarn** melalui **npm**:
```bash
npm install --global yarn
```

## Berkolaborasi
#### I. Cloning
1. Clone repository ini ke dalam laptop/komputer kalian.
2. Buka Folder repository ini melalui sebuah IDE (seperti: Visual Studio Code).

#### II. Instalasi Flask
1. Buka terminal dan masuk ke *directory* projek atau bisa melalui visual studio code dengan Ctrl + ~
2. Masukkan perintah berikut kedalam terminal:
```bash
py -3 -m venv .venv
```
3. Aktivasi Environment python kalian dengan perintah berikut:
```bash
.venv\Scripts\activate
```
4. Install Flask:
```bash
pip install flask
```
#### III. Debugging
Projek ini menggunakan *python* dan *node_modules*. Oleh karena itu kita perlu menjalankan 2 script sekaligus karena perbedaan *dependency* aplikasinya.
1. Buka 2 terminal sekaligus (Visual Studio Code: Tanda '**+**' pada samping kanan terminal).
2. Pada terminal pertama, eksekusi perintah berikut:
```
yarn
```
2. Pada terminal kedua, jalankan **app.py**:
```bash
python app.py
```
atau:
```bash
flask run
```
3. Setelah flask berjalan, nyalakan **tailwind** dengan perintah berikut:
```bash
yarn tailwind
```

## Ekstensi yang Mungkin Anda Perlukan (VSC)
- Python Extension Pack
- Tailwind CSS Intellisense

## Desain Figma
- [Projek File Manager](https://www.figma.com/file/Dkeym0AqX9NakMaCsahaD4/P.-Perangkat-Lunak?type=design&node-id=21-137&mode=design&t=Vkkap0czwjOdn9VD-0)
