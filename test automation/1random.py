import requests


class Test_new_joke():

    # Create new joke

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        # Create random joke

        url = "https://api.chucknorris.io/jokes/random"
        result = requests.get(url)
        print("Status code:" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Accepted")
        else:
            print("Failed")
        result.encoding = "utf-8"
        print(result.text)
        chek = result.json()
        # chek_info = chek.get("categories")
        # print(chek_info)
        # assert chek_info == []
        # print("Category accepted")
        chek_info_value = chek.get("value")
        print(chek_info_value)
        name = "Chuck"
        if name in chek_info_value:
            print("Chuck finded")
        else:
            print("Chuck is not finded")


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()
