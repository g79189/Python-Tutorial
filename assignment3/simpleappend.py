file_path="output.txt"
with open(file_path,'a') as file:
  chars_written=file.write('New log entry \n')
  print(f"Added {chars_written} characters to {file_path}")
