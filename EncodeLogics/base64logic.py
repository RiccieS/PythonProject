import base64

class Logic:
    def __init__(self):
        self.text = ""
        self.private_key = ""
        self.result = ""
        self.name = "Base64"

    def encode(self):
        '''Uses transform method to shift character value and then encode it using base64'''
        def transform(key, message):
            enc = []
            # Iterate through each character in the message
            for i in range(len(message)):
                # Get the corresponding key character for the current message character
                key_c = key[i%len(key)]
                # Perform the encoding transformation and add the result to the list of encoded characters
                enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
            # Encode the list of encoded characters using base64 and return the result
            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        # Perform the encoding transformation using the private key and message text and store the result
        self.result = transform(self.private_key, self.text)

    def decode(self):
        '''Uses transform method to shift character value back and then decode it using base64'''
        def transform(key, message):
            dec = []
            # Decode the message using base64
            message = base64.urlsafe_b64decode(message).decode()
            # Iterate through each character in the decoded message
            for i in range(len(message)):
                # Get the corresponding key character for the current message character
                key_c = key[i % len(key)]
                # Perform the decoding transformation and add the result to the list of decoded characters
                dec.append(chr((256 + ord (message[i]) - ord(key_c)) % 256))
            # Return the list of decoded characters as a string
            return "".join(dec)

        # Perform the decoding transformation using the private key and message text and store the result
        self.result = transform(self.private_key, self.text)
