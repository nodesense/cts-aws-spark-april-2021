```
EMR Create separate securty group, subnet altogether..
we need to whitelist ips again.. 

check for Security groups for Master in the UI

Click on the Security groups link for master.. and 

inbound rule for ssh for the IP..

you need to use the key which is available with you..


For emr, hadoop is username, not ubuntu..

Copy from Master public DNS or use the UI to copy the command

```

```
ssh -i cts-gopal-key.pem hadoop@ec2-3-20-234-226.us-east-2.compute.amazonaws.com


```

