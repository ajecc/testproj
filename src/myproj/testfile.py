import argparse
from clearml import Task

if __name__ == "__main__":
    task = Task.init(project_name="testproj", task_name="testfile")
    p = argparse.ArgumentParser()
    p.add_argument("config", type=argparse.FileType("r"))
    args = p.parse_args()
    print("got config", args.config)
    task.execute_remotely(queue_name="Eugene")
