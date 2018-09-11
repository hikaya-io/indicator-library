import csv
from indicatorlibrary.quickstart.models import Indicator
with open('indicator_new.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        p = Indicator(level = row[0],name = row[2], sector =row[5], subsector=row[6], number = row[1], definition = row[7],justification = row[8], unit_of_measure = row[9], disaggregation = row[11], direction_of_change = row[12], baseline = row[13], rationale_for_target = row[15], means_of_verification = row[16], question_format = row[17], data_collection_method = row[18], denominator = row[20], numerator = row[21], responsible_person = row[22], method_of_analysis = row[23], information_use = row[24], quality_assurance = row[26], data_issues = row[27],indicator_changes = row[28], comments = row[29])
        p.save()
