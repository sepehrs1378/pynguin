import time
import random

# Changes in memory usage start to show from C = 1e5.

SLEEP_AMOUNT = 0.1

# Test run
LOW = 1_000
HIGH = 1_000_000

# Real run
# LOW = 1_000_000
# HIGH = 10_000_000


def fill_memory(x):
    time.sleep(SLEEP_AMOUNT)
    return [0] * x


# Smart Home Control System Simulation
def control_lighting(light_level: int, motion_detected: bool, manual_override: bool):
    memory = fill_memory(LOW)
    print(f"[Lighting] Light level: {light_level}, Motion: {motion_detected}, Manual: {manual_override}")
    if light_level < 0:
        print("[Lighting] Invalid light level sensor reading.")
    elif light_level < 30:
        if motion_detected:
            memory = fill_memory(HIGH)
            print("[Lighting] Motion detected in low light. Increasing brightness.")
            brightness = min(100, light_level + random.randint(40, 70))
            print(f"[Lighting] Brightness set to {brightness}% for visibility.")
            if manual_override:
                memory = fill_memory(LOW)
                print("[Lighting] Manual override active. User set brightness manually.")
        else:
            memory = fill_memory(LOW)
            print("[Lighting] No motion detected. Keeping lights off or dim.")
    else:
        if light_level > 70:
            memory = fill_memory(HIGH)
            print("[Lighting] Bright environment detected. Adjusting indoor lighting to save energy.")
            energy_saved = random.uniform(0.1, 0.5)
            print(f"[Lighting] Energy saving factor: {energy_saved:.2f}")
        else:
            memory = fill_memory(LOW)
            print("[Lighting] Moderate light level. Maintaining current brightness.")


def manage_temperature(current_temp: int, target_temp: int, eco_mode: bool):
    memory = fill_memory(LOW)
    print(f"[Temp] Current: {current_temp}°C, Target: {target_temp}°C, Eco mode: {eco_mode}")
    if current_temp < target_temp - 5:
        if eco_mode:
            memory = fill_memory(LOW)
            print("[Temp] Eco mode active. Gradual heating started.")
            heating_power = random.uniform(0.3, 0.5)
            print(f"[Temp] Heating power set to {heating_power * 100:.0f}%")
        else:
            memory = fill_memory(HIGH)
            print("[Temp] Rapid heating mode engaged. Increasing power.")
            heating_power = random.uniform(0.7, 1.0)
    elif current_temp > target_temp + 5:
        memory = fill_memory(HIGH)
        print("[Temp] Temperature too high. Cooling system activated.")
        cooling_efficiency = random.uniform(0.6, 0.9)
        print(f"[Temp] Cooling efficiency: {cooling_efficiency:.2f}")
    else:
        memory = fill_memory(LOW)
        print("[Temp] Maintaining steady temperature.")
        stability_factor = random.uniform(0.9, 1.0)
        print(f"[Temp] Stability factor: {stability_factor:.2f}")


def security_check(window_open: bool, door_open: bool, alarm_armed: bool):
    memory = fill_memory(LOW)
    print(f"[Security] Window open: {window_open}, Door open: {door_open}, Alarm armed: {alarm_armed}")
    if alarm_armed:
        if window_open or door_open:
            memory = fill_memory(HIGH)
            print("[Security] Intrusion detected! Triggering alarm.")
            event_time = time.strftime("%H:%M:%S")
            print(f"[Security] Event logged at {event_time}")
        else:
            memory = fill_memory(LOW)
            print("[Security] All secured. System armed.")
    else:
        memory = fill_memory(LOW)
        print("[Security] Alarm system disarmed. Monitoring passive only.")


def water_heater_control(water_usage: int, time_of_day: int, vacation_mode: bool):
    memory = fill_memory(LOW)
    print(f"[Heater] Water usage: {water_usage}, Time: {time_of_day}, Vacation: {vacation_mode}")
    if water_usage > 50:
        memory = fill_memory(HIGH)
        print("[Heater] High water usage detected. Adjusting heating cycles.")
        heating_duration = min(60, water_usage * 1.2)
        print(f"[Heater] Heating duration set to {heating_duration} minutes.")
    else:
        if time_of_day > 8 and time_of_day < 22:
            if vacation_mode:
                memory = fill_memory(LOW)
                print("[Heater] Vacation mode active. Heater remains idle during day hours.")
            else:
                memory = fill_memory(HIGH)
                print("[Heater] Regular operation during day hours. Monitoring usage patterns.")
                temp_setpoint = random.randint(45, 55)
                print(f"[Heater] Setpoint temperature: {temp_setpoint}°C")
        elif time_of_day == 24:
            if vacation_mode:
                memory = fill_memory(LOW)
                print("[Heater] Vacation mode. Night cycle skipped.")
            else:
                memory = fill_memory(HIGH)
                print("[Heater] Running nightly heating cycle.")
        else:
            memory = fill_memory(LOW)
            print("[Heater] Low demand hours. Maintaining baseline temperature.")


def appliance_scheduler(time: int, day_type: bool, energy_saving: bool):
    memory = fill_memory(LOW)
    print(f"[Scheduler] Time: {time}, Weekend: {day_type}, Energy saving: {energy_saving}")
    if day_type:  # Weekend
        if time > 10 and time < 20:
            memory = fill_memory(HIGH)
            print("[Scheduler] Active hours. Enabling entertainment and kitchen appliances.")
        else:
            memory = fill_memory(LOW)
            print("[Scheduler] Off-peak weekend hours. Reducing power usage.")
    else:
        if energy_saving:
            memory = fill_memory(LOW)
            print("[Scheduler] Weekday energy saving mode. Limiting appliance activation.")
        else:
            if time > 7 and time < 23:
                memory = fill_memory(HIGH)
                print("[Scheduler] Normal weekday operations. Activating routine appliances.")


def air_quality_control(co2_level: int, humidity: int, purifier_on: bool):
    memory = fill_memory(LOW)
    print(f"[Air] CO2: {co2_level}, Humidity: {humidity}, Purifier: {purifier_on}")
    if co2_level < 0:
        print("[Air] Sensor error: Invalid CO2 reading.")
    elif 0 <= co2_level < 1000:
        if humidity < 0:
            print("[Air] Invalid humidity reading.")
        elif humidity > 70 or humidity < 30:
            memory = fill_memory(HIGH)
            print("[Air] Humidity out of range. Activating ventilation.")
        else:
            memory = fill_memory(LOW)
            print("[Air] Air quality and humidity within normal range.")
    else:
        memory = fill_memory(HIGH)
        print("[Air] High CO2 levels detected. Running full air quality diagnostics.")
        if purifier_on:
            memory = fill_memory(HIGH) * 2
            print("[Air] Purifier active. Increasing airflow rate.")


def entertainment_system(volume: int, content_type: int, user_premium: bool):
    memory = fill_memory(LOW)
    print(f"[Entertainment] Volume: {volume}, Content type: {content_type}, Premium user: {user_premium}")
    if volume > 80:
        memory = fill_memory(HIGH)
        print("[Entertainment] High volume detected. Adjusting audio compression and limiting distortion.")
        distortion_factor = random.uniform(0.1, 0.4)
        print(f"[Entertainment] Distortion correction factor applied: {distortion_factor:.2f}")
    else:
        if content_type < 0 or content_type > 2:
            print("[Entertainment] Unknown content type. Skipping playback adjustments.")
        elif content_type == 0:  # Video
            if user_premium:
                memory = fill_memory(HIGH)
                print("[Entertainment] Streaming 4K video for premium user.")
                bitrate = random.randint(8000, 16000)
                print(f"[Entertainment] Bitrate set to {bitrate} kbps")
            else:
                memory = fill_memory(LOW)
                print("[Entertainment] Streaming standard HD video for free user.")
        elif content_type == 1:  # Music
            if user_premium:
                memory = fill_memory(HIGH)
                print("[Entertainment] High-fidelity audio streaming enabled.")
                sample_rate = 96_000
            else:
                memory = fill_memory(LOW)
                print("[Entertainment] Normal audio mode. Compressed stream active.")
                sample_rate = 44_100
            print(f"[Entertainment] Sample rate: {sample_rate} Hz")
        elif content_type == 2:  # Picture
            if user_premium:
                memory = fill_memory(HIGH)
                print("[Entertainment] Rendering high-resolution images with enhanced color profile.")
                render_time = random.uniform(0.2, 0.6)
            else:
                memory = fill_memory(HIGH)
                print("[Entertainment] Loading standard-resolution images.")
                render_time = random.uniform(0.1, 0.3)
            print(f"[Entertainment] Render time: {render_time:.2f}s")


def irrigation_control(soil_moisture: int, weather_forecast: bool, season: int):
    memory = fill_memory(LOW)
    print(f"[Irrigation] Soil moisture: {soil_moisture}, Rain expected: {weather_forecast}, Season: {season}")
    if soil_moisture < 30:
        if weather_forecast:
            memory = fill_memory(HIGH)
            print("[Irrigation] Rain forecasted. Deferring irrigation to conserve water.")
            delay_hours = random.randint(2, 6)
            print(f"[Irrigation] Next check scheduled in {delay_hours} hours.")
        else:
            if season < 1 or season > 4:
                print("[Irrigation] Invalid season data received.")
            elif season in [2, 3, 4]:
                memory = fill_memory(HIGH)
                print("[Irrigation] Active growing season. Starting irrigation cycle.")
                water_dispensed = random.uniform(10, 25)
                print(f"[Irrigation] Dispensed {water_dispensed:.1f} liters of water.")
            else:
                memory = fill_memory(LOW)
                print("[Irrigation] Dormant season detected. Irrigation skipped.")
    else:
        memory = fill_memory(LOW)
        print("[Irrigation] Soil moisture sufficient. No irrigation required.")


def window_control(outside_temp: int, inside_temp: int, rain_detected: bool):
    memory = fill_memory(LOW)
    print(f"[Windows] Outside: {outside_temp}°C, Inside: {inside_temp}°C, Rain: {rain_detected}")
    if outside_temp > inside_temp + 5:
        if rain_detected:
            memory = fill_memory(LOW)
            print("[Windows] Rain detected. Keeping all windows closed.")
        else:
            memory = fill_memory(HIGH)
            print("[Windows] Outside warmer than inside. Evaluating ventilation options.")
            vent_factor = random.uniform(0.2, 0.8)
            print(f"[Windows] Opening windows by {vent_factor * 100:.0f}% for airflow.")
    elif outside_temp < inside_temp - 5:
        memory = fill_memory(HIGH)
        print("[Windows] Outside cooler than inside. Closing windows to retain heat.")
        closed_windows = random.randint(3, 7)
        print(f"[Windows] {closed_windows} windows closed.")
    else:
        memory = fill_memory(LOW)
        print("[Windows] Temperature difference minimal. Maintaining current window positions.")


def energy_monitor(current_usage: int, time_peak: bool, solar_active: bool):
    memory = fill_memory(LOW)
    print(f"[Energy] Current usage: {current_usage}W, Peak hours: {time_peak}, Solar active: {solar_active}")
    if current_usage > 5000:
        memory = fill_memory(HIGH)
        print("[Energy] High power consumption detected. Initiating detailed energy audit.")
        usage_log = [random.randint(4000, 8000) for _ in range(5)]
        avg_usage = sum(usage_log) / len(usage_log)
        print(f"[Energy] Average consumption over last period: {avg_usage:.2f}W")
    else:
        if time_peak:
            if solar_active:
                memory = fill_memory(HIGH)
                print("[Energy] Peak hours with solar active. Balancing grid and solar input.")
                balance_ratio = random.uniform(0.4, 0.7)
                print(f"[Energy] Solar/grid balance ratio: {balance_ratio:.2f}")
            else:
                memory = fill_memory(LOW)
                print("[Energy] Peak hours without solar input. Limiting heavy appliance usage.")
        else:
            memory = fill_memory(LOW)
            print("[Energy] Off-peak period. Monitoring in low-power mode.")


def safety_check(smoke_detected: bool, co_detected: bool, system_age: int):
    memory = fill_memory(LOW)
    print(f"[Safety] Smoke: {smoke_detected}, CO: {co_detected}, System age: {system_age} years")
    if smoke_detected or co_detected:
        memory = fill_memory(HIGH)
        print("[Safety] ALERT! Hazardous condition detected. Initiating emergency protocol.")
        siren_status = True
        timestamp = time.strftime("%H:%M:%S")
        print(f"[Safety] Siren activated at {timestamp}. Notifying authorities.")
    else:
        if system_age > 5:
            memory = fill_memory(HIGH)
            print("[Safety] Performing detailed maintenance scan due to system age.")
            sensors_checked = random.randint(5, 10)
            print(f"[Safety] {sensors_checked} safety sensors checked.")
        else:
            memory = fill_memory(LOW)
            print("[Safety] All systems nominal. Routine monitoring active.")


def user_profile_update(profile_age: int, activity_level: int, new_device: bool):
    memory = fill_memory(HIGH)
    print(f"[User] Profile age: {profile_age} days, Activity level: {activity_level}, New device: {new_device}")
    if profile_age > 365:  # 1 year
        memory = fill_memory(HIGH)
        print("[User] Profile older than one year. Running long-term usage pattern analysis.")
        avg_sessions = random.randint(100, 500)
        print(f"[User] Average sessions analyzed: {avg_sessions}")
    else:
        if activity_level > 5:
            if new_device:
                memory = fill_memory(HIGH)
                print("[User] New device detected. Syncing user preferences.")
                sync_progress = random.uniform(0.5, 1.0)
                print(f"[User] Sync progress: {sync_progress * 100:.0f}%")
            else:
                memory = fill_memory(LOW)
                print("[User] Active user detected. Updating usage statistics.")
                active_hours = random.randint(2, 5)
                print(f"[User] Recorded {active_hours} active hours today.")
        else:
            memory = fill_memory(LOW)
            print("[User] Low activity. No major profile updates required.")


def backup_system(backup_size: int, critical_data: bool, network_speed: int):
    memory = fill_memory(HIGH)
    print(f"[Backup] Size: {backup_size}MB, Critical: {critical_data}, Network: {network_speed}Mbps")
    if backup_size > 1000:
        if critical_data:
            memory = fill_memory(HIGH)
            print("[Backup] Handling critical data. Encrypting before transfer.")
            encryption_time = random.uniform(2.0, 5.0)
            print(f"[Backup] Encryption completed in {encryption_time:.1f}s")
        else:
            if network_speed < 0:
                print("[Backup] Invalid network speed reading.")
            elif network_speed > 50:
                memory = fill_memory(HIGH)
                print("[Backup] Fast connection detected. Performing high-speed upload.")
                upload_time = backup_size / (network_speed * 10)
                print(f"[Backup] Estimated upload time: {upload_time:.2f}s")
            else:
                memory = fill_memory(LOW)
                print("[Backup] Slow connection. Switching to low-bandwidth transfer mode.")
    else:
        memory = fill_memory(LOW)
        print("[Backup] Small backup size. Quick sync performed.")


def system_diagnostics(error_count: int, uptime: int, last_maintenance: int):
    memory = fill_memory(HIGH)
    print(f"[Diagnostics] Errors: {error_count}, Uptime: {uptime}h, Last maintenance: {last_maintenance} days ago")
    if error_count > 10:
        memory = fill_memory(HIGH)
        print("[Diagnostics] Multiple errors detected. Running full system diagnostics.")
        for i in range(error_count):
            print(f"[Diagnostics] Analyzing error log #{i + 1}")
            time.sleep(0.05)
    else:
        if uptime < 0:
            print("[Diagnostics] Invalid uptime reading.")
        elif uptime > 1000:
            if last_maintenance > 30:
                memory = fill_memory(HIGH)
                print("[Diagnostics] Maintenance overdue. Generating service report.")
                issues_detected = random.randint(1, 5)
                print(f"[Diagnostics] {issues_detected} issues logged for technician review.")
            else:
                memory = fill_memory(LOW)
                print("[Diagnostics] Long uptime but recent maintenance. System stable.")
        else:
            memory = fill_memory(LOW)
            print("[Diagnostics] No issues detected. Routine scan complete.")
