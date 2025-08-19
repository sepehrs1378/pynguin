import time

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
    if light_level < 0:
        pass
    elif light_level < 30:
        if motion_detected:
            memory = fill_memory(HIGH)  # High memory for detailed lighting analysis
            if manual_override:
                memory = fill_memory(LOW)  # Manual mode uses simpler calculation
        else:
            memory = fill_memory(LOW)
    else:
        if light_level > 70:
            memory = fill_memory(HIGH)  # High memory for brightness adjustment
        else:
            memory = fill_memory(LOW)


def manage_temperature(current_temp: int, target_temp: int, eco_mode: bool):
    memory = fill_memory(LOW)
    if current_temp < target_temp - 5:
        if eco_mode:
            memory = fill_memory(LOW)  # Eco mode uses simpler heating
        else:
            memory = fill_memory(HIGH)  # Aggressive heating
    elif current_temp > target_temp + 5:
        memory = fill_memory(HIGH)  # Cooling requires more computation
    else:
        memory = fill_memory(LOW)  # Maintaining temperature


def security_check(window_open: bool, door_open: bool, alarm_armed: bool):
    memory = fill_memory(LOW)
    if alarm_armed:
        if window_open or door_open:
            memory = fill_memory(HIGH)  # Detailed security analysis
        else:
            memory = fill_memory(LOW)
    else:
        memory = fill_memory(LOW)  # System disarmed


def water_heater_control(water_usage: int, time_of_day: int, vacation_mode: bool):
    memory = fill_memory(LOW)
    if water_usage > 50:
        memory = fill_memory(HIGH)  # High water usage analysis
    else:
        if time_of_day > 8 and time_of_day < 22:
            if vacation_mode:
                memory = fill_memory(LOW)
            else:
                memory = fill_memory(HIGH)  # Peak time analysis
        elif time_of_day == 24:
            if vacation_mode:
                memory = fill_memory(LOW)
            else:
                memory = fill_memory(HIGH)
        else:
            memory = fill_memory(LOW)


def appliance_scheduler(time: int, day_type: bool, energy_saving: bool):
    memory = fill_memory(LOW)
    if day_type:  # Weekend
        if time > 10 and time < 20:
            memory = fill_memory(HIGH)  # More analysis during active hours
        else:
            memory = fill_memory(LOW)
    else:
        if energy_saving:
            memory = fill_memory(LOW)
        else:
            if time > 7 and time < 23:
                memory = fill_memory(HIGH)


def air_quality_control(co2_level: int, humidity: int, purifier_on: bool):
    memory = fill_memory(LOW)
    if co2_level < 0:
        pass
    elif 0 <= co2_level < 1000:
        if humidity < 0:
            pass
        elif humidity > 70 or humidity < 30:
            memory = fill_memory(HIGH)
        else:
            memory = fill_memory(LOW)
    else:
        memory = fill_memory(HIGH)  # Detailed air quality analysis
        if purifier_on:
            memory = fill_memory(HIGH) * 2  # Even more when purifier is on


def entertainment_system(volume: int, content_type: int, user_premium: bool):
    memory = fill_memory(LOW)
    if volume > 80:
        memory = fill_memory(HIGH)  # Loud volume needs more processing
    else:
        if content_type < 0 or content_type > 2:
            pass
        elif content_type == 0:  # Video
            if user_premium:
                memory = fill_memory(HIGH)  # 4K processing
            else:
                memory = fill_memory(LOW)  # HD processing
        elif content_type == 1:  # Music
            if user_premium:
                memory = fill_memory(HIGH)
            else:
                memory = fill_memory(LOW)
        elif content_type == 2:  # Pic
            if user_premium:
                memory = fill_memory(HIGH)
            else:
                memory = fill_memory(HIGH)


def irrigation_control(soil_moisture: int, weather_forecast: bool, season: int):
    memory = fill_memory(LOW)
    if soil_moisture < 30:
        if weather_forecast:  # Rain expected
            memory = fill_memory(HIGH)  # Detailed forecast analysis
        else:
            if season < 1 or season > 4:
                pass
            elif season in [2, 3, 4]:
                memory = fill_memory(HIGH)
            else:
                memory = fill_memory(LOW)
    else:
        memory = fill_memory(LOW)


def window_control(outside_temp: int, inside_temp: int, rain_detected: bool):
    memory = fill_memory(LOW)
    if outside_temp > inside_temp + 5:
        if rain_detected:
            memory = fill_memory(LOW)  # Keep windows closed
        else:
            memory = fill_memory(HIGH)  # Consider opening
    elif outside_temp < inside_temp - 5:
        memory = fill_memory(HIGH)  # Consider closing
    else:
        memory = fill_memory(LOW)


def energy_monitor(current_usage: int, time_peak: bool, solar_active: bool):
    memory = fill_memory(LOW)
    if current_usage > 5000:
        memory = fill_memory(HIGH)  # High usage analysis
    else:
        if time_peak:
            if solar_active:
                memory = fill_memory(HIGH)  # Complex solar integration
            else:
                memory = fill_memory(LOW)
        else:
            memory = fill_memory(LOW)


def safety_check(smoke_detected: bool, co_detected: bool, system_age: int):
    memory = fill_memory(LOW)
    if smoke_detected or co_detected:
        memory = fill_memory(HIGH)  # Emergency situation
    else:
        if system_age > 5:
            memory = fill_memory(HIGH)  # Detailed system check
        else:
            memory = fill_memory(LOW)


def user_profile_update(profile_age: int, activity_level: int, new_device: bool):
    memory = fill_memory(HIGH)
    if profile_age > 365:  # 1 year
        memory = fill_memory(HIGH)  # Long-term pattern analysis
    else:
        if activity_level > 5:
            if new_device:
                memory = fill_memory(HIGH)  # New device setup
            else:
                memory = fill_memory(LOW)
        else:
            memory = fill_memory(LOW)


def backup_system(backup_size: int, critical_data: bool, network_speed: int):
    memory = fill_memory(HIGH)
    if backup_size > 1000:
        if critical_data:
            memory = fill_memory(HIGH)  # Secure backup
        else:
            if network_speed < 0:
                pass
            elif network_speed > 50:
                memory = fill_memory(HIGH)  # Fast transfer
            else:
                memory = fill_memory(LOW)
    else:
        memory = fill_memory(LOW)


def system_diagnostics(error_count: int, uptime: int, last_maintenance: int):
    memory = fill_memory(HIGH)
    if error_count > 10:
        memory = fill_memory(HIGH)  # Detailed error analysis
    else:
        if uptime < 0:
            pass
        elif uptime > 1000:
            if last_maintenance > 30:
                memory = fill_memory(HIGH)  # Maintenance needed
            else:
                memory = fill_memory(LOW)
        else:
            memory = fill_memory(LOW)
