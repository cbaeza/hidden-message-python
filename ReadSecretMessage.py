from PIL import Image

class ReadSecretMessage:

    def __init__(self, image_path, end_of_message_token):
      self.image_path = image_path
      self.end_of_message_token = end_of_message_token
      self.hidden_message = ""

    def decode_message(self):
      print(f">>> Decoding message of picture: {self.image_path}")
      image = Image.open(self.image_path)
      pixels = image.load()

      image_size = image.size
      image_width = image_size[0]
      image_height = image_size[1]

      byte = ""

      for x in range(image_width):
         for y in range(image_height):
            pixel = pixels[x,y]
            red = pixel[0]
            green = pixel[1]
            blue  = pixel[2]
            
            byte += self.get_less_sig_bit(self.number_to_binary(red))
            # RED
            if len(byte) >= 8:
               if byte == self.end_of_message_token:
                  break
               self.hidden_message += self.transform(byte)
               byte = ""
            # GREEN
            byte += self.get_less_sig_bit(self.number_to_binary(green))
            if len(byte) >= 8:
               if byte == self.end_of_message_token:
                  break
               self.hidden_message += self.transform(byte)
               byte = ""
            # BLUE
            byte += self.get_less_sig_bit(self.number_to_binary(blue))
            if len(byte) >= 8:
               if byte == self.end_of_message_token:
                  break
               self.hidden_message += self.transform(byte)
               byte = ""  
         else:
            continue
         break
      return self.hidden_message
    
    def transform(self, byte):
       #print(f"Read byte: {byte}")
       dec = self.binary_to_decimal(byte)
       #print(f"Decimal: {dec}")
       ascii = self.number_to_ascii(dec)
       #print(f"Ascii: {ascii}")
       return ascii

    def get_less_sig_bit(self, byte):
       return byte[-1]   
    
    def number_to_binary(self, number):
       return bin(number)[2:].zfill(8)
    
    def binary_to_decimal(self, binary):
       return int(binary, 2)

    def number_to_ascii(self, number):
       return chr(number)