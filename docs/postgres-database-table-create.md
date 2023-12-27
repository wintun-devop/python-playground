### Installing uuid extension
```
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```
### Database Table Creation
```
CREATE TABLE "Product" (
id uuid DEFAULT uuid_generate_v4(),
name text not null,
model_no text not null unique,
description text not null,
arrival text not null
);
```

### Insert Testing
```
INSERT INTO "Product" (name,model_no,description,arrival) VALUES ('Mikrotik L009UiGS-RM','L009UiGS-RM','L009 is more than just a router.','1/2/2012');
```

### Truncate Table
```
TRUNCATE TABLE table_name;
```