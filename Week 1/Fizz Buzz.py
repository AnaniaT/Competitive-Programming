class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      ans = []
      for q in range(n):
        q = q + 1
        if not q % 15: ans.append('FizzBuzz')
        elif not q % 5: ans.append('Buzz')
        elif not q % 3: ans.append('Fizz')
        else: ans.append(str(q))
      
      return ans
