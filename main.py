import asana

# We originally entered the Asana token here directly, but that's a terrible
# idea because it then gets checked into Github and becomes vulnerable.
client = asana.Client.access_token('ASANA_TOKEN_BAD_BAD_IDEA')

result = client.tasks.get_tasks(fields = ['gid', 'followers', 'assignee.name', 'name', 'custom_fields'], opt_pretty=True, project=1200128036189056)

projects = []
for item in result:
    print(item)
    projects.append(item)
