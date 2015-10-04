# Download API data from
# http://sahko.hylly.org/
# Depends on requests library
from requests import get
import json

API_URL = "http://sahko.hylly.org/api/"

# Municipalities
municps_req = get(API_URL + "historia/kunnat")
municps = json.loads(municps_req.content)
print("Got %s municipalities" % len(municps))

municipality_data = {}
for m in municps:
    print("Getting " + m)
    r = get(API_URL + "historia/kunnat/" + m)
    rdata = json.loads(r.content)
    municipality_data[m] = rdata

with open("municipalities.json", "w") as f:
    f.write(json.dumps(municipality_data))


# Returns only empty data.. ######################
# companies_req = get(API_URL + "historia/yhtiot")
# companies = json.loads(companies_req.content)
# print("Got %s companies" % len(companies))

# company_data = {}
# for c in companies:
#     print("Getting " + c)
#     r = get(API_URL + "historia/yhtiot/" + c)
#     rdata = json.loads(r.content)
#     company_data[c] = rdata

# with open("companies.json", "w") as f:
#     f.write(json.dumps(company_data))
