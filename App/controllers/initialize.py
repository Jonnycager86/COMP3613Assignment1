from .user import create_user
from App.database import db
from App.models import Admin, Staff, Shift, Timelog
from datetime import datetime, time


def initialize():
    db.drop_all()
    db.create_all()
    #create_user('bob', 'bobpass')
    
    #sample test data for commands 
    
    #for test purposes,e.g  2 shifts in a day both 7 hours (8am-3pm and 3pm-10pm)
    
    # Admins
    admin1 = Admin(username="alice_admin", password="adminpass1")
    admin2 = Admin(username="brian_admin", password="adminpass2")
    admin3 = Admin(username="carol_admin", password="adminpass3")
    db.session.add_all([admin1, admin2, admin3])

    # Staff Members
    staff1 = Staff(username="jon_staff", password="devpass")
    staff2 = Staff(username="maya_staff", password="designpass")
    staff3 = Staff(username="leo_staff", password="supportpass")
    staff4 = Staff(username="sarah_staff", password="marketpass")
    staff5 = Staff(username="mike_staff", password="salespass")
    staff6 = Staff(username="anna_staff", password="hrpass")
    staff7 = Staff(username="david_staff", password="financepass")
    staff8 = Staff(username="lisa_staff", password="operationspass")
    
    db.session.add_all([staff1, staff2, staff3, staff4, staff5, staff6, staff7, staff8])
    db.session.flush()  

    # if following this format should have 14 shifts in a 7 day week
    shifts = [
        Shift(start_time=datetime(2025, 9, 22, 8, 0), end_time=datetime(2025, 9, 22, 15, 0)),  # morning
        Shift(start_time=datetime(2025, 9, 22, 15, 0), end_time=datetime(2025, 9, 22, 22, 0)), # evening
        Shift(start_time=datetime(2025, 9, 23, 8, 0), end_time=datetime(2025, 9, 23, 15, 0)),  # morning
        Shift(start_time=datetime(2025, 9, 23, 15, 0), end_time=datetime(2025, 9, 23, 22, 0)), # evening
        Shift(start_time=datetime(2025, 9, 24, 8, 0), end_time=datetime(2025, 9, 24, 15, 0)),  # morning
        Shift(start_time=datetime(2025, 9, 24, 15, 0), end_time=datetime(2025, 9, 24, 22, 0)), # evening
        Shift(start_time=datetime(2025, 9, 25, 8, 0), end_time=datetime(2025, 9, 25, 15, 0)),  # morning
        Shift(start_time=datetime(2025, 9, 25, 15, 0), end_time=datetime(2025, 9, 25, 22, 0)), # evening
    ]

    db.session.add_all(shifts)
    db.session.commit()
    
    # Assign staff to shifts
    shifts[0].staff_members.extend([staff1, staff2])
    shifts[1].staff_members.extend([staff3, staff4])
    shifts[2].staff_members.extend([staff5, staff6])
    shifts[3].staff_members.extend([staff7, staff8])
    shifts[4].staff_members.extend([staff1, staff3])
    shifts[5].staff_members.extend([staff2, staff4])
    shifts[6].staff_members.extend([staff5, staff7])
    shifts[7].staff_members.extend([staff6, staff8])

    db.session.commit()
    
    # Timelogs - using valid shift indices (0-7)
    timelogs = [
        # 9/22 Morning e.g jon
    Timelog(staff_id=staff1.id, shift_id=shifts[0].id, time_in=datetime(2025, 9, 22, 7, 57), time_out=datetime(2025, 9, 22, 15, 3)),
    Timelog(staff_id=staff2.id, shift_id=shifts[0].id, time_in=datetime(2025, 9, 22, 8, 2), time_out=datetime(2025, 9, 22, 15, 0)),
        
      # 9/22 Evening
    Timelog(staff_id=staff3.id, shift_id=shifts[1].id, time_in=datetime(2025, 9, 22, 15, 0), time_out=datetime(2025, 9, 22, 22, 0)),
    Timelog(staff_id=staff4.id, shift_id=shifts[1].id, time_in=datetime(2025, 9, 22, 15, 5), time_out=datetime(2025, 9, 22, 21, 58)),
        
         # 9/23 Morning
    Timelog(staff_id=staff5.id, shift_id=shifts[2].id, time_in=datetime(2025, 9, 23, 7, 58), time_out=datetime(2025, 9, 23, 15, 0)),
    Timelog(staff_id=staff6.id, shift_id=shifts[2].id, time_in=datetime(2025, 9, 23, 8, 1), time_out=datetime(2025, 9, 23, 15, 2)),
        
        # 9/23 Evening
    Timelog(staff_id=staff7.id, shift_id=shifts[3].id, time_in=datetime(2025, 9, 23, 15, 0), time_out=datetime(2025, 9, 23, 22, 1)),
    Timelog(staff_id=staff8.id, shift_id=shifts[3].id, time_in=datetime(2025, 9, 23, 15, 3), time_out=datetime(2025, 9, 23, 21, 59)),
        
         # 9/24 Morning
    Timelog(staff_id=staff1.id, shift_id=shifts[4].id, time_in=datetime(2025, 9, 24, 7, 59), time_out=datetime(2025, 9, 24, 15, 1)),
    Timelog(staff_id=staff3.id, shift_id=shifts[4].id, time_in=datetime(2025, 9, 24, 8, 0), time_out=datetime(2025, 9, 24, 15, 2)),
        
         # 9/24 Evening
    Timelog(staff_id=staff2.id, shift_id=shifts[5].id, time_in=datetime(2025, 9, 24, 15, 2), time_out=datetime(2025, 9, 24, 22, 0)),
    Timelog(staff_id=staff4.id, shift_id=shifts[5].id, time_in=datetime(2025, 9, 24, 15, 0), time_out=datetime(2025, 9, 24, 21, 57)),
        
         # 9/25 Morning
    Timelog(staff_id=staff5.id, shift_id=shifts[6].id, time_in=datetime(2025, 9, 25, 7, 56), time_out=datetime(2025, 9, 25, 15, 0)),
    Timelog(staff_id=staff7.id, shift_id=shifts[6].id, time_in=datetime(2025, 9, 25, 8, 0), time_out=datetime(2025, 9, 25, 15, 2)),
        
         # 9/25 Evening
    Timelog(staff_id=staff6.id, shift_id=shifts[7].id, time_in=datetime(2025, 9, 25, 15, 1), time_out=datetime(2025, 9, 25, 22, 0)),
    Timelog(staff_id=staff8.id, shift_id=shifts[7].id, time_in=datetime(2025, 9, 25, 15, 3), time_out=datetime(2025, 9, 25, 21, 58)),
    ]
    
    db.session.add_all(timelogs)
    db.session.commit()