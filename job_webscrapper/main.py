from bs4 import BeautifulSoup
import requests


print('Enter some Skill that you are not familiar with:')
unfamiliar_skill = input('>').lower().replace(' ','')
print(f'filtering out {unfamiliar_skill}...')

# Fetch HTML content from website
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

# Parse HTML content using BeautifulSoup library
soup = BeautifulSoup(html_text, 'lxml')

# Find all job listings on the page
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

# Loop through each job listing and print out details for jobs that were published "few" days ago
for job in jobs: 
    # Get the published date of the job listing
    published_date = job.find('span',class_ ='sim-posted').text.split('\n')[-2]
    
    # Check if the job was published "few" days ago
    if 'few' in published_date: 
        # Get the company name from the job listing
        company_name = job.find('h3', class_='joblist-comp-name').text.replace('\r','').replace('\n','').split('(')[0]
        
        # Get the required skills for the job listing
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','').replace('"','').replace('\r','').replace('\n','').lower()
        more_info = job.header.h2.a['href'] # I do this extract value of 'href' in 'a'tag
        
        # check is unfamiliar skill is not present
        if unfamiliar_skill not in skills: 
        
            print(f'Company Name: {company_name.strip()}')
            print(f'Required Skills: {skills}')
            print(f'more_info: {more_info}')
            print('')
