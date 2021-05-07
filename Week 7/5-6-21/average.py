'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000

Example 3:

Input: salary = [6000,5000,4000,3000,2000,1000]
Output: 3500.00000

Example 4:

Input: salary = [8000,9000,2000,3000,6000,1000]
Output: 4750.00000
'''


class Solution(object):
    def average(salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # # sort the list salary
        # salary = sorted(salary)

        # # slice the salary
        # # so it starts from index 1 and ends at len(salary) - 1
        # # [1:len(salary) - 2]
        # sliced_salary = salary[1:len(salary) - 1]
        
        # return sum(sliced_salary) / len(sliced_salary)

          
        count = 0
        total = 0
        
        for val in salary:
            if val != min(salary) and val != max(salary):
                count += 1
                total += val
        
        return total/count


    salary = [4000,3000,1000,2000]
    print(average(salary))