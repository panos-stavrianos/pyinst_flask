## Example Flask app with standalone gunicorn packed with pyinstaller

#### Clone the repo and run this command to build one executable file 
> preferably make a venv and `pip install -r requirements.txt`
 ```shell script
pyinstaller --onefile --add-data 'templates:templates' app.py
```

Then run the app
```shell script
./dist/app
```