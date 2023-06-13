import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        print("\r" + "Cargando :) " + animation[i % len(animation)], end="")


spinner = loading_animation()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')