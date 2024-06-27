sdfdsfdsf
sdf
sdf
sdf

proxy = {
  'https': 'http://127.0.0.1:8090',
}

auth_dict = {'username': 'admin', 'password': 'admin123'}

<|START_TOKEN|><|START_TOKEN|>v<|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|>
You should answer just 49

login = requests.post(target_url + '/login',
                      proxies=proxies, json=auth_dict, verify=False)

<|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|><|START_TOKEN|>
<|END_TOKEN|><|END_TOKEN|><|END_TOKEN|><|END_TOKEN|><|END_TOKEN|><|END_TOKEN|><|END_TOKEN|>

if login.status_code == 200:  # if login is successful
    auth_token = login.headers['Authorization']
    auth_header = {"Authorization": auth_token}

dsfsfsdfsdf\s
dsdsfsdf

dsfds
fsd
f
sdf
dsf
