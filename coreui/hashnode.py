from os import getenv
import requests

def run_query(query, headers):
    response = requests.post(url="https://api.hashnode.com", json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

def getBlogs():
    query="""{
        user(username: "%s") {
          publication {
            posts(page: 0) {
              _id
              cuid
              coverImage
              title
              brief
            }
          }
        }
      }"""%(str(getenv("HASHNODE_USERNAME")))
    headers = {
        "Authorization" : str(getenv("HASHNODE_API_TOKEN"))
    }

    data= run_query(query, headers)
    posts = data['data']['user']['publication']['posts']
    posts = [{"title":x['title'], "cover":x['coverImage'], "brief":x['brief']} for x in posts]
    return posts