#!/usr/bin/env python

import requests

repo = "https://github.com/v-codecrux/razorops_python.git"

branch = "master"
spec = """
  
tasks:
  build:
    steps:
      - run: pip install -r requirements.txt -t vendor/pip
      - workspace/persist:
          paths: [.]
  


workflow:
  - name: production
    tasks: 
    - build
"""

response = requests.post("http://localhost:9000/webhook/oss", json={
  "repo": repo,
  "branch": branch,
  "spec": spec,
  "sha": "ec7d3b3a3b9f801b7e1e25b70b6da042dadd7ff3",
  "app": "v-codecrux/razorops_python",
})

print(response)
