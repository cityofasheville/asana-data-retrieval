import asana
import json
import os
def getProjects():
    token = os.getenv('ASANA_TOKEN')
    print(token)
    client = asana.Client.access_token(token)

    result = client.tasks.get_tasks(fields = ['gid', 'followers', 'assignee.name', 'name', 'notes', 'custom_fields', 'completed_at', 'memberships.section.name'], opt_pretty=True, project=1200128036189056)

    #print(result)
    projects = []
    for item in result:
        project = {}
        project['Name'] = item['name']
        project['Notes'] = item['notes']
        project['Completed At'] = item['completed_at']
        project['Assignee'] = None
        if item['assignee'] != None:
            project['Assignee'] = item['assignee']['name']
        project['Section/Column'] = None
        if len(item['memberships']) > 0:
            project['Section/Column'] = item['memberships'][0]['section']['name']
        project['Importance'] = None
        project['Status'] = None
        if len(item['custom_fields']) > 0:
            for fld in item['custom_fields']:
                if fld['name'] == 'Importance':
                    project['Importance'] = fld['display_value']
                if fld['name'] == 'Status':
                    project['Status'] = fld['display_value']
        projects.append(project)
       # projects.append(item)
    return projects

def lambda_handler (event, context):
    projects = getProjects()
    print(len(projects))
    count = 0
    for project in projects:
       # print(json.dumps(project))
        count = count + 1
        if count > 20:
            break
    return {
        'statusCode': 200,
        'body': projects
    }

## For local testing
lambda_handler(None, None)
