# m5-Projeto-KMDB-Wagner840
Projeto BackEnd Django - Aplicação de Critico de cinema. 

Projeto KMDB
O Projeto KMDB é uma aplicação de banco de dados de filmes completa, construída com Django e Python. Este projeto apresenta gerenciamento de filmes, usuários e revisões.

Endpoints
Aqui estão alguns dos principais endpoints que você pode usar para interagir com a API:

Filmes
GET /movies/: Retorna uma lista de todos os filmes.
POST /movies/: Cria um novo filme. Requer um corpo de solicitação JSON com os detalhes do filme.
GET /movies/{id}/: Retorna os detalhes de um filme específico.
PUT /movies/{id}/: Atualiza os detalhes de um filme específico. Requer um corpo de solicitação JSON com os novos detalhes do filme.
DELETE /movies/{id}/: Exclui um filme específico.
Usuários
GET /users/: Retorna uma lista de todos os usuários.
POST /users/: Cria um novo usuário. Requer um corpo de solicitação JSON com os detalhes do usuário.
GET /users/{id}/: Retorna os detalhes de um usuário específico.
PUT /users/{id}/: Atualiza os detalhes de um usuário específico. Requer um corpo de solicitação JSON com os novos detalhes do usuário.
DELETE /users/{id}/: Exclui um usuário específico.
Revisões
GET /movies/{movie_id}/reviews/: Retorna uma lista de todas as revisões para um filme específico.
POST /movies/{movie_id}/reviews/: Cria uma nova revisão para um filme específico. Requer um corpo de solicitação JSON com os detalhes da revisão.
GET /movies/{movie_id}/reviews/{review_id}/: Retorna os detalhes de uma revisão específica.
PUT /movies/{movie_id}/reviews/{review_id}/: Atualiza os detalhes de uma revisão específica. Requer um corpo de solicitação JSON com os novos detalhes da revisão.
DELETE /movies/{movie_id}/reviews/{review_id}/: Exclui uma revisão específica.
