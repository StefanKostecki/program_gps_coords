import os
import csv
from exif import Image
import glob
os.chdir('C:\\foto')
with open('C:\\dane_csv\\dane_gps.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=' ')
    writer.writerow(['latitude', 'longitude'])


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "W" or ref == "S":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


file_extension = glob.glob('*.JPG')

foto = os.listdir()
for i in range(len(foto)):
    with open('C:\\foto\\' + foto[i], 'rb') as image_file:
        if foto[i] in file_extension:
            try:
                img = Image(image_file)
                dc1 = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
                dc2 = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
                with open('C:\\dane_csv\\dane_gps.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=' ')
                    writer.writerow([dc1, dc2])
            except AttributeError:
                print('File has no coordinates: ' + foto[i])
        else:
            print('File has wrong extension: ' + foto[i])
print('Finish')
