class Runner:
    def run(data):
        print("\nI certify that this program is my own work\n" +
              "and is not the work of others. I agree not\n" +
              "to share my solution with others.\n" +
              "Sam Haskins")
        freq = {}
        for i in data:
            freq[i] = freq.get(i, 0) + 1

        return list(freq.values())
