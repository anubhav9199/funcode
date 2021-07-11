import subprocess


def main():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for profile in profiles:
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('utf-8').split('\n')

        results = [b.split(":")[1][1:-1]
                   for b in data if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(profile, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(profile, ""))



if __name__ == "__main__":
    main()
