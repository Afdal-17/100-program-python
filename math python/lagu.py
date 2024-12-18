import sys
import time

def lirik_berjalan(teks, kecepatan=0.1):
    for huruf in teks:
        sys.stdout.write(huruf)  
        sys.stdout.flush()  
        time.sleep(kecepatan)  


lirik = """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
"""


print("Lirik Berjalan:\n")
lirik_berjalan(lirik, kecepatan=0.05)  
