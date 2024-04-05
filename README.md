## PyDividends:
### Code to return top 20 stocks that paid the highest percentages of dividends

### First:
1. Create a folder named files
2. The file can be downloaded on -> https://www.b3.com.br/ -> market-data-e-indices -> indices-amplos -> indice-brasil-100-ibrx-100 -> composicao-da-carteira
3. Rename the file to "ibr" and convert to xlsx

### Install Virtual Environment (venv): This will avoid globally instalations of libs:
```
pip install virtualenv
```

### Create new virtual environment with name venv (you can change it):
##### You can navigate through your Command Prompt to your desired project or just open the project on vcode and use the Command Prompt inside 
```
python -m venv venv       
```

### Start venv on you project (do this before install the libs bellow):
```
{venv_name}\scripts\activate.bat 
```

### Install pandas: this lib will be used to work with the data:
```
pip install pandas
```

```
pip install yfinance
```
