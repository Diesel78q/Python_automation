import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages

def test_getting_POSTs():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    received_posts = response.json()
    assert len(received_posts) == 7, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    
    print(response.json())