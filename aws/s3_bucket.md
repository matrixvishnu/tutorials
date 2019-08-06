---
output: pdf_document
fontsize: 11pt
papersize: a6
geometry: margin=0.3cm
---


### S3 bucket: Simple Storage Service
![alt text](Amazon-Simple-Storage-Service-S3@4x.png "S3 Bucket")
A storage space where any type of files can be stored and accessed

#### Creation
- Bucket name must be unique
- A Bucket can not be transferable across accounts
- A Bucket can be cloned from other bucket 

#### Versioning
- By enabling versioning multiple versions of same doc can  be maintained
- Most recent doc will be accessed from any services

#### Server Access Logging:
- To track the logs related to this bucket
- Store the logs in an another bucket

#### Tags
- Cost allocation Tags are used to tag the buckets to track the cost of the buckets
- Tags are KEY VALUES pairs 
- AWS will generate a 'createdBy' tag by default if user doesn't create any tag after creation of the bucket

#### S3storage Class
These are the storage classes for amazon s3

- __*standerd*__ Frequently accessed data
- __*Intelligent-Tiering*__
- This is used for objects access is unpridictable
- This is will have two storage tiers One is optimized for frequently access and one for the infrequent the pricing is different for these tiers
- Based on the objects access patterns object will be between the two tiers
- __*Standerd IA(infreequent access)*__
- For Objects used less frequently but expects rapid access when needed this is used ideally for backups
- __*Standerd One Zone-IA*__
- It is same as Standard IA except the standers IA will stores the object across 3 zones but one-zone IA will be stored in only one zone this is suitable for secondary backups
- __*Glacier*__
- This is used for archival purpose public access is not possible for the objects under glacier
- Glacier provides three retrieval options that range from a few minutes to hours
- __*Glacier Deep Archive*__
- lowest-cost storage class and supports long-term retention and digital preservation for data that may be accessed once or twice in a year. 
- This is ideal solution for data 

