from challenge import Challenge

if __name__ == '__main__':
    try:
        challenge = Challenge()
        challenge.run()
    except KeyboardInterrupt:
        print("Finishing...")