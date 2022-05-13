from requests import post

print("Input the ip address you would want to track:")
ipask = input("")

response = post("http://ip-api.com/batch", json=[
  {"query": ipask}
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")

input("Press any key to quit ...")