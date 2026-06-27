class Solution:

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

