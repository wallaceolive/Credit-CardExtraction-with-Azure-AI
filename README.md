💳 Extração de Cartões de Crédito com Azure AI
📌 Visão Geral

Este projeto foi desenvolvido como parte do desafio DIO - Desafio 1 Azure AI.
O objetivo é criar uma aplicação capaz de:

Receber imagens de cartões de crédito via upload

Armazenar essas imagens no Azure Blob Storage

Extrair automaticamente dados importantes do cartão usando Azure Document Intelligence (OCR):

Tipo do cartão (VISA, MasterCard)

Nome do titular

Banco emissor

Data de validade

O projeto utiliza Streamlit para interface e os serviços de IA do Microsoft Azure para reconhecimento de informações de cartões.

🧠 Tecnologias Utilizadas

Microsoft Azure

Azure Document Intelligence (OCR)

Azure Blob Storage

Python

Streamlit (interface web)

Requests (download de imagens)

dotenv (variáveis de ambiente)

APIs REST do Azure

🏗️ Arquitetura da Solução

Fluxo simplificado da aplicação:

O usuário realiza o upload da imagem do cartão.

A imagem é enviada para o Azure Blob Storage.

O Azure Document Intelligence processa a imagem e extrai os dados.

Os dados são exibidos na interface Streamlit:

Tipo de cartão

Nome do titular

Banco emissor

Data de validade

Caso a leitura falhe, o app informa que o cartão não é válido.

Diagrama do Fluxo
<img width="1919" height="990" alt="Análise de cartão - 1" src="https://github.com/user-attachments/assets/b8b2eea7-d016-4763-8b04-991bf6c889bc" />

⚙️ Recursos Azure Criados

Azure Document Intelligence: OCR e extração de dados de cartões

<img width="1036" height="906" alt="Ambiente Azure" src="https://github.com/user-attachments/assets/de4915fb-7257-4247-a593-b20d2d59fb29" />


Azure Blob Storage: Armazena imagens enviadas

Grupo de Recursos dedicado ao projeto

🧪 Implementação

O projeto está dividido em camadas:

1️⃣ Backend (Serviços)

services/blob_service.py → Upload de imagens para Azure Blob Storage

services/card_extractor.py → Extração de informações do cartão via OCR

2️⃣ Frontend (Interface)

src/app.py → Interface Streamlit para upload, exibição da imagem e dados extraídos

3️⃣ Configurações

utils/config.py → Configurações de endpoints, chaves e container do Azure

.env → Variáveis de ambiente para credenciais (não incluídas no repositório por segurança)

📄 Resultados
1️⃣ Cartão válido detectado
<img width="601" height="835" alt="Dio 2" src="https://github.com/user-attachments/assets/724b40f3-3692-44f0-9822-528906193725" />

2️⃣ Cartão inválido
<img width="618" height="787" alt="cartao invalido" src="https://github.com/user-attachments/assets/cecd52ad-5c19-4c13-a183-269e0acf07a0" />

🔐 Segurança

As chaves de acesso do Azure não estão expostas no código

Uso de variáveis de ambiente para todas as credenciais

Imagens armazenadas em container dedicado, sem exposição pública direta

✅ Conclusão

O projeto atende aos requisitos propostos pela DIO, demonstrando uso prático de serviços de IA do Azure para OCR em cartões de crédito.

A solução pode ser expandida para:

Validar números de cartões usando algoritmo de Luhn

Suportar diferentes tipos e layouts de cartão

Integrar com dashboards, apps web ou mobile

📚 Referências

Document Intelligence Azure

Azure Blob Storage

Streamlit
