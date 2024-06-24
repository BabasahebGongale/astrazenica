import boto3
from botocore.config import Config
import time

from opensearchpy import OpenSearch, RequestsHttpConnection

# Build the client using the default credential configuration.
# You can use the CLI and run 'aws configure' to set access key, secret
# key, and default region.

my_config = Config(
    # Optionally lets you specify a region other than your default.
    region_name='us-west-2'
)

client = boto3.client('opensearch', config=my_config)

#domainName = 'my-test-domain'  # The name of the domain

domainName = 'https://search-opensearch-haystack-domain-r3unwbnrwi55amapqsgacbp6d4.us-west-2.es.amazonaws.com'

print("Using boto3 client-",client)
username='Azadmin'
password='Azadmin@1234'
http_auth = (username, password),

def indexData(host):
    """Create an index and add some sample data"""
    # Build the OpenSearch client
    client = OpenSearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=http_auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        timeout=300
    )
    # It can take up to a minute for data access rules to be enforced
    time.sleep(45)