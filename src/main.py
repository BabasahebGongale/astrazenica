from opensearchpy import OpenSearch
import botocore
#CLUSTER_URL = 'https://search-test-domain-pgrwdinn75dvbfq5lvsgoxz62e.us-west-2.es.amazonaws.com'

CLUSTER_URL = 'https://search-opensearch-haystack-domain-r3unwbnrwi55amapqsgacbp6d4.us-west-2.es.amazonaws.com'

# Username : Azadmin
# Pass : Azadmin@1234

def get_client(cluster_url = CLUSTER_URL,username='Azadmin',password='Azadmin@1234'):

    client = OpenSearch(
        hosts=[cluster_url],
        http_auth=(username, password),
        verify_certs=False,
        ssl=False
    )
    print("OpenSearch client connected...",client)
    return client

client = get_client()



# def createCollection(client):
#     """Creates a collection"""
#     try:
#         response = client.create_collection(
#             name='tv-sitcoms',
#             type='SEARCH'
#         )
#         return response
#     except botocore.exceptions.ClientError as error:
#         if error.response['Error']['Code'] == 'ConflictException':
#             print(
#                 '[ConflictException] A collection with this name already exists. Try another name.')
#         else:
#             raise error
#
# createCollection(client)

index_name = "movies"

index_body = """{
  "settings": {
    "index": {
      "knn": True,
      "knn.algo_param.ef_search": 100
    }
  },
  "mappings": { 
    "properties": {
        "embedding": {
          "type": "knn_vector", #we are going to put
          "dimension": EMBEDDING_DIM,
          "method": {
            "name": "hnsw",
            "space_type": "l2",
            "engine": "nmslib",
            "parameters": {
              "ef_construction": 128,
              "m": 24
            }
         }
     }
}"""
#
# response = client.indices.get_alias("*")
# print("Response-",response)


# for index in client.indices.get('*'):
#   print(index)

#response = client.indices.create(index=index_name, body=index_body)


response = client.indices.get('embedindex')

print(response)


# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Principal": {
#         "AWS": "*"
#       },
#       "Action": "es:*",
#       "Resource": "arn:aws:es:us-east-1:xxxxxx:domain/xxxxx/*"
#     }
#   ]
# }
