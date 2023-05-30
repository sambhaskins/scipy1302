class Runner:
    def run(data):
        print("\nI certify that this program is my own work\n" +
              "and is not the work of others. I agree not\n" +
              "to share my solution with others.\n" +
              "Sam Haskins")

        frequency = {}

        for item in data:
            frequency[item] = frequency.get(item, 0) + 1
            
        return list(frequency.values())
