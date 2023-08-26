# convert_templates.py
import string

"""
テンプレート定義：

"""
template011_summarise = """\
下の文章を200文字程度に要約してください。
## 文章
```
$data01
```
"""

template012_questionanswering = """\
テキストに基づいて下記質問に答えてください。もし答えがない場合には、「私は知らない」と答えてください。
## テキスト：
```
$data02
```

## 質問：
- $data01
"""

templates = {
    "011_summarise" : {
        "template": template011_summarise,
        "num_args": 1
    },
    "012_questionanswering" : {
        "template": template012_questionanswering,
        "num_args": 2
    }
}


class Template():
    """
    指定されたテンプレートの情報・ヘルパー関数を保持する。

    Attributes
    ----------
    type : str
        プロンプト雛形の名称

    Attributes
    ----------
    type : str
        プロンプト雛形の名称
    template : string.Template
        テンプレートの雛形情報
    data01 ～ data05 : str
        雛形に与える文字列。
    num_args : int
        雛形に与える文字列の数
    """
    def __init__(self, type):
        self.type = type

        self.template = None
        self.num_args = 0
        self.data01 = None
        self.data02 = None
        self.data03 = None
        self.data04 = None
        self.data05 = None
        if self.type in templates:
            t = templates[self.type]
            self.template = t["template"]
            self.num_args = t["num_args"]
        else:
            self.template = None
            self.num_args = 0

    def exist_template(self):
        if self.template != None:
            return True
        else:
            return False

    def conver_template(self):
        template = string.Template(self.template)
        if self.num_args == 1:
            return template.substitute(data01=str(self.data01))
        if self.num_args == 2:
            return template.substitute(
                data01=str(self.data01),
                data02=str(self.data02)
            )
