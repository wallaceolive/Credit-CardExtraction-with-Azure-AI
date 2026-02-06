# 💳 Extração de Cartões de Crédito com Azure AI

## 📌 Visão Geral
Este projeto foi desenvolvido como parte do desafio **DIO - Desafio 1 Azure AI**.  
O objetivo é criar uma aplicação capaz de:

- Receber imagens de cartões de crédito via upload
- Armazenar essas imagens no **Azure Blob Storage**
- Extrair automaticamente dados importantes do cartão usando **Azure Document Intelligence (OCR)**:
  - Tipo do cartão (VISA, MasterCard)
  - Nome do titular
  - Banco emissor
  - Data de validade

O projeto utiliza **Streamlit** para interface e os serviços de IA do **Microsoft Azure** para reconhecimento de informações de cartões.

---

## 🧠 Tecnologias Utilizadas

**Microsoft Azure**

- Azure Document Intelligence (OCR)
- Azure Blob Storage

**Python**

- Streamlit (interface web)
- Requests (download de imagens)
- dotenv (variáveis de ambiente)
- APIs REST do Azure

---

## 🏗️ Arquitetura da Solução
Fluxo simplificado da aplicação:

1. O usuário realiza o **upload da imagem do cartão**.
2. A imagem é enviada para o **Azure Blob Storage**.
3. O **Azure Document Intelligence** processa a imagem e extrai os dados.
4. Os dados são exibidos na interface Streamlit:
   - Tipo de cartão
   - Nome do titular
   - Banco emissor
   - Data de validade
5. Caso a leitura falhe, o app informa que o cartão não é válido.

**SERVIÇO DE CONFIGURAÇÃO**:

<p align="center">
  <img src="https://github.com/user-attachments/assets/b8b2eea7-d016-4763-8b04-991bf6c889bc" width="800">
</p>

---

## ⚙️ Recursos Azure Criados

- **Azure Document Intelligence**: OCR e extração de dados de cartões  

<p align="center">
  <img src="https://github.com/user-attachments/assets/de4915fb-7257-4247-a593-b20d2d59fb29" width="600">
</p>

- **Azure Blob Storage**: Armazena imagens enviadas
- **Grupo de Recursos** dedicado ao projeto

---

## 🧪 Implementação

O projeto está dividido em camadas:

### 1️⃣ Backend (Serviços)
- `services/blob_service.py` → Upload de imagens para Azure Blob Storage
- `services/card_extractor.py` → Extração de informações do cartão via OCR

### 2️⃣ Frontend (Interface)
- `src/app.py` → Interface Streamlit para upload, exibição da imagem e dados extraídos

### 3️⃣ Configurações
- `utils/config.py` → Configurações de endpoints, chaves e container do Azure
- `.env` → Variáveis de ambiente para credenciais (não incluídas no repositório por segurança)

---

## 📄 Resultados

### 1️⃣ Cartão válido detectado

<p align="center">
  <img src="https://github.com/user-attachments/assets/724b40f3-3692-44f0-9822-528906193725" width="400">
</p>

### 2️⃣ Cartão inválido

<p align="center">
  <img src="https://github.com/user-attachments/assets/cecd52ad-5c19-4c13-a183-269e0acf07a0" width="400">
</p>

---

## 🔐 Segurança

- As chaves de acesso do Azure **não estão expostas no código**
- Uso de **variáveis de ambiente** para todas as credenciais
- Imagens armazenadas em container dedicado, sem exposição pública direta

---

## ✅ Conclusão

O projeto atende aos requisitos propostos pela DIO, demonstrando **uso prático de serviços de IA do Azure para OCR em cartões de crédito**.  

A solução pode ser expandida para:

- Validar números de cartões usando algoritmo de Luhn  
- Suportar diferentes tipos e layouts de cartão  
- Integrar com dashboards, apps web ou mobile  

---

## 📚 Referências

- [Document Intelligence Azure](https://learn.microsoft.com/en-us/azure/applied-ai-services/document-intelligence/overview)  
- [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/)  
- [Streamlit](https://streamlit.io/)
