# convert_templates.py
import string

"""
テンプレート定義：

"""
template011_summaise= """\
下の文章を200文字程度に要約してください。
## 文章
```
$data01
```
"""


def convert011_summarise(data01):
    t = string.Template(template011_summaise)
    return t.substitute(data01=data01)