# Changes in memory usage start to show from C = 100_000.
LOW = 100_000  # 1_000_000
HIGH = 10_000_000  # 10_000_000


# Smart Home Control System Simulation
def control_lighting(light_level: int, motion_detected: bool, manual_override: bool):
    if light_level < 30:
        if motion_detected:
            memory = [0] * HIGH  # High memory for detailed lighting analysis
            if manual_override:
                memory = [0] * LOW  # Manual mode uses simpler calculation
        else:
            memory = [0] * LOW
    else:
        if light_level > 70:
            memory = [0] * HIGH  # High memory for brightness adjustment
        else:
            memory = [0] * LOW


def manage_temperature(current_temp: int, target_temp: int, eco_mode: bool):
    if current_temp < target_temp - 5:
        if eco_mode:
            memory = [0] * LOW  # Eco mode uses simpler heating
        else:
            memory = [0] * HIGH  # Aggressive heating
    elif current_temp > target_temp + 5:
        memory = [0] * HIGH  # Cooling requires more computation
    else:
        memory = [0] * LOW  # Maintaining temperature


def security_check(window_open: bool, door_open: bool, alarm_armed: bool):
    if alarm_armed:
        if window_open or door_open:
            memory = [0] * HIGH  # Detailed security analysis
        else:
            memory = [0] * LOW
    else:
        memory = [0] * LOW  # System disarmed


def water_heater_control(water_usage: int, time_of_day: int, vacation_mode: bool):
    if water_usage > 50:
        memory = [0] * HIGH  # High water usage analysis
    else:
        if time_of_day > 8 and time_of_day < 22:
            if vacation_mode:
                memory = [0] * LOW
            else:
                memory = [0] * HIGH  # Peak time analysis
        else:
            memory = [0] * LOW


def appliance_scheduler(time: int, day_type: bool, energy_saving: bool):
    if day_type:  # Weekend
        if time > 10 and time < 20:
            memory = [0] * HIGH  # More analysis during active hours
        else:
            memory = [0] * LOW
    else:
        if energy_saving:
            memory = [0] * LOW
        else:
            if time > 7 and time < 23:
                memory = [0] * HIGH


def air_quality_control(co2_level: int, humidity: int, purifier_on: bool):
    if co2_level > 1000:
        memory = [0] * HIGH  # Detailed air quality analysis
        if purifier_on:
            memory = [0] * HIGH * 2  # Even more when purifier is on
    else:
        if humidity > 70 or humidity < 30:
            memory = [0] * HIGH
        else:
            memory = [0] * LOW


def entertainment_system(volume: int, content_type: bool, user_premium: bool):
    if volume > 80:
        memory = [0] * HIGH  # Loud volume needs more processing
    else:
        if content_type:  # Video
            if user_premium:
                memory = [0] * HIGH  # 4K processing
            else:
                memory = [0] * LOW  # HD processing
        else:  # Audio
            memory = [0] * LOW


def irrigation_control(soil_moisture: int, weather_forecast: bool, season: int):
    if soil_moisture < 30:
        if weather_forecast:  # Rain expected
            memory = [0] * HIGH  # Detailed forecast analysis
        else:
            if season > 2:  # Summer
                memory = [0] * HIGH
            else:
                memory = [0] * LOW
    else:
        memory = [0] * LOW


def window_control(outside_temp: int, inside_temp: int, rain_detected: bool):
    if outside_temp > inside_temp + 5:
        if rain_detected:
            memory = [0] * LOW  # Keep windows closed
        else:
            memory = [0] * HIGH  # Consider opening
    elif outside_temp < inside_temp - 5:
        memory = [0] * HIGH  # Consider closing
    else:
        memory = [0] * LOW


def energy_monitor(current_usage: int, time_peak: bool, solar_active: bool):
    if current_usage > 5000:
        memory = [0] * HIGH  # High usage analysis
    else:
        if time_peak:
            if solar_active:
                memory = [0] * HIGH  # Complex solar integration
            else:
                memory = [0] * LOW
        else:
            memory = [0] * LOW


def safety_check(smoke_detected: bool, co_detected: bool, system_age: int):
    if smoke_detected or co_detected:
        memory = [0] * HIGH  # Emergency situation
    else:
        if system_age > 5:
            memory = [0] * HIGH  # Detailed system check
        else:
            memory = [0] * LOW


def user_profile_update(profile_age: int, activity_level: int, new_device: bool):
    if profile_age > 365:  # 1 year
        memory = [0] * HIGH  # Long-term pattern analysis
    else:
        if activity_level > 5:
            if new_device:
                memory = [0] * HIGH  # New device setup
            else:
                memory = [0] * LOW
        else:
            memory = [0] * LOW


def backup_system(backup_size: int, critical_data: bool, network_speed: int):
    if backup_size > 1000:
        if critical_data:
            memory = [0] * HIGH  # Secure backup
        else:
            if network_speed > 50:
                memory = [0] * HIGH  # Fast transfer
            else:
                memory = [0] * LOW
    else:
        memory = [0] * LOW


def system_diagnostics(error_count: int, uptime: int, last_maintenance: int):
    if error_count > 10:
        memory = [0] * HIGH  # Detailed error analysis
    else:
        if uptime > 1000:
            if last_maintenance > 30:
                memory = [0] * HIGH  # Maintenance needed
            else:
                memory = [0] * LOW
        else:
            memory = [0] * LOW
