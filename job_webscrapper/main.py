from bs4 import BeautifulSoup
import requests
import time
from datetime import date

def find_jobs():
    # Fetch HTML content from website, Parse HTML conten
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all job listings on the page
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

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
                with open(f'posts/jobs_{date.today()}.txt', 'a') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills}\n')
                    f.write(f'more_info: {more_info}\n')
                    f.write('\n')
    
    print(f'\nfile saved: jobs_{date.today()}.txt')
               

print('Enter some Skill that you are not familiar with:')
unfamiliar_skill = input('>').lower().replace(' ','')
print(f'\nfiltering out {unfamiliar_skill}...')

if __name__=='__main__':
    while True:
        find_jobs()
        wait_time=10
        print(f'\nwaiting for {wait_time} mins... or press ctrl+c to terminate loop')
        time.sleep(wait_time*60)

