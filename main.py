from challenge import Challenge

def main():
    """
    Main function to execute the web scraping process.

    This function initializes the Challenge class, runs the scraping process,
    and handles potential exceptions, such as KeyboardInterrupt or unexpected errors.

    Raises:
    - Exception: If an unexpected error occurs during the scraping process.
    """
    try:
        print("Starting the scraping process.")
        challenge = Challenge()
        challenge.run()
        print("Scraping process completed successfully.")
    except KeyboardInterrupt:
        print("Process interrupted by the user. Finishing...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        raise e

if __name__ == '__main__':
    main()
