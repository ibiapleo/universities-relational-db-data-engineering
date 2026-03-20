## Atividade 2

### Integrantes do Grupo

- Leonardo José Oliveira Ibiapina
- João Lucas Marcolino Cavalcanti Silva
- Ênio Matheus Gomes Bazante

## Implementacao Realizada

### Arquitetura em Camadas

O projeto foi estruturado seguindo o padrão de camadas, separando as responsabilidades entre extração e carregamento de dados:

#### Camada de Extração (`src/extract.py`)

Classe `UniversityExtractor` responsável por acessar a API e desserializar os dados retornados em JSON.

**Funcionalidades principais:**

- `fetch_by_country(country: str)`: Busca universidades de um país específico.
- `fetch_by_countries(countries: Iterable[str])`: Busca universidades de múltiplos países em uma única execução.

Todas as operações contêm docstrings explicativas seguindo o padrão Python.

#### Camada de Carregamento (`src/load.py`)

Classe `UniversityLoader` responsável por transformar listas de dicionários em dados persistidos no banco de dados.

**Funcionalidades principais:**

- `load(universities: list[dict])`: Persiste universidades no banco e retorna a quantidade inserida.
- Evita duplicações usando consultas filtradas por nome e país.
- Gerencia transações com suporte adequado ao SQLAlchemy ORM.

#### Integração (`main.py`)

O script principal orquestra a extração e carga, permitindo buscar dados de vários países em uma única execução:

```python
countries = ["Brazil", "Argentina", "Chile"]
extractor = UniversityExtractor()
loader = UniversityLoader()
universities = extractor.fetch_by_countries(countries)
inserted = loader.load(universities)
```

### Boas Práticas Implementadas

- **Docstrings**: Todos os métodos possuem docstrings descritivas em português.
- **Type Hints**: Anotações de tipo em todos os métodos para melhor legibilidade e segurança.
- **Separação de Responsabilidades**: Classes separadas para extração e carregamento.
- **Tratamento de Erros**: Validação adequada com `raise_for_status()` em requisições HTTP.

### Formatacao com Black

O projeto utiliza a biblioteca Black para garantir formatação consistente.

#### Como Executar

##### Linux / macOS

1. Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

3. Instale as dependencias (incluindo Black):

```bash
pip install -r requirements.txt
```

4. Rode o formatador em todo o projeto:

```bash
black .
```

5. Execute o arquivo principal:

```bash
python main.py
```

##### Windows (PowerShell)

1. Crie o ambiente virtual:

```powershell
python -m venv .venv
```

2. Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependencias (incluindo Black):

```powershell
pip install -r requirements.txt
```

4. Rode o formatador em todo o projeto:

```powershell
black .
```

5. Execute o arquivo principal:

```powershell
python main.py
```
