#!/usr/bin/env python3
import argparse
import json
import sys
import time

def main():
    parser = argparse.ArgumentParser(description="Generate stratified tasks.")
    parser.add_argument('--n', type=int, default=5, help="Number of tasks to generate per stratum")
    args = parser.parse_args()

    print(f"Starting stratified task generation (Target: {args.n} tasks per stratum)...")

    strata = ["easy", "medium", "hard"]
    all_tasks = []

    for stratum in strata:
        print(f"--- Processing stratum: {stratum} ---")
        for i in range(1, args.n + 1):
            time.sleep(0.05)
            task = {
                "task_id": f"task_{stratum}_{i:03d}",
                "type": "stratified",
                "stratum": stratum,
                "description": f"Generated stratified task ({stratum}) #{i}"
            }
            all_tasks.append(task)
            print(f"-> Created {task['task_id']}")

    print(f"Successfully generated total of {len(all_tasks)} stratified tasks across {len(strata)} tiers.")
    sys.exit(0)

if __name__ == '__main__':
    main()