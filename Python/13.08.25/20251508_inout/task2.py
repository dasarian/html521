from datetime import datetime, timedelta

hours_input = input("Введите количество часов: ")
minutes_input = input("Введите количество минут: ")

hours = float(hours_input)
minutes = float(minutes_input)

task_duration = timedelta(hours=hours, minutes=minutes)

total_duration = task_duration + timedelta(hours=1)

deadline = datetime.now().replace(hour=19, minute=0, second=0, microsecond=0)

start_time = deadline - total_duration

print(f"Самое позднее время начала: {start_time.strftime('%H:%M')}")
