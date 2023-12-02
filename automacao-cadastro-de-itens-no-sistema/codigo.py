# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa(exemplo)
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui as pag
import time 
import pandas as pd

EMAIL = "email@exemplo.com"
SENHA = "exemplo123"

pag.PAUSE = 0.3

# DICAS:
# pag.write -> escrever um texto
# pag.press -> apertar 1 tecla
# pag.click -> clicar em algum lugar da tela
# pag.hotkey -> combinação de teclas

# abrir o navegador (chrome)

# modo 1:
# pag.press("win")
# pag.write("chrome")c
# pag.press("enter")

# modo 2:
pag.hotkey("win","r")
pag.write("chrome")
pag.press("enter")

# entrar no link 

pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")
# aguardar carregamento da página
time.sleep(3)

# Passo 2: Fazer login (user: email@exemplo.com | pass: exemplo123)

# selecionar o campo de email
pag.click(x=748, y=391)

# escrever o email
pag.write(EMAIL)
pag.press("tab")
pag.write(SENHA)
pag.press("enter")
time.sleep(3)


# Passo 3: Importar a base de produtos para cadastrar

tabela = pd.read_csv("produtos.csv")
print(tabela)

# tabela.columns -> percorre colunas da tabela
# tabela.index -> percorre os indices(linhas) da tabela 

for linha in tabela.index:
    print(linha)
    # Passo 4: Cadastrar um produto

    # clicar no campo de código
    pag.click(x=779, y=283)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, 'codigo']
    # preencher o campo
    pag.write(str(codigo))
    # passar para o próximo campo
    pag.press("tab")
    # preencher os campos
    pag.write(str(tabela.loc[linha, 'marca']))
    pag.press("tab")

    pag.write(str(tabela.loc[linha, 'tipo']))
    pag.press("tab")

    pag.write(str(tabela.loc[linha, 'categoria']))
    pag.press("tab")

    pag.write(str(tabela.loc[linha, 'preco_unitario']))
    pag.press("tab")

    pag.write(str(tabela.loc[linha, 'custo']))
    pag.press("tab")

    if not pd.isna(tabela.loc[linha, 'obs']):
        pag.write(str(tabela.loc[linha, 'obs']))
    pag.press("tab")
    
    pag.press("enter") # cadastra o produto (botao enviar)
    # dar scroll até o topo
    pag.scroll(5000)

    # Passo 5: Repetir o processo de cadastro até o fim
