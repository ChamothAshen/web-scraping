import os
from dotenv import load_dotenv
from scraper import LinkedInScraper
from utils import save_to_csv

def main():
    print("=== LinkedIn Profile Scraper ===")

    load_dotenv()
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")

    if not email or not password:
        print("❌ Please set your LINKEDIN_EMAIL and LINKEDIN_PASSWORD in .env file")
        return

    # --- Enable headless mode ---
    scraper = LinkedInScraper(email, password, headless=True)
    scraper.login()

    profile_url = input("Enter LinkedIn Profile URL: ")
    data = scraper.scrape_profile(profile_url)

    print("\n--- Scraped Profile ---")
    print("Name:", data["name"])
    print("Job Title:", data["job_title"])
    print("Location:", data["location"])

    print(f"Debug: Scraped data: {data}")  # Debug log

    output_file = input("Enter output CSV file path (e.g., data/profiles.csv): ")
    save_to_csv(data, output_file)
    print(f"✅ Data saved to {output_file}")

    scraper.close()

if __name__ == "__main__":
    main()
