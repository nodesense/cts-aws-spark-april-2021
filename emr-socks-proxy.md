
gitbash / windows

```

cd c:

cd keys

ssh -i mykeypair.pem -N -D 8157 hadoop@ec2-###-##-##-###.compute-1.amazonaws.com

```

```
in firefox, add foxyproxy plugin ,  google and go the page, "add to firefox"

Patterns: configuraing proxy that if user visit this pages, use proxy 

 *ec2*.amazonaws.com* 
 *10*.amazonaws.com* 
 
```


Now try to copy jupyter url 

https://ec2-xx-yy-zzz-aaa.us-east-2.compute.amazonaws.com:9443/hub/login?next=%2Fhub%2F

jupyter username: jovyan
password: jupyter
