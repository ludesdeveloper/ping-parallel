# PARALLEL PING SRIPTS 

### **Requirements**

1. Python 3 Installed 

### **Arguments**
This script takes 3 arguments, example:
```
python main.py 192.168.1 c 254
```
1st argument, 192.168.1 is ip prefix

2nd argument, c is class subnet mask

3rd argument, 254 is workers(maximum is 254), for how much concurrency happen at one time
> For worker, i suggest start with 5 first, if you think your pc can handle it, you can increase it **gradually**

### **Class C**
1. Let'say we want to ping 192.168.1.1 - 192.168.1.254
2. Use this command below
```
python main.py 192.168.1 c 254
```

### **Class B**
1. Let'say we want to ping 192.168.1.1 - 192.168.254.254
2. Use this command below
```
python main.py 192.168 b 254
```
### **Class A**
1. Let'say we want to ping 192.1.1.1 - 192.254.254.254
2. Use this command below
```
python main.py 192 a 254
```
