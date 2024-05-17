import fusion
import os

manga_folder = "/Users/aymnms/Documents/Mangas/Boruto Two Blue Vortex/"


list_chapitre = os.listdir(manga_folder)
list_chapitre.sort(key=fusion._natural_keys)

for element in list_chapitre:
    chapiter_folder = os.path.abspath(os.path.join(manga_folder, element))
    if os.path.isdir(chapiter_folder):
        print(element)
        pdf_path = os.path.abspath(os.path.join(manga_folder, element + ".pdf"))
        fusion.create_pdf_from_imgs(chapiter_folder, pdf_path)

