class Solution:
    def isAlphanumeric(self, char: str) -> bool:
        if chr(48) <= char <= chr(57) or chr(65) <= char <=  chr(90) or chr(97) <= char <= chr(122):
            return True
        else:
            return False 

    def isPalindrome(self, s: str) -> bool:
        begInd = 0
        endInd = len(s) - 1
        while begInd < endInd:
            while begInd < endInd and not s[begInd].isalnum():
                begInd += 1
            while begInd < endInd and not s[endInd].isalnum():
                endInd -= 1
            if s[begInd].lower() != s[endInd].lower():
                return False
            begInd += 1
            endInd -= 1

        return True


a = Solution()
mys = 'A man, a plan, a canal: Panama'
mys = '.,'

print(a.isPalindrome(mys))
# print (a.toUpper(mys[2]))

    # while p1 < p2 
    # p1 skipNonalpha
    # p2 skipNonalpha

    # if p1 == p2 
    #   continue 
    # else return false 

 # 
# print("A")     