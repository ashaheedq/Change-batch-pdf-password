import pikepdf
import os

file_name = os.listdir()
print(file_name)
password = "GD@3i$@44T!"
correct_password = "GDaEis@44t!"

for file in file_name:
    pdf = pikepdf.open(file, password=password)
    pdf.save("NEW"+file, encryption=pikepdf.Encryption(owner=correct_password, user=correct_password, R=6))
    pdf.close