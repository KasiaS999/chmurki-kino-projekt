from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "neo4j+s://fad2c7c7.databases.neo4j.io:7687",
    auth=("neo4j", "aqO-fedtuHEIuw_HNgoDK4MP5j1_ImuzQSS8AIe-Pl0"))


def list_all_people():
    query = "MATCH (p:Person)-[r]->() RETURN p, r"
    with driver.session() as session:
        return session.run(query).data()


def list_all_movies():
    query = "MATCH (n:Movie) RETURN (n)"
    with driver.session() as session:
        return session.run(query).data()


def find_and_return_movie(title):
    query = "MATCH (n:Movie WHERE n.title = '" + title + "') RETURN n"
    with driver.session() as session:
        return session.run(query).data()


def find_and_return_movies_year(year):
    query = f"MATCH (n:Movie WHERE n.released = {year}) RETURN n"
    with driver.session() as session:
        return session.run(query).data()


def find_movie_actors(title):
    query = ("MATCH (a:Movie {title: '" + title + "'})<-[:ACTED_IN]-(actors)"
                                                  " RETURN actors")
    with driver.session() as session:
        return session.run(query).data()


def find_cast(title):
    query = ("MATCH (a:Movie {title: '" + title + "'})<-[r]-(cast)"
                                                  " RETURN r, cast")
    with driver.session() as session:
        return session.run(query).data()


def find_persons_movies(person):
    query = ("MATCH (a:Person {name: '" + person + "'})-[r]->(cast)"
                                                   " RETURN r, cast")

    with driver.session() as session:
        return session.run(query).data()


def find_movie_director(title):
    query = ("MATCH (a:Movie {title: '" + title + "'})<-[:DIRECTED]-(director)"
                                                  " RETURN director")
    with driver.session() as session:
        return session.run(query).data()





