#!/usr/bin/env python3
import argparse
import json
import sys
import time

def main():
    parser = argparse.ArgumentParser(description="Generate standard tasks.")
    parser.add_argument('--n', type=int, default=5, help="Number of tasks to generate")
    args = parser.parse_args()

    print(f"Starting standard task generation (Target: {args.n} tasks)...")

    tasks = []
    for i in range(1, args.n + 1):
        time.sleep(0.1) # Simulate generation workload
        task = {
            "task_id": f"task_std_{i:03d}",
            "type": "standard",
            "complexity": "moderate",
            "description": f"Generated standard task #{i}"
        }
        tasks.append(task)
        print(f"-> Created {task['task_id']}")

    print(f"Successfully generated {len(tasks)} standard tasks.")
    sys.exit(0)

if __name__ == '__main__':
    main()