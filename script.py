import pikepdf
import os

file_name = os.listdir()
print(file_name)
old_password = "GD@3i$@44T!"
new_password = "GDaEis@44t!"

for file in file_name:
    pdf = pikepdf.open(file, password=old_password)
    pdf.save("NEW"+file, encryption=pikepdf.Encryption(owner=new_password, user=new_password, R=6))
    pdf.close
