import click, pytest, sys
from rich.console import Console
from rich.table import Table
from datetime import datetime, timedelta
from flask.cli import with_appcontext, AppGroup
from datetime import datetime
from App.database import db, get_migrate
from App.models import User, Admin, Shift, Staff, Timelog, Staff_shift
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


#NOTE: All sample data for admin users, staff users,
# shifts etc are in initialize.py

'''
Staff Commands
'''
staff_cli = AppGroup('staff', help="Staff member object commands")

# Command to view all staff
@staff_cli.command("view", help="Displays roster of all staff")
@click.argument("format", default="string")
def list_roster(format):
    staff_list = Staff.query.all()
    for staff in staff_list:
        print(staff)
    

# Command to view all shifts    
@staff_cli.command("view-shifts", help="view all shifts")
def list_shifts():
    shift_list = Shift.query.all()
    for shift in shift_list:
        print(shift)
   
   
# Command to add new staff user
@staff_cli.command("add-staff", help="Add a new staff user")   
def add_staff():

        name = click.prompt("Enter new staff username")
        if not 3 <= len(name) <= 20:
            print("Username needs to be in between 3 and 30 characters")
            
        password = click.prompt("Enter password" , hide_input = True)
        if len(password)<6:
            print("Password must be longer than 6 characters")
            return
        
        new_staff = Staff(name, password) 
        print(f"New staff {name} added")
        db.session.add(new_staff)
        db.session.commit()
        


# Command to log time in
@staff_cli.command("time-in", help="Logs the time in for the staff user for a shift")
def log_time_in():
    username = click.prompt("Enter username")
    staff = Staff.query.filter_by(username=username).first()
    if not staff:
        print("Staff could not be found")
        return
    
    
    if not staff.shifts:
        print("No shifts assigned to this staff member.")
        return
    
    for shift in staff.shifts:
        print(f" Shift ID :{shift.id} {shift.start_time} - {shift.end_time}")
    
    shift_id = click.prompt("Enter your shift ID based on the assigned shifts above", type=int)
    shift = Shift.query.filter_by(id=shift_id).first()
    if not shift:
        print("invalid shift ID entered")
        return
    

    today = datetime.now()
    date_str = click.prompt("Enter date in format (dd/mm/yyyy)")
    time_in_str = click.prompt("Enter time in format (24 hour time) (hh:mm)")
    print(time_in_str)
    
    date_time_str = f"{date_str} {time_in_str}"
    
    try:
        dateTimeObj = datetime.strptime(date_time_str, "%d/%m/%Y %H:%M" )
        if dateTimeObj > today:
            print("Date entered is after today's date")
            return
    
    except ValueError:
        print("date/time format invalid")
        
    log = Timelog(staff_id=staff.id, shift_id=shift.id,time_in=dateTimeObj)
    db.session.add(log)
    db.session.commit()
    print(f"time-in recorded for {staff.username} on shift {shift.id} at {dateTimeObj}.")
        
        
        
#Command to log time out
@staff_cli.command("time-out", help="Logs the time in for the staff user for a shift")
def log_time_out():
    username = click.prompt("Enter username")
    staff = Staff.query.filter_by(username=username).first()
    if not staff:
        print("Staff could not be found")
        return
    
    shift_id = click.prompt("Enter your shift ID", type=int)
    shift = Shift.query.filter_by(id=shift_id).first()
    if not shift:
        print("invalid shift ID entered")
        return
    

    date_str = click.prompt("Enter date in format (dd/mm/yyyy)")
    time_in_str = click.prompt("Enter time in format (24 hour time) (hh:mm)")
    print(date_str)
    print(time_in_str)
    
    date_time_str = f"{date_str} {time_in_str}"
    
    try:
        dateTimeObj = datetime.strptime(date_time_str, "%d/%m/%Y %H:%M")
    
    except ValueError:
        print("date/time format invalid")
    
    
    existing_log = Timelog.query.filter_by(staff_id=staff.id, shift_id=shift.id).first()
    if not existing_log.time_in:
        print("No time-in record for this shift")
        return
    
    existing_log.time_out = dateTimeObj;
    
    db.session.commit()
    print(f"time-out recorded for {staff.username} on shift {shift.id} at {dateTimeObj}.")


app.cli.add_command(staff_cli)


'''
Admin Commands
'''


admin_cli = AppGroup('admin', help="admin commands")

# Command to add new admin user
@admin_cli.command("add-admin", help="Add a new admin user")   
def add_staff():

        name = click.prompt("Enter new admin username")
        if not 3 <= len(name) <= 20:
            print("Username needs to be in between 3 and 20 characters")
            return
        
        password = click.prompt("Enter password")
        if len(password)<6:
            print("Password must be longer than 6 characters")
            return
        
        new_admin = Admin(name, password) 
        print(f"New staff {name} added")
        db.session.add(new_admin)
        db.session.commit()
    
    
# Command to schedule a shift // fixed amount of shifts for the week
@admin_cli.command("schedule-shift", help="Schedule a staff member's shift")
def schedule_shift():
    
    admin_username = click.prompt("Enter admin username")
    admin = Admin.query.filter_by(username=admin_username).first()
    if not admin:
        print("Admin not found or not Admin user")
        return
    
    staff_username = click.prompt("Enter staff username to schedule")
    staff = Staff.query.filter_by(username=staff_username).first()
    if not staff:
        print("Staff member not found")
        return
    
    shift_list = Shift.query.all()
    for shift in shift_list:
        print(f"{shift} {shift.start_time} {shift.end_time}")
        
    shift_selection = click.prompt("Select a shift ID for selection", type = int)
    shift = Shift.query.filter_by(id=shift_selection).first()
    
    if staff in shift.staff_members:
        print(f"{staff} is already assigned to this shift")
        return
    
    shift.staff_members.append(staff)
    db.session.commit()
    print(f" {staff.username} has been assigned to shift {shift.id}")
    
    

def get_weekly_shift_report(start_date):
    end_date = start_date + timedelta(days=7)
    shifts = Shift.query.filter(
        Shift.start_time >= start_date,
        Shift.end_time <= end_date
    ).all()

    report = []
    for shift in shifts:
        staff = Staff.query.get(shift.staff_id)
        log = Timelog.query.filter_by(shift_id=shift.id, staff_id=staff.id).first()

        time_in = log.time_in if log else None
        time_out = log.time_out if log else None
        hours_worked = None
        status = "Complete" if time_in and time_out else "In Only" if time_in else "No Log"

        if time_in and time_out:
            hours_worked = (time_out - time_in).total_seconds() / 3600
            int_hours = int(hours_worked)
            deci = hours_worked - int_hours
            mins = round(60 * deci)
            
        report.append({
            "staff": staff.username,
            "date": shift.start_time.strftime("%d/%m/%Y"),
            "start": shift.start_time.strftime("%H:%M"),
            "end": shift.end_time.strftime("%H:%M"),
            "time_in": time_in.strftime("%H:%M") if time_in else "-",
            "time_out": time_out.strftime("%H:%M") if time_out else "-",
            "hours": f"{(int(hours_worked))}h {mins} m" if hours_worked else "-",
            "status": status
        })

    return report


@admin_cli.command("shiftreport", help="View weekly shift report")
def shift_report_command():
    
    start_date = click.prompt("Enter a start date")
    try:
        start_dt = datetime.strptime(start_date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Use DD/MM/YYYY.")
        return

    report = get_weekly_shift_report(start_dt)

    table = Table(title="Weekly Shift Report", show_lines=True)
    table.add_column("Staff", style="cyan", no_wrap=True)
    table.add_column("Date", style="white")
    table.add_column("Shift Start", style="green")
    table.add_column("Shift End", style="green")
    table.add_column("Time In", style="yellow")
    table.add_column("Time Out", style="yellow")
    table.add_column("Hours Worked", justify="right", style="magenta")
    table.add_column("Status", style="bold")

    for entry in report:
        table.add_row(
            entry["staff"],
            entry["date"],
            entry["start"],
            entry["end"],
            entry["time_in"],
            entry["time_out"],
            entry["hours"],
            entry["status"]
        )

    console = Console()
    console.print(table)



app.cli.add_command(admin_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)