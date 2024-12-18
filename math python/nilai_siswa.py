import os
os.system ("cls")

mtk = 76
ipa = 80
ips = 21
pab = 95
nilai = mtk+ipa+ips+pab
rn = nilai/4
print(rn)

if rn<=100 and rn>=90:
    print("Grade A")

elif rn<=90 and rn>=80:
    print("Grade B")

elif rn<=80 and rn>=70:
    print("Grade C")

elif rn<=70 and rn>=60:
    print("Grade E")