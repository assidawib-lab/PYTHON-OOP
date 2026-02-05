print("Hello World!")
# cara membuat fungsi
# struktur: 'def namaFungsi(parameternya'
def hello(name):
    print(f"Hello Bli, {name}")
# panggil di bawh, ga boleh nyatu dengan def
hello("ujang")
hello("made")
hello("Nyoman")
hello("Komang")

# minta 2 parameter penilaian
def nilai(name, uts, uas):
    rumus = uts + uas
    print(f"nilai akhir adalah {name}: {rumus}")
          
nilai("Bayu", 80, 90)
nilai("asep", 70, 80)
nilai("Ujang", 75, 85)