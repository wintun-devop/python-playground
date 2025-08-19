```
create database async_crud;
```
```
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```
```
CREATE TABLE "Product" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    model_no TEXT NOT NULL,
    description TEXT,
    arrival DATE
);
```