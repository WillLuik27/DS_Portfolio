
import pandas as pd

def grab_sheet(file_path):
    """
    Extract data from the provided CSV file and return the required datasets.
    :param file_path: Path to the CSV file.
    :return: Dictionary containing parsed data.
    """
    try:
        # Load CSV into a DataFrame
        data = pd.read_csv(file_path)

        data.columns = data.columns.str.strip()  # Remove leading/trailing spaces
        data.columns = data.columns.str.title()  # Capitalize each word (e.g., 'monday' -> 'Monday')
        print(data.columns)  # Check the cleaned column names


        # Initialize variables
        employee_names = []
        employee_pref = {}
        ability = {}
        availability = {}
        force_shift = {}
        allocated_max_hours = {}
        allocated_min_hours = {}
        hourly_requirements_BM = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

        # Helper function to extract a value from the table
        def get_value(operation_name):
            try:
                return data.loc[data['Operations'] == operation_name, 'Values'].values[0]
            except IndexError:
                print(f"Error: '{operation_name}' not found in CSV.")
                return None

        # Extract operational settings
        min_shift_len_hrs = get_value('Min shift length')
        max_shift_len_hrs = get_value('Max shift length')
        start_hour = get_value('start hour')
        end_hour = get_value('end hour')
        break_len = get_value('break length')
        hrs_until_break = get_value('hours until ppl need break')
        FP_cutoff_hour = get_value('FP cutoff hour')
        total_labor_hour_limit = get_value('Total hours for the week')
        min_weekly_FP_hrs = get_value('Min weekly FP hrs')
        earliest_shift_end = get_value('Earliest shift end ')
        latest_shift_start = get_value('Latest shift start')
        earliest_latest_flag = get_value('Include Earliest + Latest constraint?')
        max_daily_O_hrs = get_value('Max Daily Oven hrs')
        FP_latest_hr = get_value('FP latest time to work (24 hr #)')
        latest_FP_flag = get_value('Include the FP latest time constraint')

        # Extract hourly requirements for BM (row-based for weekdays only)
        bm_rows = data.loc[data['Operations'] == 'Min FP work hrs before cutoff', ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]]
        for day in hourly_requirements_BM.keys():
            hourly_requirements_BM[day] = bm_rows[day].dropna().astype(float).tolist()

        # Construct and return the data dictionary
        return {
            "hourly_requirements_BM": hourly_requirements_BM,
            "job_type": None,  # Add logic if needed
            "days_considering": list(hourly_requirements_BM.keys()),
            "total_labor_hour_limit": total_labor_hour_limit,
            "min_weekly_FP_hrs": min_weekly_FP_hrs,
            "FP_cutoff_hour": FP_cutoff_hour,
            "end_hour": end_hour,
            "start_hour": start_hour,
            "break_len": break_len,
            "hrs_until_break": hrs_until_break,
            "max_shift_len_hrs": max_shift_len_hrs,
            "min_shift_len_hrs": min_shift_len_hrs,
            "availability": availability,
            "force_shift": force_shift,
            "allocated_max_hours": allocated_max_hours,
            "allocated_min_hours": allocated_min_hours,
            "ability": ability,
            "employee_pref": employee_pref,
            "employee_names": employee_names,
            "sheets_time_limit": None,  # Add logic if needed
            "earliest_shift_end": earliest_shift_end,
            "latest_shift_start": latest_shift_start,
            "earliest_latest_flag": earliest_latest_flag,
            "max_daily_O_hrs": max_daily_O_hrs,
            "FP_latest_hr": FP_latest_hr,
            "latest_FP_flag": latest_FP_flag,
        }

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None




file_path = "/Users/williamluik/Desktop/Class_Documents/Sr_Fall/DS_Portfolio/DS_Portfolio/LG_Scheduler/Back_end.csv"


data = grab_sheet(file_path)


hourly_requirements_BM = data["hourly_requirements_BM"]
job_type = data["job_type"]
days_considering = data["days_considering"]
total_labor_hour_limit = data["total_labor_hour_limit"]
FP_cutoff_hour = data["FP_cutoff_hour"]
end_hour = data["end_hour"]
start_hour = data["start_hour"]
break_len = data["break_len"]
hrs_until_break = data["hrs_until_break"]
max_shift_len_hrs = data["max_shift_len_hrs"]
min_shift_len_hrs = data["min_shift_len_hrs"]
availability = data["availability"]
force_shift = data["force_shift"]
allocated_max_hours = data["allocated_max_hours"]
allocated_min_hours = data["allocated_min_hours"]
ability = data["ability"]
employee_pref = data["employee_pref"]
employee_names = data["employee_names"]
min_daily_FP_hrs = data["min_daily_FP_hrs"]
min_weekly_FP_hrs = data["min_weekly_FP_hrs"]
sheets_time_limit = data["sheets_time_limit"]
earliest_shift_end_hrs =data["earliest_shift_end"]
latest_shift_start_hrs= data["latest_shift_start"]
earliest_latest_flag = data["earliest_latest_flag"]
max_daily_O_hrs = data["max_daily_O_hrs"]
FP_latest_hr = data["FP_latest_hr"]
latest_FP_flag= data["latest_FP_flag"]
emp_num_shifts = data["emp_num_shifts"]
start_shift_ranges = data["start_shift_ranges"]
shift_lengths = data["shift_lengths"]



print("_______Operations info check________")
print("days_considering", days_considering)
print("total_labor_hour_limit", total_labor_hour_limit)
print("min_morning_FP_hrs______________", min_morning_FP_hrs)
print("FP_cutoff_hour",FP_cutoff_hour, " AM")