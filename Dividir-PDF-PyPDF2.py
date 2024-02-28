import PyPDF2

# Caminho do arquivo PDF de entrada
input_pdf_path = r'C:\Users\PC-CM-BONSUCESSO\Pictures\ControlCenter4\Scan\pdf.pdf'

# Caminho do diretório de saída
output_dir = r'C:\Users\PC-CM-BONSUCESSO\Pictures\ControlCenter4\Scan\onde-esta-salvo'

# Abra o arquivo PDF
with open(input_pdf_path, 'rb') as file:
    # Crie um objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Obtenha o número total de páginas
    num_pages = len(pdf_reader.pages)
    
    # Itere sobre cada página e crie um arquivo PDF separado para cada uma
    for i in range(num_pages):
        # Crie um objeto PDFWriter
        pdf_writer = PyPDF2.PdfWriter()
        
        # Adicione a página atual ao objeto PDFWriter
        pdf_writer.add_page(pdf_reader.pages[i])
        
        # Salve o arquivo PDF com o nome "pagina_X.pdf", onde X é o número da página
        output_file_path = f'{output_dir}\\pagina_{i+1}.pdf'
        with open(output_file_path, 'wb') as output_file:
            pdf_writer.write(output_file)
