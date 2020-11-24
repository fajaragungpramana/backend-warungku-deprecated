# API SPEC
This is REST API warungku.

### Author
```bash
Author      : Fajar Agung Pramana
Created At  : 14 November 2020
Location    : Indonesia
```

### Information
```bash
Url         : https://implizstudio.com/warungku/
Key Owner   : ba674290781901e3b093eabdc0a186b51477598a565d8cf840da22276c344b51
```

# Database SPEC
This is database schema

### Owners
```bash
tablename   : owners
```
```bash
row         : INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
id          : VARCHAR(100) NOT NULL
photo       : VARCHAR(100) NULL
full_name   : VARCHAR(50) NOT NULL
address     : VARCHAR(150) NULL
store       : RELATIONSHIP STORES
email       : VARCHAR(50) NOT NULL
password    : VARCHAR(100) NOT NULL
create_at   : VARCHAR(30) NULL
update_at   : VARCHAR(30) NULL
ip_address  : VARCHAR(30) NULL
```

### Stores
```bash
tablename   : stores
```
```bash
row         : INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
owner_id    : VARCHAR(100) NOT NULL FOREIGN KEY OWNERS (ID)
name        : VARCHAR(50) NOT NULL
address     : VARCHAR(150) NULL 
latitude    : VARCHAR(30) NULL
longitude   : VARCHAR(30) NULL
```

### Verifications
```bash
table       : verifications
```
```bash
row         : INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
owner_id    : VARCHAR(100) NOT NULL FOREIGN KEY OWNERS (ID)
name        : VARCHAR(50) NOT NULL
account     : VARCHAR(30) NOT NULL
email       : BOOLEAN NOT NULL
phone       : BOOLEAN NOT NULL
code        : INTEGER
```

# EndPoint SPEC
This is endpoint api

### Global
This is global response all endpoint can show it

###### Response 403
```json5
{
  status  : "Forbidden",
  message : "Invalid api key!",
  data    : null 
}
```

###### Response 500
```json5
{
  status  : "Internal Server Error",
  message : "Something wrong. Please, try again!",
  data    : null 
}
```

### OwnerRegister [POST]
<b>owner/auth/register</b>. This endpoint provide user to registration owner account
###### Header
```bash
access_key_owner    : Key Owner 
```
###### Body
```bash
full_name   : String
store_name  : String
email       : String
password    : String
```
###### Response 201
```json5
{
  status  : "Created",
  message : "Owner account has been created!",
  data    : {
     id: "db338f42-365c-4711-87d2-1ad2bb4c2642"               
  }
}
```
###### Response 400
```json5
{
  status  : "Bad Request",
  message : "Fill all the request body!",
  data    : null 
}
```
###### Response 406
```json5
{
  status  : "Not Acceptable",
  message : "Owner with a same email is already exist!",
  data    : null 
}
```

### OwnerLogin [POST]
<b>owner/auth/login</b>. This endpoint provide user to login owner account

###### Header
```bash
access_key_owner    : Key Owner
```
###### Body
```bash
email       : String
password    : String
```
###### Response 200
```json5
{
  status  : "OK",
  message : "Owner login success!",
  data    : {
     id: "db338f42-365c-4711-87d2-1ad2bb4c2642"               
  } 
}
```
###### Response 400
```json5
{
  status  : "Bad Request",
  message : "Fill all the request body!",
  data    : null 
}
```
###### Response 404
```json5
{
  status  : "Not Found",
  message : "Account is not registered!",
  data    : null 
}

```
###### Response 406
```json5
{
  status  : "Not Acceptable",
  message : "Wrong password!",
  data    : null 
}
```
###### Response 202
```json5
{
  status  : "Accepted",
  message : "Owner login success, but account not verified!",
  data    : {
     id: "db338f42-365c-4711-87d2-1ad2bb4c2642"               
  }
}
```

### OwnerVerificationCode [GET]
<b>owner/auth/code</b>. This endpoint to sent code verification to owner account 

###### Header
```bash
access_key_owner    : Key Owner
```
###### Body
```bash
account_id          : String
account_email       : String
```
###### Response 200
```json5
{
  status  : "OK",
  message : "Code verification has been sent!",
  data    : {
     access_token  : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDU1ODU2MDAsIm5iZiI6MTYwNTU4NTYwMCwianRpIjoiMGU0NzBlMWItYmUxZS00NmJkLWI3MDEtMmQ2ZWRhNjk2M2M5IiwiZXhwIjoxNjA1NTg1NjYwLCJpZGVudGl0eSI6WyJmMDRmYWM1Ny0yZjMxLTRhZmMtOTViYi0wYmI1YTZkYWM3YmEiXSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.QR3-t3oeoDUt58da6o1Ce8F--5-3upi90wkINrcYb-I",
     expired       : "1 Minutes"                
  } 
}
```
###### Response 400
```json5
{
  status  : "Bad Request",
  message : "Fill all the request body!",
  data    : null
}
```
###### Response 404
```json5
{
  status  : "Not Found",
  message : "Account id not found!",
  data    : null 
}
```

### OwnerVerificationAccount [POST]
<b>owner/auth/verification</b>. This endpoint to verify owner account 

###### Header
```bash
access_key_owner    : Key Owner
Authorization       : access_token
```
###### Body
```bash
account_id          : String
account_code        : Int        
```
###### Response 200
```json5
{
  status  : "OK",
  message : "Account verification success!",
  data    : null
}
```
###### Response 400
```json5
{
  status  : "Bad Request",
  message : "Fill all the request body!",
  data    : null
}
```
###### Response 406
```json5
{
  status  : "Not Acceptable",
  message : "Wrong verification code!",
  data    : null 
}
```
