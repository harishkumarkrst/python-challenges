import csv
import os


def extract_csv(filepath):
    if not os.path.exists(filepath):
        return []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def clean_record(record):
    cleaned = {
        k.strip(): v.strip() if isinstance(v, str) else v
        for k, v in record.items()
    }

    cleaned["salary"] = float(cleaned["salary"])
    cleaned["years"] = int(cleaned["years"])

    return cleaned


def filter_records(records, **criteria):
    return [
        r for r in records
        if all(r.get(key) == value for key, value in criteria.items())
    ]


def transform_salaries(records, multiplier):
    return [
        {
            **r,
            "salary": round(r["salary"] * multiplier, 2)
        }
        for r in records
    ]


def aggregate_by_department(records):
    groups = {}

    for record in records:
        dept = record["department"]

        if dept not in groups:
            groups[dept] = []

        groups[dept].append(record["salary"])


    result = {}

    for dept, salaries in groups.items():

        total = sum(salaries)

        result[dept] = {
            "count": len(salaries),
            "total_salary": total,
            "avg_salary": round(total / len(salaries), 2)
        }

    return result


def run_pipeline(filepath):

    # Extract
    records = extract_csv(filepath)

    # Transform
    cleaned_records = [
        clean_record(record)
        for record in records
    ]

    # Aggregate
    department_stats = aggregate_by_department(cleaned_records)

    return {
        "total_records": len(cleaned_records),
        "departments": department_stats
    }