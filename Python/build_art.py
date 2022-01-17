import json
import requests
from json import JSONEncoder


class ArtProcessingEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class ArtInput:
    list_references = []
    def __init__(self, co_relation_id):
        self._co_relation_id = co_relation_id

    @property
    def co_relation_id(self):
        return self._co_relation_id

    @co_relation_id.setter
    def co_relation_id(self, new_id):
        self._co_relation_id = new_id

    @classmethod
    def set_reference_list(cls, references_list):
        cls.list_references = references_list

    def to_dict(self) -> dict:
        return {"art:correlationID": f"{self._co_relation_id}", "art:references": f"{ArtInput.list_references}"}

    def __repr__(self):
        return f"Input builder for ART"


def main():
    with open("input.txt", 'r', encoding="UTF-8") as file:
        references = file.readlines()
        references = [ref.strip() for ref in references]
    art_input = ArtInput("references")
    art_input.set_reference_list(references)
    data = json.dumps(art_input.to_dict(), ensure_ascii=False).encode()
    print(data)
    response = invoke_url(url='https://dev.art.elsevier.com/structure', data=data)
    print(response)


jwt = {
        'dev': "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyX2lkIjoxMjN9."
            "YR93vT1wUoCCbziUVy9sA3PtZGewU_HZHTcGWzOBo8VqVGvoOQZkPqqbS"
            "sf8yYU7gvGyptUqBGhDilZc"
            "bUM7d6c-BJPBwaI6hc1HuHTwzMWcAU4IjsDvAl3uN245ON3MPTOmK0z"
            "jieKjd3j-5EMXw"
            "UkeVOKvMvwUUCW9azCcw2lMlrwnf5M1AQUb9u9jFld3hU5UTN9nJRz0"
            "5LI2Cnf6iXD4jBudF"
            "AUejcg9QjPMz4qW3thUkCoFFmEn2obXZv-dzfg-we8RTSzI5aEXHHJYa4"
            "BG-reiK8UrLJ1kJQYy"
            "yiI3vN0yNyMj-prOZk8DKBaF568z5l0JmfsFNQUKrV49dXqMHAkAMLH"
            "RMSNaoWcS2DR3kA"
            "d16fROa1Eo632eJVMeeAkjuAjeh_guCE11jn_f5GmlwGKlfp3G1XEO"
            "zpzJaTPnd45V"
            "Qmb4rWmHK_PMug5sdDgsaqS5HIXr9naPRipbTY52sQaWcohZeAEyXn"
            "KbjDcamX4heBc4"
            "NwzVo8hCzaHbAEtuxfVBzSbX5zm8f3LcMrvb9AssajrLZQeDf01-dv"
            "FC_jVRbFP-AxdL6R"
            "uQvx94mq4uH5irHw4Uqrtc55A3T1V19aUXxSAsuB_qfuv74Ic_cQQ5"
            "WYk_9Mni1ww9i2k5k"
            "eTSLB_X-Dy9eCcZkUJ69GdCU35jcGOmIDZlClqov-I"}

def headers():
    return {'Content-Type': "application/json",
            "X-Jwt-Assertion": f"{jwt['dev']}"}


def invoke_url(url, data):
    response = requests.post(url,
                             headers=headers(),
                             data=data)
    return response


if __name__ == "__main__":
    main()
