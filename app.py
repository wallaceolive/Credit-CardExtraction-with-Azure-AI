import streamlit as st
from services.blob_service import upload_to_blob_storage
from services.card_extractor import extract_credit_card_info


def config_interface():
    st.title("Upload de Arquivos - DIO - Desafio-1 - Azure - Fake - Docs")

    uploaded_file = st.file_uploader(
        "Escolha uma imagem do cartão",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        file_name = uploaded_file.name

        # Envia o arquivo para o Azure Blob Storage
        blob_url = upload_to_blob_storage(uploaded_file, file_name)

        if blob_url:
            st.success(f"Arquivo '{file_name}' enviado com sucesso!")
            st.write(f"URL: {blob_url}")

            # 🔥 EXTRAÇÃO (agora existe de verdade)
            credit_card_info = extract_credit_card_info(blob_url)

            show_image_credit_validation(blob_url, credit_card_info)
        else:
            st.error("Ocorreu um erro ao enviar o arquivo.")


def show_image_credit_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_container_width=True)
    st.write("### Informações do Cartão de Crédito:")

    if credit_card_info and credit_card_info.get("raw_text"):
        with st.expander("🔍 Texto OCR detectado"):
            st.text(credit_card_info["raw_text"])


    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown(
            f"<h2 style='color: green;'>Cartão Válido: {credit_card_info['card_name']}</h2>",
            unsafe_allow_html=True
        )

        st.write(f"**Nome do Titular:** {credit_card_info['holder_name']}")
        st.write(f"**Banco Emissor:** {credit_card_info['bank_name']}")
        st.write(f"**Validade:** {credit_card_info['expiration_date']}")

    else:
        st.markdown(
            "<h2 style='color: red;'>Cartão de Crédito Não Válido</h2>",
            unsafe_allow_html=True
        )
        st.write("Não foi possível identificar um cartão de crédito válido.")


if __name__ == "__main__":
    config_interface()
