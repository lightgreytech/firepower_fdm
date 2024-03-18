# first import the yaml library
import yaml
# second define a yaml file read function
def yaml_load(filename):
    fh = open(filename, "r")
    yamlrawtext = fh.read()
    yamldata = yaml.load(yamlrawtext,Loader=yaml.FullLoader)
    return yamldata

# Then have access to device's items

ftd_host = {}
ftd_host = yaml_load("profile_ftd.yml")    
print(ftd_host["devices"])    
# the following stores into FDM_XXX variables all connexion details of the first device in the dictionary
FDM_USER = ftd_host["devices"][0]['username']
FDM_PASSWORD = ftd_host["devices"][0]['password']
FDM_IP_ADDR = ftd_host["devices"][0]['ipaddr']
FDM_PORT = ftd_host["devices"][0]['port']
FDM_VERSION = ftd_host["devices"][0]['version']
print("===")
print(FDM_USER)
print(FDM_PASSWORD)
print(FDM_IP_ADDR)
print(FDM_PORT)
print(FDM_VERSION)