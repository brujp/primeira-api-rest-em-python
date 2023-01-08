# API Rest em Python utilizando o Flask e TinyDB

## API Rest desenvolvida em Python - Live de Python #175 (Eduardo Mendes) - https://www.youtube.com/watch?v=1_nQ5A2HcgU
 
## Documentações

Documentação do Flask: https://flask.palletsprojects.com/en/2.2.x/

Documentação do TinyDB: https://tinydb.readthedocs.io/en/latest/

## Utilização da API

✅ Para acessar a documentação (Swagger), rodar a aplicação localmente e acessar:
http://localhost:5000/apidoc/swagger

Utilizar o Postman ou Insomnia para realizar as requests!

⏫ POST /pessoas: 
{
	"idade": 23,
	"nome": "Bruninho"
}

🔃 PUT /pessoas/{id}
{
	"id": 1,
	"idade": 23,
	"nome": "Bruninho"
}

⏬ GET /pessoas

❌ DELETE /pessoas/{id}

