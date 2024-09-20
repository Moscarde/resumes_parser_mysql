Este projeto tem como objetivo gerenciar o download e o armazenamento de arquivos de currículos a partir de uma planilha do Excel e fazer o processamento para atualizar um banco de dados. O fluxo de processamento é o seguinte:

1. **Leitura da Planilha**: A função `update_db` lê a planilha `planilha_exemplos.xlsx` e extrai a coluna "Resume File" que contém as URLs dos arquivos.
    
2. **Verificação de URLs**: O projeto verifica quais URLs já estão armazenadas no banco de dados. URLs que não estão presentes são adicionadas à lista de novas URLs.
    
3. **Download de Arquivos**: Para cada URL nova, o arquivo é baixado e salvo em um diretório chamado `resume_files`.
    
4. **Extração de Texto**: Após o download, o texto é extraído do arquivo PDF (atualmente, esta parte é um placeholder).
    
5. **Armazenamento no Banco de Dados**: O texto extraído e a URL são armazenados na tabela `resumes` do banco de dados especificado (MySQL ou SQLite).
    

## Como Utilizar

### Pré-requisitos

- Python 3.x
- Bibliotecas: `pandas`, `requests`, `sqlalchemy`, `openpyxl`, `mysql-connector-python` (para MySQL)

### Passos para Configuração

1. **Clone o Repositório**: Faça o clone do repositório para sua máquina local.
    
2. **Instale as Dependências**: Utilize o seguinte comando para instalar as dependências necessárias: