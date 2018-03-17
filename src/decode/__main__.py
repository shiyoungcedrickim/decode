# -*- coding:utf8 -*-
# https://github.com/dialogflow/dialogflow-python-client/blob/master/examples/send_text_example.py
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# ========================================================================
# 
# All extra code
# Copyright 2018 Shiyoung Cedric Kim.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
def drun(cmd=input("> ")):
    request.query = cmd
    response = request.getresponse()
    print(subprocess.check_output(response.read(), shell=True))
def main(args=None):
    if args is None:
        args = " ".join(str(s) for s in sys.argv[1:])
        argsraw = args.split(" ")
        argst = " ".join(str(s) for s in argsraw[1:])
    import sys
    import subprocess.check_output
    if args == "":
        import os.path
        import uuid.uuid4
        try:
            import apiai
        except ImportError:
            sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
            import apiai
        while true:
            drun()
    elif argsraw[0] == "run":
        drun(argst)
    elif argsraw[0] == "file":
        dfile = open(argst, "r")
        drun(dfile.read().replace("\n", " && "))
        dfile.close()
request = apiai.ApiAI("67c4e73769d2498ca8ac6f7573a36845").text_request()
request.lang = "en"
request.session_id = uuid.uuid4()
if __name__ == "__main__":
    main()