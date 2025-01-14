from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name="user_Products"):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query,**kwargs):
    print(kwargs)
    index = get_index()
    params = {}
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params["tagFilters"]= tags
            print(params)
    results = index.search(query,params)
    return results