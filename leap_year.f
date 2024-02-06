!===============================================================================
!
      SUBROUTINE Is_Leap_Year (year, leap)
!
! This subroutine returns "leap" as TRUE if the four digit "year" specified
! is a leap year (where February has 29 days instead of the usual 28).  Since 
! the nominal start of the Gregorian calendar on 15 October 1582, leap years
! occur in years with 4 as a factor (e.g., 1992, 1996, 2004, 2008), except
! for centuries (e.g., 1800, 1900, 2100, 2200), though the century rule is
! suspended every 400 years (e.g., 1600, 2000, 2400 are leap years).  This
! rule system makes the average year 365.2425 days long, which is close to
! the astronomical value of 365.2422.  The difference will be less than a
! day by year 4000.  At this time there is no international standard that
! specifies whether 4000 is a leap year or not.
!
! Variables used
!
! ---------- Intent IN/OUT -----------
!
      integer, intent (IN)  :: year      ! must be a four digit year
      logical, intent (OUT) :: leap      ! True if "year" is a leap year
!
!-------------------------------------------------------------------------------
!
!  Go up the heirarchy of rules covered in the comments above.
!
      if         ( mod(year, 400) == 0 ) then
            leap = .TRUE.
         else if ( mod(year, 100) == 0 ) then
            leap = .FALSE.
         else if ( mod(year,   4) == 0 ) then
            leap = .TRUE.
         else
            leap = .FALSE.
         end if

      return
      end subroutine Is_Leap_Year
!
!===============================================================================
!
      PROGRAM Test_Is_Leap_Year
!
! This program tests the subroutine Is_Leap_Year.
!
! Variables used
!
      integer :: year    ! year to test for being a leap year
      logical :: leap    ! true if a leap year
!
!-------------------------------------------------------------------------------
!
 10   write (*, *)                        ! blank line
      write (*, *) "Enter a four digit year (or 0 to exit):"
      read (*, *) year

      if (year == 0) then                 ! if exit code, then
            goto 20                       !    go to exit block
         else if (year < 1582) then
            print *, "ERROR:  ", year, "is pre-Gregorian calendar."
            goto 10
         else if (year >= 4000) then
            print *, "ERROR:  ", year, "has no agreed on leap year standard."
            goto 10
         end if
      
      call Is_Leap_Year (year, leap)

      if (leap) then
            print *, year, "is a leap year"
         else
            print *, year, "is not a leap year"
         end if
         
      goto 10                             ! loop continuously until exit code

 20   write (*, *)                        ! blank line
      print *, "Thank you; have a good end of semester."

      stop
      end program Test_Is_Leap_Year
