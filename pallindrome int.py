#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    reversed_n = 0
	    while n > 0:
	        digit = n % 10  # Get the last digit
	        reversed_n = reversed_n * 10 + digit  # Build the reversed number
	        n //= 10  # Remove the last digit
        return reversed_n
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.is_palindrome(n)
        print(ans)

        print("~")

# } Driver Code Ends