import elasticsearch
from elasticsearch_dsl import Search

# Database ---> elasticsearch
# Table ---> Index
# Field ---> Document

INDEX_NAME = "index_1"

ELASTIC_HOST = "https://localhost:9200"
USERNAME = "elastic"
PASSWORD = "M1LG8BaqGa8QTiC_hd3-"

client = elasticsearch.Elasticsearch(
    hosts=[ELASTIC_HOST], basic_auth=(USERNAME, PASSWORD), verify_certs=False
)

# data_1 = {
#     'id': 1,
#     'name': 'Django-ElasticSearch',
#     'number': '401',
#     'summary': 'A simple app runs based on django framework and search engine of elasticsearch.'
# }

# data_2 = {
#     'id': 2,
#     'name': 'Django-restapi',
#     'number': '601',
#     'summary': 'A simple app runs based on django framework.'
# }

# add_data_1 = client.index(index=INDEX_NAME, body=data_1)
# add_data_2 = client.index(index=INDEX_NAME, body=data_2)

# print(add_data_1)

if __name__ == "__main__":
    search_text = input("What do you want to search for: ")
    fields = ["name", "number", "summary"]

    resutls = (
        Search(index=INDEX_NAME)
        .using(client)
        .query("multi_match", fields=fields, fuzziness="AUTO", query=search_text)
    )

    for hit in resutls:
        print(f"ID: {hit.id}, File_Name: {hit.name}")
