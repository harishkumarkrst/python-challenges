import csv
import os


def write_file(filepath, content):
    """
    Write content to file.
    """
    with open(filepath, "w") as f:
        f.write(content)


def read_file(filepath):
    """
    Read entire file content.
    """
    with open(filepath, "r") as f:
        return f.read()


def count_lines(filepath):
    """
    Count non-empty lines.
    """
    with open(filepath, "r") as f:
        lines = f.readlines()

    return len([line for line in lines if line.strip()])


def write_csv(filepath, headers, rows):
    """
    Write CSV file.
    """
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        for row in rows:
            writer.writerow(row)


def read_csv(filepath):
    """
    Read CSV and return list of dictionaries.
    """
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)

        return list(reader)


def search_in_file(filepath, keyword):
    """
    Find lines containing keyword.
    """
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [
        line.strip()
        for line in lines
        if keyword in line
    ]
