from PIL import Image
import img2pdf
import os
from pypdf import PdfWriter, PdfReader
import re

def _create_pdf_from_image(image_path: str, pdf_path: str = "") -> str:
    if not pdf_path:
        pdf_path = os.path.splitext(image_path)[0] + ".pdf"

    # Ouverture de l'image
    with Image.open(image_path) as image:
        # Conversion en chunks avec img2pdf
        pdf_bytes = img2pdf.convert(image.filename)

    # Écriture des fichiers PDF avec les chunks
    with open(pdf_path, "wb") as file:
        file.write(pdf_bytes)

    return pdf_path

def _create_one_pdf_for_each_image_from_folder(folder_path: str) -> list[str]:
    print(folder_path + "> create one pdf for each image from folder")
    pdfs_path = []

    file_paths = os.listdir(folder_path)
    file_paths.sort(key=_natural_keys)

    # Créer un fichier PDF pour chaque image
    for file_path in file_paths:
        file_path = os.path.join(folder_path, file_path)
        if _is_image(file_path):
            pdf_path = _create_pdf_from_image(file_path)
            pdfs_path.append(pdf_path)

    print("<" + folder_path)
    return pdfs_path

def _create_pdf_from_pdfs(folder_path: str, pdf_writer_path: str = "output.pdf") -> str:
    print(folder_path + "> create pdf from pdfs")
    pdf_writer = PdfWriter()

    # sort file by number
    file_paths = os.listdir(folder_path)
    file_paths.sort(key=_natural_keys)

    for file_path in file_paths:
        file_path = os.path.join(folder_path, file_path)
        if file_path.endswith(".pdf"):
            with open(file_path, "rb") as file:
                pdf = PdfReader(file)
                for i in range (0, pdf.get_num_pages()):
                    pdf_writer.add_page(pdf.get_page(i))

    with open(pdf_writer_path, "wb") as output:
        pdf_writer.write(output)
        response = output.name

    print("<" + folder_path)
    return response

def _delete_pdfs(pdfs: list[str]):
    for pdf in pdfs:
        os.remove(pdf)  

def _is_image(file_path: str):
    image_extensions = (
        ".apng",
        ".avif",
        ".gif",
        ".jpg",
        ".jpeg",
        ".jfif", 
        ".pjpeg",
        ".pjp",
        ".png",
        ".svg",
        ".webp",
        ".bmp",
        ".ico",
        ".cur",
        ".tif",
        ".tiff"
    )

    # Extraire l'extension du fichier
    file_extension = os.path.splitext(file_path)[1].lower()
    
    # Vérifier si l'extension du fichier est dans la liste des extensions d'image acceptées
    return file_extension in image_extensions

def _natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    def atoi(text):
        return int(text) if text.isdigit() else text

    return [ atoi(c) for c in re.split(r'(\d+)', text) ]



def create_pdf_from_imgs(folder_path_of_imgs: str, pdf_path: str):
    print("Begining creation of PDFs from images in folder:", folder_path_of_imgs)
    pdfs_path = _create_one_pdf_for_each_image_from_folder(folder_path_of_imgs)

    _create_pdf_from_pdfs(folder_path_of_imgs, pdf_path)

    _delete_pdfs(pdfs_path)
    print("PDFs creation from images in folder", folder_path_of_imgs, "done!")
