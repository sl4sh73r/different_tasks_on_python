a=input()
print(a[:a.find("h")+1]+a[a.rfind("h")-1:a.find("h"):-1]+a[a.rfind("h"):])
