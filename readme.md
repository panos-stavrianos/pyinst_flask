## Example Flask app with standalone gunicorn packed with pyinstaller

#### Clone the repo and run this command to build one executable file 
 ```shell script
pyinstaller --onefile --add-data 'templates:templates' --add-data 'static:static' app.py
```

Then run the app
```shell script
./dist/app
```