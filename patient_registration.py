import datetime

names = []
pickup_times = []
hospitals = []
patient_statuses = []
appointment_dates = []

print("Enter patient information. Type '0' as the patient name to finish registration.")

while True:
    patient_name = input("What is the patient's name?: ")
    if patient_name == "0":
        break
    else:
        names.append([patient_name])
        app_year = int(input("Appointment year? (2024 ->): "))
        app_month = int(input("Appointment month? (1-12): "))
        app_day = int(input("Appointment day? (1-31): "))
        app_hour = int(input("Appointment hour? (0-23): "))
        app_minute = int(input("Appointment minute? (0-59): "))
        
        appointment = datetime.datetime(app_year, app_month, app_day, app_hour, app_minute)
        appointment_date = datetime.datetime(app_year, app_month, app_day)
        appointment_dates.append(appointment_date)
        
        # Distance to hospital in meters
        dist_to_hospital = float(input("Distance to the hospital? (km): ")) * 1000
        
        # Assuming an average vehicle speed of 40 km/h
        travel_hours = (dist_to_hospital / 40000 * 60) // 60
        travel_minutes = (dist_to_hospital / 40000 * 60) % 60
        
        travel_duration = datetime.timedelta(hours=travel_hours, minutes=travel_minutes)
        pickup_time = appointment - travel_duration
        
        # Calculated when the patient should be picked up from home
        pickup_times.append(pickup_time)
        print(f"Calculated pickup times: {pickup_times}")
        
        target_hospital = input("Which hospital are they going to?: ")
        hospitals.append(target_hospital)
        
        while True:
            status = input("Enter 'a' for standing patient, 'y' for bed-resident patient: ")
            if status != "y" and status != "a":
                print("Invalid input. Please try again.")
            else:
                break
        patient_statuses.append(status)

# Added lists to the system successfully. [cite: 147, 155, 156]
