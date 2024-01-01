import elasticsearch
from elasticsearch_dsl import Search

ELASTIC_HOST = "https://localhost:9200"
USERNAME = "elastic"
PASSWORD = "M1LG8BaqGa8QTiC_hd3-"

client = elasticsearch.Elasticsearch(
    hosts=[ELASTIC_HOST], basic_auth=(USERNAME, PASSWORD), verify_certs=False
)

def lookup(query, index, fields):
    # in case of no query.
    if not query:
        return 
    
    resutls = Search(index=index) \
              .using(client) \
              .query("multi_match", fields=fields, fuzziness="AUTO", query=query)

    q_results = []
    for hit in resutls:
        print(f"ID: {hit.id}, URL: {hit.url}, File_Name: {hit.title}")

        data = {
            'title': hit.title,
            'description': hit.description,
            'url': hit.url
        }
        
    q_results.append(data)
    return q_results


# lookup("PS4", "products", ["title", "description"])