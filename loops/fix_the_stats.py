# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

#The error is placing the variable (failed) inside a (for) function, which causes the value of the (failed) variable to reset to zero every time.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1
#The first error is that this line represents a change in the division type, making the result 30 instead of 30.0.
#The second error is that the print function was placed inside the for function, causing the process to repeat with each operation.
print(f"Average session: {total / count} minutes")

#The mistake is that it only reads the range from 1 to 3; we should write it as 4+1 so that it completes the count to 4.
for level in range(1, 4 + 1):
    print(f"level {level}")