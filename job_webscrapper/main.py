from bs4 import BeautifulSoup  
import requests  
import time  
from datetime import date  

def find_jobs():
    # Fetch HTML content from website, Parse HTML content
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
            
            # Check if unfamiliar skill is not present and the job details are not already in the file
            if unfamiliar_skill not in skills:
                with open(f'posts/jobs_{date.today()}.txt', 'a+') as f:
                    # Move the file pointer to the beginning of the file and read the entire content of the file
                    f.seek(0)  
                    data = f.read()  
                    # Check if job details are already in the file and skip writing to the file if the data already exists
                    if f'Company Name: {company_name.strip()}\nRequired Skills: {skills}\nmore_info: {more_info}\n' in data:
                        continue  # Skip writing to the file
                        
                    # Write the job details to the file if it's not already present
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills}\n')
                    f.write(f'more_info: {more_info}\n')
                    f.write('\n')  # Add an empty line between job listings
                    
    # Print a message indicating that the file has been saved
    print(f'\nFile saved: jobs_{date.today()}.txt')

# Ask the user to enter an unfamiliar skill
print('Enter some skill that you are not familiar with:')
unfamiliar_skill = input('>').lower().replace(' ','')

# Print a message indicating that the filtering is in progress
print(f'\nFiltering out {unfamiliar_skill}...')

# Run the job search continuously
if __name__=='__main__':
    while True:
        find_jobs()
        wait_time=10  # Set the wait time between job searches
        print(f'\nWaiting for {wait_time} mins... or press ctrl+c to terminate loop')
        time.sleep(wait_time*60)  # Wait for the specified time before running the job search again
