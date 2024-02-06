

def Is_Leap_Year(year):
      """determines if year is leap year

      Inputs: an integer describing the year
      Output: a boolean describing if year is leap year """
      year = int(year);
      if( year% 400 == 0 ):
            return True;
      elif ( year%100) == 0 :
            return False;
      elif ( (year%4) == 0 ):
            return True;
      return False;
