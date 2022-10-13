import pyautogui as p
import time

run_all_button = 370, 75
reset_button = 555, 75


def click():
    p.mouseDown()
    time.sleep(0.1)
    p.mouseUp()
    time.sleep(0.1)


# wait for setup
time.sleep(10)

runs = 12

# basically, will take an hour for 100 epochs
time_per_epoch = 32.0
epochs = 200
extra_sleep_time = 180

print(
    f"Will finish in {(time_per_epoch * epochs + extra_sleep_time)*runs / 60} minutes"
)

time.sleep(time_per_epoch * epochs + extra_sleep_time)

for i in range(runs):
    # reset kernel
    p.moveTo(reset_button)
    click()
    time.sleep(5)

    # run all
    p.moveTo(run_all_button)
    click()

    time.sleep(time_per_epoch * epochs + extra_sleep_time)
