from .user import create_user
from App.database import db
from App.models import Admin, Staff, Shift, Timelog
from datetime import datetime, time


def initialize():
    db.drop_all()
    db.create_all()
    #create_user('bob', 'bobpass')
    
    #test for commands (change later)
    
    # Create Admins
    admin1 = Admin(username="alice_admin", password="adminpass1")
    admin2 = Admin(username="brian_admin", password="adminpass2")
    admin3 = Admin(username="carol_admin", password="adminpass3")
    db.session.add_all([admin1, admin2, admin3])

    # Create Staff Members
    staff1 = Staff(username="jon_staff", password="devpass")
    staff2 = Staff(username="maya_staff", password="designpass")
    staff3 = Staff(username="leo_staff", password="supportpass")
    staff4 = Staff(username="sarah_staff", password="marketpass")
    staff5 = Staff(username="mike_staff", password="salespass")
    staff6 = Staff(username="anna_staff", password="hrpass")
    staff7 = Staff(username="david_staff", password="financepass")
    staff8 = Staff(username="lisa_staff", password="operationspass")
    
    db.session.add_all([staff1, staff2, staff3, staff4, staff5, staff6, staff7, staff8])
    db.session.flush()  # ensures staff IDs are available for FK use

    # Create Shifts - ensuring at least 2 shifts per staff member
    shifts = [
        # Jon's shifts (staff1)
        Shift(staff_id=staff1.id,
              start_time=datetime(2025, 9, 22, 9, 0),
              end_time=datetime(2025, 9, 22, 17, 0)),
        Shift(staff_id=staff1.id,
              start_time=datetime(2025, 9, 25, 9, 0),
              end_time=datetime(2025, 9, 25, 17, 0)),
        Shift(staff_id=staff1.id,
              start_time=datetime(2025, 9, 29, 8, 30),
              end_time=datetime(2025, 9, 29, 16, 30)),
        
        # Maya's shifts (staff2)
        Shift(staff_id=staff2.id,
              start_time=datetime(2025, 9, 23, 10, 0),
              end_time=datetime(2025, 9, 23, 18, 0)),
        Shift(staff_id=staff2.id,
              start_time=datetime(2025, 9, 26, 10, 0),
              end_time=datetime(2025, 9, 26, 18, 0)),
        Shift(staff_id=staff2.id,
              start_time=datetime(2025, 9, 30, 9, 30),
              end_time=datetime(2025, 9, 30, 17, 30)),
        
        # Leo's shifts (staff3)
        Shift(staff_id=staff3.id,
              start_time=datetime(2025, 9, 24, 8, 30),
              end_time=datetime(2025, 9, 24, 16, 30)),
        Shift(staff_id=staff3.id,
              start_time=datetime(2025, 9, 27, 8, 30),
              end_time=datetime(2025, 9, 27, 16, 30)),
        Shift(staff_id=staff3.id,
              start_time=datetime(2025, 10, 1, 9, 0),
              end_time=datetime(2025, 10, 1, 17, 0)),
        
        # Sarah's shifts (staff4)
        Shift(staff_id=staff4.id,
              start_time=datetime(2025, 9, 22, 8, 0),
              end_time=datetime(2025, 9, 22, 16, 0)),
        Shift(staff_id=staff4.id,
              start_time=datetime(2025, 9, 24, 8, 0),
              end_time=datetime(2025, 9, 24, 16, 0)),
        Shift(staff_id=staff4.id,
              start_time=datetime(2025, 9, 26, 8, 0),
              end_time=datetime(2025, 9, 26, 16, 0)),
        Shift(staff_id=staff4.id,
              start_time=datetime(2025, 9, 28, 8, 0),
              end_time=datetime(2025, 9, 28, 16, 0)),
        
        # Mike's shifts (staff5) - includes some weekend shifts
        Shift(staff_id=staff5.id,
              start_time=datetime(2025, 9, 21, 12, 0),
              end_time=datetime(2025, 9, 21, 20, 0)),
        Shift(staff_id=staff5.id,
              start_time=datetime(2025, 9, 22, 12, 0),
              end_time=datetime(2025, 9, 22, 20, 0)),
        Shift(staff_id=staff5.id,
              start_time=datetime(2025, 9, 28, 12, 0),
              end_time=datetime(2025, 9, 28, 20, 0)),
        Shift(staff_id=staff5.id,
              start_time=datetime(2025, 9, 29, 12, 0),
              end_time=datetime(2025, 9, 29, 20, 0)),
        
        # Anna's shifts (staff6)
        Shift(staff_id=staff6.id,
              start_time=datetime(2025, 9, 23, 9, 0),
              end_time=datetime(2025, 9, 23, 17, 0)),
        Shift(staff_id=staff6.id,
              start_time=datetime(2025, 9, 25, 9, 0),
              end_time=datetime(2025, 9, 25, 17, 0)),
        Shift(staff_id=staff6.id,
              start_time=datetime(2025, 9, 27, 8, 0),
              end_time=datetime(2025, 9, 27, 16, 0)),
        
        # David's shifts (staff7) - part-time schedule
        Shift(staff_id=staff7.id,
              start_time=datetime(2025, 9, 23, 13, 0),
              end_time=datetime(2025, 9, 23, 17, 0)),
        Shift(staff_id=staff7.id,
              start_time=datetime(2025, 9, 25, 13, 0),
              end_time=datetime(2025, 9, 25, 17, 0)),
        Shift(staff_id=staff7.id,
              start_time=datetime(2025, 9, 27, 13, 0),
              end_time=datetime(2025, 9, 27, 17, 0)),
        Shift(staff_id=staff7.id,
              start_time=datetime(2025, 9, 30, 13, 0),
              end_time=datetime(2025, 9, 30, 17, 0)),
        
        # Lisa's shifts (staff8) - early morning shifts
        Shift(staff_id=staff8.id,
              start_time=datetime(2025, 9, 22, 6, 0),
              end_time=datetime(2025, 9, 22, 14, 0)),
        Shift(staff_id=staff8.id,
              start_time=datetime(2025, 9, 24, 6, 0),
              end_time=datetime(2025, 9, 24, 14, 0)),
        Shift(staff_id=staff8.id,
              start_time=datetime(2025, 9, 26, 6, 0),
              end_time=datetime(2025, 9, 26, 14, 0)),
        Shift(staff_id=staff8.id,
              start_time=datetime(2025, 9, 29, 6, 0),
              end_time=datetime(2025, 9, 29, 14, 0)),
    ]
    
    db.session.add_all(shifts)
    db.session.flush()

    # Create some sample Timelogs (if you want to test with actual clock-in/out data)
    timelogs = [
        # Jon's timelogs for his first shift
        Timelog(staff_id=staff1.id, shift_id=shifts[0].id,
               time_in=datetime(2025, 9, 22, 8, 58),
               time_out=datetime(2025, 9, 22, 17, 5)),
        
        # Maya's timelogs for her first shift
        Timelog(staff_id=staff2.id, shift_id=shifts[3].id,
               time_in=datetime(2025, 9, 23, 9, 55),
               time_out=datetime(2025, 9, 23, 18, 10)),
        
        # Leo's timelogs for his first shift
        Timelog(staff_id=staff3.id, shift_id=shifts[6].id,
               time_in=datetime(2025, 9, 24, 8, 30),
               time_out=datetime(2025, 9, 24, 16, 35)),
        
        # Sarah's timelogs
        Timelog(staff_id=staff4.id, shift_id=shifts[9].id,
               time_in=datetime(2025, 9, 22, 7, 55),
               time_out=datetime(2025, 9, 22, 16, 0)),
        
        # Mike's timelogs
        Timelog(staff_id=staff5.id, shift_id=shifts[13].id,
               time_in=datetime(2025, 9, 21, 11, 58),
               time_out=datetime(2025, 9, 21, 20, 2)),
        
        # Anna's timelogs
        Timelog(staff_id=staff6.id, shift_id=shifts[17].id,
               time_in=datetime(2025, 9, 23, 9, 0),
               time_out=datetime(2025, 9, 23, 17, 0)),
        
        # David's timelogs
        Timelog(staff_id=staff7.id, shift_id=shifts[20].id,
               time_in=datetime(2025, 9, 23, 13, 5),
               time_out=datetime(2025, 9, 23, 17, 0)),
        
        # Lisa's timelogs
        Timelog(staff_id=staff8.id, shift_id=shifts[24].id,
               time_in=datetime(2025, 9, 22, 5, 58),
               time_out=datetime(2025, 9, 22, 14, 2)),
    ]
    
    db.session.add_all(timelogs)
    db.session.commit()