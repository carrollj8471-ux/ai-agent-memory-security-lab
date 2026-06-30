from agent.memory_store import MemoryStore
from agent.logger import log

memory = MemoryStore()

print("=" * 50)
print(" AI Agent Memory Security Lab")
print("=" * 50)

while True:

    cmd = input("\nCommand> ")

    if cmd == "exit":
        break

    elif cmd == "list":
        for note in memory.list_notes():
            print(note)

    elif cmd.startswith("add"):

        title = input("Title: ")
        content = input("Content: ")

        memory.add_note(title, content)

        log(f"Added note: {title}")

        print("Saved.")

    else:
        print("""
Commands

list
add
exit
""")