## Modelagem das Tabelas

Para armazenar os dados retornados pela API, optei por uma modelagem relacional composta por três tabelas principais:

- **universities**: Armazena informações básicas retornadas de cada universidade (nome, país, estado/província, código alfa).
- **university_domains**: Armazena os domínios associados a cada universidade.
- **university_webpages**: Armazena as páginas web associadas a cada universidade.

O relacionamento entre as tabelas é feito via chave estrangeira, garantindo integridade referencial.

### Exemplo da modelagem

```sql
CREATE TABLE universities (
    id VARCHAR(36) PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    state_province TEXT,
    alpha_two_code TEXT
);

CREATE TABLE university_domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    university_id INTEGER,
    domain TEXT,
    FOREIGN KEY (university_id) REFERENCES universities(id)
);

CREATE TABLE university_webpages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    university_id INTEGER,
    web_page TEXT,
    FOREIGN KEY (university_id) REFERENCES universities(id)
);
```

## Estratégia para Dados de Vários Países

Para dados de múltiplos países, adotei as seguintes práticas:

- **Campo obrigatório de país**: Toda universidade possui o campo `country`, permitindo consultas filtradas por país.
- **Chaves primárias e estrangeiras**: Uso de UUID como chave primária para universidades, garantindo unicidade global e integridade referencial.
- **Normalização**: Domínios e web pages são armazenados em tabelas separadas, evitando redundância e facilitando manutenção.
- **Índices**: O uso de índices nas chaves primárias e estrangeiras para melhorar o desempenho das consultas.

Exemplo de consulta:
```sql
SELECT 
    u.name, 
    u.country, 
    d.domain, 
    w.web_page
FROM universities u
JOIN university_domains d ON u.id = d.university_id
JOIN university_webpages w ON u.id = w.university_id
WHERE u.country = 'Brazil';
```

---

## Como Executar

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
2. Execute o arquivo principal:
   ```
   python main.py
   ```
3. O banco de dados `unis.db` será criado automaticamente e populado com os dados da API.

4. Para realizar uma consulta no banco:
   ```
   sqlite3 unis.db
   sqlite> (COLE AQUI O EXEMPLO DE CONSULTA)
   ```

---

## Visualização do Banco

O arquivo `unis.db` pode ser aberto com ferramentas como [DB Browser for SQLite](https://sqlitebrowser.org/) ou extensões do VS Code para inspeção dos dados.
