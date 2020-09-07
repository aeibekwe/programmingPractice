# necessary imports
import requests
from requests.auth import HTTPBasicAuth


# for username && password
def get_username():
  print('Enter Username: ')
  username = input('')
  return str(username)

def get_password():
  print('Enter Password: ')
  password = input('')
  return str(password)

# put the authentication info together
auth = HTTPBasicAuth(get_username(), get_password())

# input authentication info and log in to BlackBoard using requests
r = requests.get('https://login.usc.edu/login/login?spEntityID=https://shibboleth.usc.edu/idp/sp&service=&goto=https://login.usc.edu/sso/SSORedirect/metaAlias/USCRealm/idp?ReqID%3D_cd10a0c9f6b7fce24b61ba9f06d02e91%26index%3Dnull%26acsURL%3Dhttps://shibboleth.usc.edu/idp/sp/Shibboleth.sso/SAML2/POST%26spEntityID%3Dhttps://shibboleth.usc.edu/idp/sp%26binding%3Durn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST', auth)
if r.status_code == requests.codes.ok:
  print(r.headers['content-type'])

#verbs = requests.options(r.url)
#verbs.status_code



