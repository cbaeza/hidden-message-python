# Steganography: Hidden message in PNG images.

The project aim to be used for educational purposes. 
The following tool hide a message into a PNG image. The produces of the message can hidde the message using **WriteSecretMessage.py**. The receptor of the image can read the hidden message using the **ReadSecretMessage.py**.

## LSB (Least Significant Bit) Substitution
You can hidde a secret message using the least significant bits.
The technique is called Steganography and can be applied to both grayscale and color images. In color images, channels like Red, Green, and Blue (RGB) can be used independently or jointly to hide information.
This technique used in the code involve modify the values of the first color channels to encode the hidden data.

# Usage
Given a input image in PNG format like this example:

![Igel](Igel.png)

Encoding a message 

    from WriteSecretMessage import WriteSecretMessage
    from ReadSecretMessage import ReadSecretMessage

    end_of_message_token = [1, 1, 1, 1, 1, 1, 1, 1] # dec 255 => ÿ
    secret_message = "Greeting from Germany!"
    m = WriteSecretMessage(secret_message, "Igel.png","Igel2.png", end_of_message_token)
    m.hidde_message_in_picture()

The code produces the output image (Igel2.png) which is apparently the same as the original image (Idel.png). The technique 
make the changes indetectable to the human eyes.

The image produced with the hidden message is the following:  

![Igel](Igel2.png)

Decoding the message

    concat = ''.join(map(str, end_of_message_token))
    p = ReadSecretMessage("Igel2.png", concat )
    print(f">>> Hidden message: {p.decode_message()}")

The end of message token is used to indicate the end of message and also is used to detect and finish the decoding process.

Run the code

    $ python3 main.py
    
Have fun !