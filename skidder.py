import time
import random
import sys
import os

class SkidderSimulator:
    def __init__(self, target):
        self.target = target
        self.stages = [
            "initializing connection to target",
            "performing reconnaissance and footprinting",
            "scanning for open ports and services",
            "analyzing service versions",
            "searching for known vulnerabilities",
            "preparing exploit payloads",
            "delivering exploit payload",
            "establishing remote shell access",
            "escalating privileges on target system",
            "extracting sensitive files and credentials",
            "creating persistent backdoor",
            "covering tracks by clearing logs",
            "disconnecting cleanly from target"
        ]
        self.success_messages = [
            "exploit executed successfully",
            "remote shell established",
            "privilege escalation successful",
            "data extraction complete",
            "backdoor created",
            "logs cleared",
            "operation completed"
        ]
        self.log_file = "skidder_operation.log"

    def print_with_delay(self, message, delay=0.03):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def simulate_stage(self, stage):
        self.print_with_delay(f"[+] {stage}...")
        time.sleep(random.uniform(1.5, 3.0))
        success_msg = random.choice(self.success_messages)
        self.print_with_delay(f"[✓] {success_msg}\n")
        self.write_log(f"{stage} - {success_msg}")

    def write_log(self, log_entry):
        with open(self.log_file, "a") as log:
            log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {log_entry}\n")

    def run(self):
        self.print_with_delay(f"Starting skid operation on target: {self.target}\n", delay=0.05)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)  # clear old logs
        for stage in self.stages:
            self.simulate_stage(stage)
        self.print_with_delay(f"Skid operation on {self.target} finished successfully 💀🔥")

if __name__ == "__main__":
    target_ip = "192.168.1.100"  # replace with your target ip or whatever
    skidder = SkidderSimulator(target_ip)
    skidder.run()
