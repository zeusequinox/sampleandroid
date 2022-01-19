import requests
import json
import sys


def get_all_scans():
    query = '''
        query {
          scans {
            scans {   
              id
              title
              progress
            }
          }
        }
        '''
    request = requests.post(uri,json={"query":query}, headers=headers)
    if request.status_code == 200:
        print(request.json())
        data = requests.json()
        return data
    else:
        print("Forbidden")
        return False



def scan(title,path,headers):
    #path = sys.argv[1]
    apk = open(path,'rb')
    query = '''mutation newMobileScan($title: String!, $assetType: String!, $application: Upload!, $plan: String!) {
  createMobileScan(title: $title, assetType:$assetType, application: $application, plan: $plan) {
    scan {
        id
    }
  }
}'''
    data = {
        'operations': json.dumps({'query': query,
                                  'variables': {'title': 'fake_title', 'assetType': 'android', 'application': None,
                                                'plan': 'free'}}),
        'map': json.dumps({
            '0': ['variables.application'],
        })
    }
    resp = requests.post('https://api.ostorlab.co/apis/graphql/', data=data, files={'0': apk.read(),}, headers=headers)

    if resp.status_code == 200:
        return "Uploaded Successfully! {0}".format(str(resp.text))
    else:
        return "Failed to Upload, {0}".format(str(resp.text))



if __name__ == '__main__':
    
    uri = "https://api.ostorlab.co/apis/graphql_token/"
    headers = {"X-Api-Key": "" }
    if len(sys.argv) == 1:
        print("Invalid Parameters Specified")
        exit()
    else:
        title = sys.argv[1]
        apiKey = sys.argv[2]
        path = sys.argv[3]
        headers = {"X-Api-Key": apiKey }
        print(scan(title,path,headers))
    #print(apiKey,path,headers)
