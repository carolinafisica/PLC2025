import re

#Lista de tokens possíveis e respetivos padrões
token_specification = [
    ("COMMENT", r'#.*'),  #Comentários
    ("SELECT", r'\bselect\b'), #Palavra reservada SELECT; se não tivesse o \b, ia selecionar tudo o que contivesse select como selected, selection, etc.
    ("WHERE", r'\bwhere\b'), # Palavra reservada WHERE
    ("LIMIT", r'\bLIMIT\b'), # Palavra reservada LIMIT
    ("VAR", r'\?\w+'), # Variáveis: ?nome, ?desc, ?s, etc.
    ("PREFIX", r'\w+:\w+'), # Prefixos: dbo:MusicalArtist, foaf:name
    ("STRING", r'"[^"]*"@[a-z]+'), # Strings: "Chuck Berry"@en; [^"]* apanha zero ou mais caracteres que não são ", ou seja, "[^"]*" apanha tudo o que está entre aspas
    ("NUMBER", r'\d+'), # Números 
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("DOT", r'\.'),
    ("SEMICOLON", r';'), 
    ("SKIP", r'[ \t\n]+'), # Espaços em branco
]

def tokenize(code):
    tokens = []
    regex_parts = [f"(?P<{name}>{pattern})" for name, pattern in token_specification]
    regex = re.compile("|".join(regex_parts))  # Cria um padrão único que casa com SELECT ou WHERE OU VAR ou NUMBER ou ... ou seja, isto é um grande padrão que casa com todas as categorias de tokens 

    for match in regex.finditer(code): #Procura todos os matches no input tendo em conta o padrão total; cada match é um objeto que contém o texto encontrado, a posição no texto e qual grupo nomeado foi ativado (SELECT, VAR, STRING, etc.)
        kind = match.lastgroup #Guarda a categoria do match
        value = match.group() #Guarda o texto que deu match

        if kind == "SKIP" or kind == "COMMENT":
            continue

        else:
            tokens.append((kind, value))
    return tokens


# Exemplo de uso
if __name__ == "__main__":
    code = """# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""
    for token in tokenize(code):
        print(token)
