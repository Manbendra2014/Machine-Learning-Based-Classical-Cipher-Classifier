# Machine Learning Based Classical Cipher Classifier

## Overview

<p align="justify">This project aims to build a machine learning based classifier to distinguish between various classical ciphers. Classical ciphers are historical encryption techniques that perform simple substitution or transposition on plaintext to produce ciphertext. By training a machine learning model on labeled examples of ciphertexts from different ciphers, the classifier can predict the cipher used to encrypt an unseen ciphertext.</p>

## Classical Ciphers

### Group 1 : Substitution Ciphers

#### 1. Playfair Cipher

#### 2. Polybius Square Cipher


#### 3. Baconian Cipher

#### 4. Atbash Cipher

### Group 2 : Transposition Ciphers

#### 5. Columnar Transposition Cipher

#### 6. Scytale Cipher

#### 7. Rail Fence Cipher

#### 8. Caesar Cipher

### Group 3 : Advanced Ciphers

#### 9. Hill Cipher

#### 10. Affine Cipher

#### 11. Vigenère Cipher

#### 12. Gronsfeld Cipher

## Dataset Preparation
## Machine Learning Model
## Model Evaluation
## Working of Each Cipher

### Group 1 : Substitution Ciphers

#### 1. Playfair Cipher

- **Key :** <p align="justify">The Playfair Cipher requires a keyword to construct the Playfair Square matrix. The keyword should be unique, with no duplicate letters, and is used to generate the matrix.</p>
- **Encryption :** <p align="justify">The plaintext must be processed in pairs of two letters. If there is an odd number of letters, a dummy letter (like 'X') is added at the end. The encryption process involves finding the positions of the pair in the Playfair Square and applying specific rules to determine the ciphertext.</p>
- **Decryption :** <p align="justify">The decryption process is similar to encryption, but it involves reversing the rules used during encryption to find the original plaintext.</p>

#### 2. Polybius Square Cipher

- **Key :** <p align="justify">The Polybius Square Cipher does not use a traditional key like other ciphers. Instead, it relies on the fixed 5x5 matrix (Polybius Square) where each letter of the alphabet corresponds to a unique row and column position.</p>
- **Encryption :** <p align="justify">The plaintext is converted into its numerical representation based on the row and column positions in the Polybius Square. The numerical values are then concatenated to form the ciphertext.</p>
- **Decryption :** <p align="justify">Decryption requires a knowledge of the Polybius Square to reverse the process and find the original plaintext.</p>

#### 3. Baconian Cipher

- **Key :** <p align="justify">The Baconian Cipher uses a fixed 5-letter alphabet (A and B) to represent each letter of the English alphabet. There is no additional key required for the encryption or decryption process.</p>
- **Encryption :** <p align="justify">Each letter in the plaintext is converted into its corresponding Baconian representation based on the 5-letter alphabet. The resulting binary sequence forms the ciphertext.</p>
- **Decryption :** <p align="justify">Decryption involves reversing the process by converting the binary sequence back to plaintext based on the Baconian alphabet.</p>

#### 4. Atbash Cipher

- **Key :** <p align="justify">The Atbash Cipher does not require a key for encryption or decryption. The substitution pattern is fixed and remains the same for all messages.</p>
- **Encryption :** <p align="justify">Each letter in the plaintext is replaced by its reverse in the alphabet. For example, 'A' becomes 'Z,' 'B' becomes 'Y,' and so on.</p>
- **Decryption :** <p align="justify">The decryption process is the same as encryption since the substitution pattern is fixed.</p>

### Group 2 : Transposition Ciphers

#### 5. Columnar Transposition Cipher

- **Key :** <p align="justify">The Columnar Transposition Cipher requires a keyword to determine the column order during encryption and decryption. The keyword should contain unique letters with no duplicates.</p>
- **Encryption :** <p align="justify">The plaintext is written in rows under the keyword, and then the columns are rearranged based on the alphabetical order of the letters in the keyword. The ciphertext is read column by column to generate the encrypted message.</p>
- **Decryption :** <p align="justify">Decryption involves rearranging the columns based on the original keyword to obtain the original plaintext.</p>

#### 6. Scytale Cipher

- **Key :** <p align="justify">The Scytale Cipher uses a cylindrical device called a "scytale" as its key. The scytale has a specific circumference that determines the number of letters to be written on each turn during encryption and decryption.</p>
- **Encryption :** <p align="justify">The plaintext is written lengthwise along the scytale, and the ciphertext is read off the cylinder in a spiral pattern to produce the encrypted message.</p>
- **Decryption :** <p align="justify">To decrypt, the scytale must have the same circumference as used during encryption. The ciphertext is wrapped around the scytale, and the plaintext is read off in a straight line to reveal the original message.</p>

#### 7. Rail Fence Cipher

- **Key :** <p align="justify">The Rail Fence Cipher requires the number of "rails" or rows as its key, which determines the height of the zigzag pattern.</p>
- **Encryption :** <p align="justify">The plaintext is written diagonally along the rails, and then the ciphertext is read off row by row to produce the encrypted message.</p>
- **Decryption :** <p align="justify">Decryption involves recreating the zigzag pattern by placing the ciphertext letters in the appropriate rails, and then reading the plaintext off diagonally.</p>

#### 8. Caesar Cipher

- **Key :** <p align="justify">The Caesar Cipher requires a fixed integer value (key) that determines the shift for encryption and decryption. The key value represents the number of positions each letter is shifted down the alphabet.</p>
- **Encryption :** <p align="justify">Each letter in the plaintext is shifted down the alphabet by the key value to produce the ciphertext. For example, with a shift of 3, 'A' becomes 'D,' 'B' becomes 'E,' and so on.</p>
- **Decryption :** <p align="justify">Decryption involves shifting each letter in the ciphertext up the alphabet by the negative key value to reveal the original plaintext.</p>

### Group 3 : Advanced Ciphers

#### 9. Hill Cipher

- **Key :** <p align="justify">The Hill Cipher requires a square matrix called the encryption key matrix. The matrix must be invertible to allow for decryption.</p>
- **Encryption :** <p align="justify">The plaintext is divided into blocks of letters, each represented as a matrix. Encryption involves multiplying each matrix with the encryption key matrix to produce the ciphertext matrix.</p>
- **Decryption :** <p align="justify">To decrypt, the ciphertext matrix is multiplied by the inverse of the encryption key matrix to obtain the original plaintext matrix, which is then converted back to text.</p>

#### 10. Affine Cipher

- **Key :** <p align="justify">The Affine Cipher requires two numeric keys, 'a' and 'b,' with 'a' being coprime with 26 (the number of letters in the English alphabet). The key 'a' determines the multiplication factor, and 'b' determines the shift value for encryption and decryption.</p>
- **Encryption :** <p align="justify">Each letter in the plaintext is first converted to a numerical value. Encryption involves applying the mathematical operation: ciphertext = (a * plaintext + b) % 26, where '%' represents the modulo operation.</p>
- **Decryption :** <p align="justify">Decryption requires finding the modular inverse of 'a,' which allows for the reverse operation to find the original plaintext.</p>

#### 11. Vigenère Cipher

- **Key :** <p align="justify">The Vigenère Cipher uses a keyword that is repeated as many times as needed to match the length of the plaintext. The letters of the keyword determine the letter shift for each corresponding letter in the plaintext.</p>
- **Encryption :** <p align="justify">Each letter in the plaintext is shifted based on the corresponding letter in the keyword to generate the ciphertext.</p>
- **Decryption :** <p align="justify">Decryption involves finding the letters of the keyword needed to reverse the shifts and obtain the original plaintext.</p>

#### 12. Gronsfeld Cipher

- **Key :** <p align="justify">The Gronsfeld Cipher requires a numeric key, similar to the Vigenère Cipher. The key is repeated as needed to match the length of the plaintext, and each numeric value determines the letter shift for the corresponding letter in the plaintext.</p>
- **Encryption :** <p align="justify">Each letter in the plaintext is shifted based on the corresponding numeric value in the key to generate the ciphertext.</p>
- **Decryption :** <p align="justify">Decryption involves finding the numeric values of the key needed to reverse the shifts and obtain the original plaintext.</p>

## Conclusion

<p align="justify">Leveraging machine learning to train a classifier on labeled datasets of ciphertexts encrypted with classical ciphers offers a powerful tool for identifying the encryption technique applied to unseen ciphertexts. This classifier can play a vital role in analyzing and deciphering encrypted messages, thereby offering valuable insights into historical encryption methods and their respective strengths in ensuring security. Understanding classical ciphers not only allows us to marvel at the brilliance of historical cryptographers but also lays a strong foundation for comprehending and developing modern cryptographic techniques that are essential for safeguarding computer security and protecting sensitive data in today's digital age.</p>
