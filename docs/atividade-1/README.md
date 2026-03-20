## Modelagem das Tabelas

Para armazenar os dados retornados pela API, foi utilizada uma modelagem relacional composta por tres tabelas principais:

- **universities**: Armazena informacoes basicas de cada universidade (nome, pais, estado/provincia e codigo alfa).
- **university_domains**: Armazena os dominios associados a cada universidade.
- **university_webpages**: Armazena as paginas web associadas a cada universidade.

O relacionamento entre as tabelas e feito via chave estrangeira, garantindo integridade referencial.

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

## Estrategia para Dados de Varios Paises

Para dados de multiplos paises, foram adotadas as seguintes praticas:

- **Campo obrigatorio de pais**: Toda universidade possui o campo `country`, permitindo consultas filtradas por pais.
- **Chaves primarias e estrangeiras**: Uso de UUID como chave primaria para universidades, garantindo unicidade global e integridade referencial.
- **Normalizacao**: Dominios e web pages sao armazenados em tabelas separadas, evitando redundancia e facilitando manutencao.
- **Indices**: Uso de indices nas chaves primarias e estrangeiras para melhorar o desempenho das consultas.

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

## Como Executar

### Linux / macOS

1. Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Execute o arquivo principal:

```bash
python main.py
```

### Windows (PowerShell)

1. Crie o ambiente virtual:

```powershell
python -m venv .venv
```

2. Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependencias:

```powershell
pip install -r requirements.txt
```

4. Execute o arquivo principal:

```powershell
python main.py
```

O banco de dados `unis.db` sera criado automaticamente e populado com os dados da API.

Para realizar uma consulta no banco:

```bash
sqlite3 unis.db
sqlite> (cole aqui o exemplo de consulta)
```

## Visualizacao do Banco

O arquivo `unis.db` pode ser aberto com ferramentas como DB Browser for SQLite ou extensoes do VS Code para inspecao dos dados.
