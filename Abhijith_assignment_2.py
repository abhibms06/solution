# Assignment 2 (Couchbase Programming assignment )
# Submitter name : Abhijith Jain

# Problem statment
'''
Simple query tool: Install the latest couchbase-server and enable data, query and index
 services. Load the sample bucket “travel-sample”. Create a tool that takes a couchbase N1QL query to travel sample bucket as a command line parameter and print the query results back to user. The tool can use any couchbase sdk to connect to the travel sample
 bucket and query. The tool is also expected to retry the query in temporary failure cases.
'''

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery

# Default bucket name
bucket_name = 'travel-sample'
bucket = Bucket('couchbase://localhost/'+ bucket_name)

print('Enter N1QL query: ', end='')
input_query = input()

query = N1QLQuery(input_query)

# Retry in case of temporary failures(timeout)
query.timeout = 30

# Display results
for row in bucket.n1ql_query(query):
    for k in row.keys():
        print(row[k],end=' ')
    print()

