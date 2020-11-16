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

### Owner
```bash
tablename   : owners
```
```bash
row         : INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
id          : VARCHAR(100) NOT NULL
photo       : VARCHAR(100) NULL
full_name   : VARCHAR(50) NOT NULL
address     : VARCHAR(150) NULL
email       : VARCHAR(50) NOT NULL
password    : VARCHAR(100) NOT NULL
create_at   : VARCHAR(30) NULL
update_at   : VARCHAR(30) NULL
ip_address  : VARCHAR(30) NULL
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

### OwnerRegister
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
  message : "Owner with a same email is already exist!",
  data    : null 
}
```

### OwnerLogin
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
  message : "Account is not registered!",
  data    : null 
}
```
###### Response 401
```json5
{
  status  : "Unauthorized",
  message : "Wrong password account!",
  data    : null 
}
```