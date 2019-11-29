import apem 
npm=input("Masukkan NPM ")#issue 36
paswd=input("Masukkan password akun SIAP anda ")
speech = apem.Apem(npm, paswd)

speech.speak()