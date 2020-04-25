import requests
from os import listdir
from os.path import isfile, join

MISTRAL_URL = "http://mistral-chom-2.sdnoshm05.netcracker.com"

workflow_root_path = "D:\git\workflow-service_mapping\mistral\workflow"
files = [f for f in listdir(workflow_root_path) if isfile(join(workflow_root_path, f))]
print(files)
for file_name in files:
    with open(join(workflow_root_path, file_name), "r") as f:
        content = "".join(f.readlines())
        print(content)
        resp = requests.post(u"%s/v2/workflows" % MISTRAL_URL, data=content)
        print(resp)


