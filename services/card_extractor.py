from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from utils.config import Config
import requests
import re


def extract_credit_card_info(image_url: str) -> dict | None:
    try:
        credential = AzureKeyCredential(Config.KEY)
        client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        response = requests.get(image_url)
        if response.status_code != 200:
            return None

        image_data = response.content

        poller = client.begin_analyze_document(
            model_id="prebuilt-layout",
            body=image_data,
            content_type="application/octet-stream"
        )

        result = poller.result()

        full_text = []
        for page in result.pages:
            for line in page.lines:
                full_text.append(line.content)

        ocr_text = " ".join(full_text)

        # 👀 DEBUG ABSOLUTO — isso vai aparecer no Streamlit
        return {
            "card_name": "Detectado" if re.search(r"\d{4}", ocr_text) else None,
            "holder_name": "OCR DEBUG",
            "bank_name": "OCR DEBUG",
            "expiration_date": "OCR DEBUG",
            "raw_text": ocr_text
        }

    except Exception as e:
        return {
            "card_name": None,
            "raw_text": f"ERRO OCR: {e}"
        }
