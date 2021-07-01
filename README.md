
# Blog Rest Django3

Aplicação feita em Python utilizando Django3 para a vaga de desenvolvedor na empresa Mudi.

A aplicação devia fornecer: 
- Um App de Autores     
    - Uma rota para cadastro de autores contendo ( Nome e Sobrenome ).     
    - Uma rota para listagem de autores
- Um App de Publicações     
    - Uma rota para cadastro de publicações contendo ( Titulo, Descrição e Autor).     
    - Uma rota para listagem das publicações.     
    - Um filtro de publicações por autor.
## API Referencia

#### Obter todos os autores

```http
  GET /authors
```

#### Inserir novo autor

```http
  POST /authors
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Requerido**. Primeiro nome do autor |
| `last_name` | `string` | **Requerido**. Sobrenome do autor |


#### Obter todas as publicações

```http
  GET /publications
```

#### Obter publicação pelo author
```http
  GET /publications/?author_id=<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Requerido**. Id do autor |


  
## Rodar projeto
#### Iniciar ambiente virtual
```bash
python -m venv .venv 
pip install -r requirements.txt 
```

#### Rodar projeto
```bash
cd blog
python manage.py runserver
```

### Acessar
```html
http://127.0.0.1:8000/authors/
http://127.0.0.1:8000/publications/
```
    
