# Check year function - returns true/false if year is in range
def yearCheck(year):
  return 0 < year <= 9999
  
# Leap year check function - called in dayMonthCheck function
def leapYear(year):
  # below is the formula for a leap year
  if (year%4==0) and (year%100 !=0 or year%400 == 0): 
    return True
  else:
    return False

# function thats check validity of day and month
def dayMonthCheck( day, month, year):
  leap = leapYear(year) # check for leap year
  monthList1 = [1,3,5,7,8,10,12] ## months with 31 days
  monthList2 = [4,6,9,11] ## months with 30 days
  monthList3 = 2 ## month with 28 or 29 days. ie feb
  
  if month in monthList1: # check valid day for list1
    if day >=1 and day <= 31: 
        return True
    else:
        return False
  elif month in monthList2: #check valid day for list2
          if day >= 1 and day <= 30: 
              return True
          else:
              return False
  elif month == monthList3 and leap == False: ## check valid day if feb and not a leap year
      if day >=1 and day <= 28: ## 
          return True
      else:
          return False
  elif month == monthList3 and leap == True: # check valid day if feb and leap year is true
      if day >=1 and day <= 29: 
          return True
      else:
          return False
  else:
    # return false here - as it cannot be a valid month if not in any list
    return False
    
# final validateDate function which simply calls other helper functions 
def validateDate(dd=31, mm=1, yyyy=1900):
  year = yearCheck(yyyy) # check year
  dayMonth = dayMonthCheck(dd, mm, yyyy) # check day/month
  if year and dayMonth == True: # if values are true is valid
    return True
  else: # else it is not a valid date
    return False
  
print(validateDate()) # True

print(validateDate(31, 4, 1999)) # False

print(validateDate(29, 2, 1900)) # False

print(validateDate(29, 2, 2020)) # True

print(validateDate(mm=6)) # False

print(validateDate(mm=6, dd=0)) # False

print(validateDate(yyyy=10001)) # False


