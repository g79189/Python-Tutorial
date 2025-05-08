def log_event (event, log_file='app.log'):
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{timestamp}] {event}\n'
    with open(log_file, 'a') as file:
        file.write(log_entry)
        print(f"Logged: {log_entry.strip()}")
        
if __name__ == "__main__":
    log_event("Application Started")
    log_event("User logged in: Greg")
    log_event("Error database connection failed.")
    
    
   