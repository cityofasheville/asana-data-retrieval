import asana
import json
import os
def getProjects():
    token = os.getenv('ASANA_TOKEN')
    print(token)
    client = asana.Client.access_token(token)

    result = client.tasks.get_tasks(fields = ['gid', 'followers', 'assignee.name', 'name', 'custom_fields'], opt_pretty=True, project=1200128036189056)

    #print(result)
    projects = []
    for item in result:
        print(item)
        projects.append(item)
    return projects

def lambda_handler (event, context):
    result = getProjects()
    return {
        'statusCode': 200,
        'body': result
    }

## For local testing
#lambda_handler(None, None)
