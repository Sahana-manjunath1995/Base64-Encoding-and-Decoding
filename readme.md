# Encoding and decoding of characters using base62

The main goal of this project is to encode the given input and provide decoded characters as output.

Base64 encoding converts the binary data into text format, which is passed through communication channel where a user can handle text safely. Base64 is also called as Privacy enhanced Electronic mail (PEM) and is primarily used in email encryption process.

## Following steps are involved in encoding  of characters

### Step 1
Iterate the characters in the string and convert each of the characters into unicode values.

### Step 2
Convert the  unicode values into binary numbers and store them in list as 8 bits.

### Step 3
Group the binary list numbers into 6 bits with the help of slicing and store them in bits list

### Step 4
Convert the above binary number into decimal number

### Step 5
Convert the decimal numbers into base64 characters

## Following steps are involved in decoding  of characters

### Step 1
Iterate the encoded characters, find their index and store them as decimal numbers in the list

### Step 2
Iterate the decimal number list and convert them into binary, store them as 8 bits in the list.

### Step 3
Truncate the bits by using slicing and store them in bits list.

### Step 4
Group the binary list numbers into 8 bits with the help of slicing.

### Step 5
Convert binary number into decimal and store them in list.

### Step 6
Iterate the decimal number list and convert each of the element into character using chr() function and store them as string.

One common application of Base64 encoding on the web is to encode binary data so it can be included in a URL.




