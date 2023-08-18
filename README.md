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
pip install -r webapi/requirements.txt
```

### run app
- run [main.py](./webapi/main.py)
```sh
uvicorn webapi.main:app --reload
```

## License
MIT License

