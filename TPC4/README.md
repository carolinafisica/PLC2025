Neste texto, os principais tipos de tokens são:

-Palavras reservadas que são palavras fixas da linguagem como select, where, LIMIT
-Variavéis como ?nome, ?desc, ?s, ?w
-Prefixos como dbo:MusicalArtist, foaf:name
-Cadeia de texto como "Chuck Berry"@en
-Símbolos como {, }, ., ;
-Números como 1000

Para criar este analisador léxico tenho de definir padrões para cada tipo de token