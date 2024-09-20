import pandas as pd
from modules.db_operations import create_db_session, create_table, url_exists, add_resume
from modules.utils import download_file, extract_text_from_pdf

def update_db(file_path, db_type):
    session, engine = create_db_session(db_type)

    # Criar a tabela se não existir
    create_table(engine)

    # 1.1 Ler a planilha e obter as URLs
    df = pd.read_excel(file_path)
    urls = df["Resume File"].tolist()

    # 1.2 Obter URLs que ainda não estão no banco de dados
    new_urls = [url for url in urls if not url_exists(session, url)]

    if not new_urls:
        print("Nenhuma nova URL encontrada. Finalizando.")
        session.close()
        return  # Finaliza se não houver novas URLs

    # 1.3 Processar cada nova URL
    dest_folder = 'resume_files'

    for url in new_urls:
        print(f"Baixando arquivo: {url}")
        file_path = download_file(url, dest_folder)
        extracted_text = extract_text_from_pdf(file_path)

        # Criar um novo registro no banco de dados
        add_resume(session, extracted_text, url)

    # Salvar as alterações no banco de dados
    session.commit()
    session.close()
    print("Processamento concluído!")

if __name__ == "__main__":
    update_db('planilha_exemplos.xlsx', 'mysql')  # ou 'sqlite'
