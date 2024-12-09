def read_reports(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            # Convert the line into a list of integers
            reports.append(list(map(int, line.split())))
    return reports

def is_safe_report(report):
    # Check if the levels are all increasing or all decreasing
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    if not (is_increasing or is_decreasing):
        return False
    
    # Check if differences between adjacent levels are between 1 and 3 (inclusive)
    is_valid_difference = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return is_valid_difference

def classify_reports(reports):
    classifications = []
    safe_count = 0
    for report in reports:
        is_safe = is_safe_report(report)
        classifications.append(is_safe)
        if is_safe:
            safe_count += 1
    return classifications, safe_count

def classify_reports_with_dampener(reports):
    classifications, safe_count = classify_reports(reports)

    for i, (report, is_safe) in enumerate(zip(reports, classifications)):
        if not is_safe:
            # Check if removing any level makes the report safe
            for j in range(len(report)):
                modified_report = report[:j] + report[j+1:]  # Remove the j-th level
                if is_safe_report(modified_report):
                    classifications[i] = True  # Update classification to safe
                    safe_count += 1            # Increase safe count
                    break  # Stop further checks as the report is now classified as safe

    return classifications, safe_count


reports = read_reports('inputs/input2.txt')

# Part 1
classifications, safe_count = classify_reports(reports)

print(f"Safe reports: {safe_count}")

# Part 2 
classifications, safe_count = classify_reports_with_dampener(reports)
print(f"Safe reports: {safe_count}")
