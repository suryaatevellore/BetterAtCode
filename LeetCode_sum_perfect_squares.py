import math
class Solution:
  def find_squares(self, num):
      x = math.sqrt(num)
      z = math.ceil(x)
      if int(x) == z:
          # perfect square
          x = int(x) + 1
      else:
        #not a perfect square
        x = z
      ps = {i*i for i in range(1, x)}
      return ps
  
  def find_min(self, ps, y, i):
      # print(f"min bound array is {ps}")
      ps.reverse()
      x = [a for a in ps if a<=y]
      if not x:
          return 1
      return max(x)

  def recurse_num(self, ps, n, i, num):
      if i!=1 and n%i==0:
          return n // i
      # breakpoint()
      if n in ps:
          # print(f"{n} found in {ps}")
          num+=1
          return num
      y = n - i
      # print(f"{n} reduced to {y}")
      num+=1
      if y in ps:
          num += 1
          return num   
      
      temp = []
      temp.append(i)
      while(y>0):
        c = self.find_min(list(ps), y, i)
        # print(f"min element found was {c}")
        temp.append(c)
        y = y-c
        num+=1
      print(f"summation for {i} is {temp}")
      return num
      
  def numSquares(self, n: int) -> int:
      if n == 0:
          return 0
      all_nums = []
      perfect_squares = self.find_squares(n)  
      for i in perfect_squares:
          print(f"testing for i= {i}")
          print(f"perfect squares is {perfect_squares}")
          num = self.recurse_num(perfect_squares, n, i, 0)
          print(f"num for {i} is {num}")
          all_nums.append(num)
      print(f"all nums = {all_nums}")
      return min(all_nums)
      

s = Solution()
y = s.numSquares(96)
print(y)

