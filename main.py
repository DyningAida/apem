import apem 
npm=input("Masukkan NPM ")
paswd=input("Masukkan password akun SIAP anda ")
speech = apem.Apem(npm, paswd)

speech.speak()