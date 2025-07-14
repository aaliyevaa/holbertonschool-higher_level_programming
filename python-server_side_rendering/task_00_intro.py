#!/usr/bin/env python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid data types")
        return
    if not template.strip():
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return

    for index, attendee in enumerate(attendees, start=1):
        filled_template = template

        for placeholder in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(placeholder)
            if value is None:
                value = 'N/A'
            filled_template = filled_template.replace(f'{{{placeholder}}}', str(value))


        output_file = f"output_{index}.txt"
        if os.path.exists(output_file):
            continue
        try:
            with open(output_file, 'w') as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Failed to write file {output_file}: {e}")
