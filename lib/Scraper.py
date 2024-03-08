from bs4 import BeautifulSoup 
import requests

class Course:
    def __init__(self, title, schedule, description):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '------------------'
        return output

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        return BeautifulSoup(requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course in self.get_page().select('.post'):
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text  if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        for course in self.courses:
            print(course)

if __name__ == "__main__":
    scraper = Scraper()
    scraper.make_courses()
    scraper.print_courses()
