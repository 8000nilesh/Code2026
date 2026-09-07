import scrapy

class GovernmentScrapper(scrapy.Spider):
    name = 'gov'
    custom_settings = {
        'LOG_LEVEL': 'WARNING',
    }
    start_urls = [
        'https://egazette.gov.in/RecentUploads.aspx?Category=3'
    ]

    def parse(self, response):
        subjects = response.css(
            "span[id^='gvGazetteList_lbl_Subject_'] ::text"
        ).getall()

        cleaned_subjects = [
            ' '.join(subject.split()) for subject in subjects if subject.strip()
        ]

        print("\nTop 5 subjects:")
        for number, subject in enumerate(cleaned_subjects[:5], start=1):
            print(f"{number}. {subject}\n")