import apem 
npm=input("Masukkan NPM ")
paswd=input("Masukkan password akun SIAP anda ")
speech = apem.Apem(npm, paswd) #penyelesaian issue 38

speech.speak()