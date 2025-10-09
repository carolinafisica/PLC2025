import re

def markdown_to_html(md_text):
    html_lines = []
    lines = md_text.split('\n')
    in_list = False  # flag para saber se estamos dentro de uma lista <ol>

    for line in lines:
        line = line.strip() #Remoção de espaços em branco no começo e fim da linha

        # Cabeçalhos
        if re.match(r'### ', line):  #Verificação se a linha começa com ###
            html_lines.append(f"<h3>{line[4:]}</h3>") #Pegar em tudo depois dos 4 primeiros caracteres e colocar entre <h3> e <\h3>
        elif re.match(r'## ', line):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif re.match(r'# ', line):
            html_lines.append(f"<h1>{line[2:]}</h1>")

        # Listas numeradas 
        elif re.match(r'\d+\.\s', line): #Verificação se a linha começa com algo do tipo 1. 
            if not in_list:
                html_lines.append("<ol>") #Abri a lista
                in_list = True
            item = re.sub(r'^\d+\.\s', '', line) #Remove o numero, o ponto e o espaço e deixa só o texto, subtituindo a parte que não se quer por uma string vazia
            html_lines.append(f"<li>{item}</li>") #Envolve o texto com <li> e </li>
        else: #Caso não faça match com algo do tipo 1. e ainda estiver dentro da lista, é para fechá-la
            if in_list:
                html_lines.append("</ol>") 
                in_list = False

            # Caso não faça match com algo do tipo 1. mas se já estiver fora da lista....

            # Bold 
            line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)  # Se fosse só .+ capturava 1 ou mais caracteres o máximo possivel, mas usando o ?, permite que seja só até fazer match com o padrão a seguir
            
            # Itálico 
            line = re.sub(r'\*(.+?)\*', r'<i>\1</i>', line)

            # Links 
            line = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

            # Imagens 
            line = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', line)

          
            html_lines.append(line) #Adiciona as linhas ao HTML

    # fecha lista
    if in_list:
        html_lines.append("</ol>")

    return '\n'.join(html_lines)


# Exemplo:
if __name__ == "__main__":
    md_text = """# Exemplo
##Subtítulo
Este é um **texto em bold** e este é um *em itálico*.
Como pode ser consultado em [página da UC](http://www.uc.pt)

1. Primeiro item
2. Segundo item
3. Terceiro item

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

    html = markdown_to_html(md_text)
    print(html)
