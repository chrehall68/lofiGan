import pyautogui as p
import time

run_all_button = 370, 75
reset_button = 555, 75


def write_file_conf(file, batch_size, epoch_size, start_pos):
    with open("./config.env", "w") as f:
        f.write(f"FILE={file}\n")
        f.write(f"BATCH_SIZE={batch_size}\n")
        f.write(f"EPOCH_SIZE={epoch_size}\n")
        f.write(f"START_POS={start_pos}\n")
        f.close()


def click():
    p.mouseDown()
    time.sleep(0.1)
    p.mouseUp()
    time.sleep(0.1)


file_confs = [
    ("lofi-part1.wav", "100", "200", "0"),
    ("lofi-part1.wav", "100", "200", "200"),
    ("lofi-part2.wav", "100", "200", "0"),
    ("lofi-part2.wav", "100", "200", "200"),
    ("lofi-part4.wav", "100", "200", "0"),
    ("lofi-part4.wav", "100", "200", "92"),
    ("lofi-part5.wav", "100", "200", "0"),
    ("lofi-part5.wav", "100", "200", "192"),
    ("lofi-part6.wav", "100", "200", "0"),
    ("lofi-part6.wav", "100", "200", "80"),
    ("lofi-part7.wav", "100", "200", "0"),
    ("lofi-part8.wav", "100", "200", "0"),
    ("lofi-part9.wav", "100", "200", "0"),
    ("lofi-part10.wav", "100", "200", "0"),
    ("lofi-part11.wav", "100", "200", "0"),
    ("lofi-part12.wav", "100", "200", "0"),
    ("lofi-part13.wav", "100", "200", "0"),
    ("lofi-part14.wav", "100", "200", "0"),
]

# wait for setup
time.sleep(10)
print(f"Will finish in {(7 * 400 + 310)*len(file_confs) / 60} minutes")

for file_conf in file_confs:
    write_file_conf(*file_conf)
    time.sleep(5)

    # reset kernel
    p.moveTo(reset_button)
    click()
    time.sleep(5)

    # run all
    p.moveTo(run_all_button)
    click()

    time.sleep(7 * 400 + 300)
