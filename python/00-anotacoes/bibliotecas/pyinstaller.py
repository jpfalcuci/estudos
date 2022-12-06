""" pyinstaller =>
 
    1) Instalar o pyinstaller:
        pip install pyinstaller
 
    2) Criar o executável:
        pyinstaller file.py
            pasta build é usada durante o processo interno de criação do executável
            dist fica tudo que é do executável
        pyinstaller --noconsole
            evita janela de console
        pyinstaller --name="Executador de Projetos"
            cria uma pasta "Executador de Projetos" dentro de dist
        pyinstaller --icon="icon.ico"
            usa arquivo como ícone; arquivo do ícone deve estar na mesma pasta dist
        pyinstaller --icon="icon.ico" --add-data="icon.ico;."
            adiciona o arquivo icon.ico; '.' significa pasta raiz do projeto onde o arquivo ficará durante a execução
        pyinstaller --onefile
            transforma todo conteúdo em um só arquivo
 
        pyinstaller --noconsole --name="Executador de Projetos" --icon="icon.ico" --add-data="icon.ico;." --onefile main.py """
