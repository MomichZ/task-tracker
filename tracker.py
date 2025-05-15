def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(f"{task}\n")

if __name__ == "__main__":
    add_task("Первая задача")
