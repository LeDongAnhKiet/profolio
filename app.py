from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Lê Đông Anh Kiệt',
                           job_title='Data Analyst',
                           about='Eager to apply my data analysis expertise to identify actionable insights and support data-driven decision-making.',
                           skills=['Python', 'PHP', 'C++', 'C#', 'SQL', 'Data Analysis', 'Machine Learning'],
                           projects=[
                               {'name': 'World Happiness Report', 'description': 'Analyzed data and uncovered GDP correlations', 'link': 'https://github.com/LeDongAnhKiet/World_Happiness_Report'},
                               {'name': 'LS Consulting Website', 'description': 'Developed a homepage for an interior design company', 'link': 'https://lsmodel.vn'},
                               {'name': 'Housing Price Prediction', 'description': 'Built regression models for price analysis', 'link': 'https://github.com/LeDongAnhKiet/House_Pricing_Prediction'}
                           ],
                           experience=[
                               {'role': 'Programmer Intern', 'company': 'Thien Long Group', 'duration': 'Oct 2023 - Jan 2024'},
                               {'role': 'Developer Collaborator', 'company': 'Enjoy Sport', 'duration': 'Jan 2024 - Mar 2024'},
                               {'role': 'Developer Collaborator', 'company': 'CBTech', 'duration': 'Oct 2024 - Now'}
                           ],
                           contact={'email': 'ledonganhkiet1909@gmail.com', 'linkedin': 'https://linkedin.com/in/keithle1909', 'github': 'https://github.com/LeDongAnhKiet'})

if __name__ == '__main__':
    app.run(debug=True)
