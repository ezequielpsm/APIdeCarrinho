from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert('algum filme', 'comedia', 2010)

repo.delete('Batman')

data = repo.select()

print(data)
