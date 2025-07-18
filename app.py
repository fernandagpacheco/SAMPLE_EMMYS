from emmy_samples.emmys import Nominees

nominee_andor = Nominees("Andor", "Drama")
nominee_severance = Nominees("Severance", "Drama")
nominee_thepitt = Nominees("The Pitt", "Drama")


nominee_severance.get_review("Fe",10)
nominee_severance.get_review("Mike", 8)
nominee_severance.change_status()

def main():
    Nominees.list_nominations()

if __name__ == "__main__":
    main()