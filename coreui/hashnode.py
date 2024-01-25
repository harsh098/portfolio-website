from os import getenv
import requests

def run_query(query, headers):
    response = requests.post(url="https://gql.hashnode.com", json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

def getBlogs():
    query="""
        query Publication {
        publication(host: "randomtinkering.hashnode.dev") {
        title
        posts(first: 10) {
          edges {
            node {
              title
              brief
              url
              coverImage {
                attribution
                photographer
                url
              }
            }
          }
        }
      }
    }
    """
    headers = {
        "Authorization" : str(getenv("HASHNODE_API_TOKEN"))
    }

    data= run_query(query, headers)
    posts = data['data']['publication']['posts']['edges']
    posts = [{
        "title":x['node']['title'], 
        "cover":x['node']['coverImage']['url'], 
        "brief":x['node']['brief'], 
        "link": f"{x['node']['url']}"
        } for x in posts]
    return posts