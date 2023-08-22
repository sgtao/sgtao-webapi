# sgtao-webapi
- Webアプリ向けのAPIサービスを立ち上げたい

## setup
### git clone
```sh
# git clone <repository>
cd sgtao-webapi
python -m venv venv
```

### install packages
```sh
source venv/bin/activate
pip install -r ./requirements.txt
```

### run app
- run [main.py](./webapi/main.py)
```sh
uvicorn main:app --reload
```

## for deploy to [Deta Space](https://deta.space/)

### install space-cli
```sh
curl -fsSL https://get.deta.dev/space-cli.sh | sh
```

### login Deta space
- 前もって[Deta space](https://deta.space/)にログインして、Tokenを発行しておく
```sh
space login
# Enter Token after exec. command
```

#### 実行ログ
```sh
$ space login
To authenticate the Space CLI with your Space account, generate a new access token in your Space settings and paste it below:
? Enter access token (xx chars) > *************************
👍 Login Successful!
Checking for new Space CLI version...
```

### create project
```sh
space new
```

### edit `Spacefile`
```yaml
# Spacefile Docs: https://go.deta.dev/docs/spacefile/v0
v: 0
micros:
  - name: webapi
    src: .
    path: api
    engine: python3.9
    public_routes:
      - "/api/allinone/*"
```

## deploy project
```sh
space push
```

- 実行したら、[Deta Space](https://deta.space/)でプロジェクトを確認する
  * private Cloud上で、FastAPI docsでAPI挙動を確認
  * ローカルから APIのURIを確認
```sh
$ curl -X 'GET' 'https://sgtaowebapi-xxx.deta.app/api/allinone/' \
  -H 'accept: application/json' -s | jq
{
  "message":"hello from allinone."
}
```

## License
- MIT License.

