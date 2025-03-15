## uuidv4 custom function
```
CREATE FUNCTION `UUIDV4` () RETURNS VARCHAR(255) NOT DETERMINISTIC NO SQL SQL SECURITY INVOKER
RETURN LOWER(
    CONCAT(
        # 1th and 2nd block are made of 6 random bytes
        HEX(RANDOM_BYTES(4)),
        '-',
        HEX(RANDOM_BYTES(2)),
        # 3th block will start with a 4 indicating the version, remaining is random
        '-4',
        SUBSTR(HEX(RANDOM_BYTES(2)), 2, 3),
        '-',
        # 4th block first nibble can only be 8, 9 A or B, remaining is random
        CONCAT(
            HEX(FLOOR(ASCII(RANDOM_BYTES(1)) / 64) + 8),
            SUBSTR(HEX(RANDOM_BYTES(2)), 2, 3)
        ),
        '-',
        # 5th block is made of 6 random bytes
        HEX(RANDOM_BYTES(6))
    )
);
```

### Database Table Creation
```
CREATE TABLE products (
id  CHAR(36) NOT NULL,
name text NOT NULL,
model_no varchar(255) NOT NULL UNIQUE,
description text NOT NULL,
arrival varchar(255) NOT NULL,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(id)
);
```
### Insert Testing
```
INSERT INTO product (id,name,model_no,description,arrival) VALUES (uuidv4(),'Mikrotik L009UiGS-RM','L009UiGS-RM','L009 is more than just a router.','1/2/2012');
```