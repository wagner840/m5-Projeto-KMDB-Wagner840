# m5-Projeto-KMDB-Wagner840
Projeto BackEnd Django - Aplicação de Critico de cinema. 

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```