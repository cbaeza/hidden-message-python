from PIL import Image
import math

class WriteSecretMessage:

    def __init__(self, message, image_path, output_path, end_of_message_token):
        print(f">>> WriteSecretMessage! '{message}' in picture: {image_path}")
        self.message = message
        self.image_path = image_path
        self.output_path = output_path
        self.end_of_message_token = end_of_message_token

    def hidde_message_in_picture(self):    
        image = Image.open(self.image_path)
        pixels = image.load()

        image_size = image.size
        image_width = image_size[0]
        image_height = image_size[1]
        counter = 0
        print(f"Image size: {image_size}")
        message_list = self.get_list_of_bits(self.message)
        message_len = len(message_list)
        print(f"Message len: {message_len}")

        for x in range(image_width):
            for y in range(image_height):
                if counter < message_len:
                    pixel = pixels[x,y]
                    #print(pixel)
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    #print(f"Red: {red}, Green: {green}, Blue: {blue}")
                    # RED
                    if counter < message_len:
                        red_modified = self.modify_color(red, message_list[counter])
                        counter += 1
                    else:
                        red_modified = red   
                    # GREEN
                    if counter < message_len:
                        green_modified = self.modify_color(green, message_list[counter])
                        counter += 1
                    else:
                        green_modified = green;   
                    # BLUE
                    if counter < message_len:
                        blue_modified = self.modify_color(blue, message_list[counter])
                        counter += 1
                    else:
                        blue_modified = blue

                    pixels[x, y] = (red_modified, green_modified, blue_modified)
                    print(f">>> Counter: {counter}")
                    print(f">>> Image len: {len(message_list)}")
    
                else:
                    break
    
            else:
                continue
            break
        if counter >= message_len:
            print("The message has been written correctly!")
        else:
            print(f"Warning: the messagen is not written completely. Still to write {math.floor((message_len - counter) / 8)} characters")

        image.save(self.output_path)


    def get_ascii_representation(self,character):
        return ord(character)
    
    def get_binary_representation(self, number):
        return bin(number)[2:].zfill(8)
    
    def change_last_bit(self, byte, bit_replacement):
        return byte[:-1] + str(bit_replacement)
    
    def binary_to_decimal(self, binary):
        return int(binary,2)

    def get_list_of_bits(self, text):
        list = []
        for letter in text:
            ascii_rep = self.get_ascii_representation(letter)
            binary_rep = self.get_binary_representation(ascii_rep)
            for bit in binary_rep:
                list.append(bit)
        # add end of message
        for bit in self.end_of_message_token:
            list.append(bit)

        return list
    
    def modify_color(self, original_color, bit):
        print(f"Bit: {bit}")
        binary_color = self.get_binary_representation(original_color)
        print(f"binary_color: {binary_color}") 
        modified_color = self.change_last_bit(binary_color, bit)
        print(f"modified_color: {modified_color}")
        dec = self.binary_to_decimal(modified_color)
        print(f"dec: {dec}")
        return dec
