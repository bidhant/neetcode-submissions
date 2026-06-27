class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for character in strs: 
            character_length = str(len(encoded_string))
            encoded_string +=  character_length + "#" + character
        return encoded_string


    def decode(self, s: str) -> List[str]:
        # s = 5#hello5#world
        decoded_string = []
        i=0
        while i < len(strs):
            while j != "#":
                j += 1
            character_length = s[i:j]

            start = j+1
            end = start + character_length
            decoded_string.append(s[start:end])

            i = end
        
        return decoded_string
            





















    

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs: 
            length_of_word = str(len(word))
            encoded_string += length_of_word + "#" + word
        
        return (encoded_string)

    def decode(self, s: str) -> List[str]:
        # s = 4#hello 4#world

        result = []
        i= 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            length_of_word = int(s[i:j])
            
            result.append(s[j+1: j + length_of_word + 1])
            i =  j + 1 + length_of_word 

        return result

