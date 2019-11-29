import apem 
npm=input("Masukkan NPM ")
paswd=input("Masukkan password akun SIAP anda ") #issue 37
speech = apem.Apem(npm, paswd)

speech.speak()