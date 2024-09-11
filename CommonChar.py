 class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arr = []
        arr1 = []
        arr2 = []
        arr3 = []
        for i in words[0]:
            arr.append(i)

        for a in words[1]:
            arr1.append(a)

        for b in words[2]:
            arr2.append(b)  
    
        for char in arr:
            if char in arr1 and char in arr2:
                arr3.append(char)
                arr1.remove(char)
                arr2.remove(char)

                
        return arr3                  
