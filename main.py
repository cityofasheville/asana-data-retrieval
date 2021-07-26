import asana
import os

# We originally entered the Asana token directly in the client call, but that's a terrible
# idea because it then gets checked into Github and becomes vulnerable. Instead we will 
# take it from the environment. 
# 
# To set the environment variable in Windows, enter the following:
#
#   set ASANA_TOKEN=token-string
#
# (replacing 'token-string' with the actual token)

token = os.getenv('ASANA_TOKEN')
client = asana.Client.access_token(token)

result = client.tasks.get_tasks(fields = ['gid', 'followers', 'assignee.name', 'name', 'custom_fields'], opt_pretty=True, project=1200128036189056)

projects = []
for item in result:
    print(item)
    projects.append(item)
