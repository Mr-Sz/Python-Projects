from bs4 import BeautifulSoup
import requests

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
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','').replace('\r','').replace('\n','').split('(')[0]
        
        # Get the required skills for the job listing
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','').replace('"','').replace('\r','').replace('\n','')
        
        # Print out the details for the job listing
        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        ''')

# Add a commit message to indicate what changes were made to the code
print("Added commit messages to code")
