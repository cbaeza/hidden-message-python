from WriteSecretMessage import WriteSecretMessage
from ReadSecretMessage import ReadSecretMessage

end_of_message_token = [1, 1, 1, 1, 1, 1, 1, 1] # dec 255 => ÿ
secret_message = "Greeting from Germany!"
m = WriteSecretMessage(secret_message, "Igel.png","Igel2.png", end_of_message_token)
m.hidde_message_in_picture()

concat = ''.join(map(str, end_of_message_token))
p = ReadSecretMessage("Igel2.png", concat )
print(f">>> Hidden message: {p.decode_message()}")
