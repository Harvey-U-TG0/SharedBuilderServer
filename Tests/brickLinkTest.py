import requests
import ast
from requests_oauthlib import OAuth1

import sys
sys.path.append('/Users/harveyu/GitHub/SharedBuilderServer/SecureData')
from privateKeys import Keys

brickLinkBaseURL = "https://api.bricklink.com/api/store/v1"

auth = Keys.brickLinkAuth


response = requests.get(brickLinkBaseURL + "/items/part/3001old/price", auth=auth)

data = response.json()
#dictionary = ast.literal_eval(data)

print(data['data']['avg_price'])


