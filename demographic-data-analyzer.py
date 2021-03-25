# coding=<UTF-8>

"""Program to fulfill project - "boilerplate-demographic-data-analyzer" - from
course Data-Analysis-With-Python, from freecodecamp.com"""

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Finds how many of each race are represented in dataset. Pandas series with race names as index labels.
    race_count = (df.groupby('race')['race'].count()).sort_values(ascending=False)

    # Finds the average age of men
    _sex_age = df[['sex', 'age']]
    _sex_age_df = _sex_age.set_index('sex')
    _sex_male_df = _sex_age_df.drop(['Female'], axis=0)
    _male_age_sum = _sex_male_df['age'].sum()
    _num_males = len(_sex_male_df)
    average_age_men = round(_male_age_sum / _num_males, 1)

    # Finds the percentage of people who have a Bachelor's degree
    _education = df.groupby('education')['education'].count()
    _bachelors = _education['Bachelors']
    percentage_bachelors = round((_bachelors / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    _education = df.groupby('education')['education'].count()
    _upper_ed_sum = _education[['Bachelors', 'Masters', 'Doctorate']].sum()

    _bachelors_fifty_k = (df['education'] == 'Bachelors') & (df['salary'] == '>50K')
    _masters_fifty_k = (df['education'] == 'Masters') & (df['salary'] == '>50K')
    _doctorate_fifty_k = (df['education'] == 'Doctorate') & (df['salary'] == '>50K')

    _over_fifty_k_percent = round((len(df[_bachelors_fifty_k]) + len(df[_masters_fifty_k]) +
                                   len(df[_doctorate_fifty_k])) / _upper_ed_sum * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    _low_ed_rich_mask = (df['salary'] == '>50K') & (df['education'] != 'Bachelors') & (df['education'] != 'Masters') \
        & (df['education'] != 'Doctorate')
    _low_ed_total_mask = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') \
        & (df['education'] != 'Doctorate')
    _percent_low_ed = round((len(df[_low_ed_rich_mask]) / len(df[_low_ed_total_mask])) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    _percent_w_high_ed = round((_upper_ed_sum / len(df)) * 100, 1)
    _percent_wo_high_ed = round(((len(df) - _upper_ed_sum) / len(df)) * 100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = _percent_w_high_ed
    lower_education = _percent_wo_high_ed

    # percentage with salary >50K
    higher_education_rich = _over_fifty_k_percent
    lower_education_rich = _percent_low_ed

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df['hours-per-week'].min()  # find the least amount of hours in a week that someone works
    _min_hours = df['hours-per-week'] == min_work_hours  # find all people who work the least amount of time in a week
    _min_hours_df = df[_min_hours]  # new dataframe for min_hours
    _rich_min_hours = _min_hours_df['salary'] == '>50K'  # finds people making over 50K that work min hours
    # finds percent for min hours who are rich
    _percent_rich_min_hours = round((len(_min_hours_df[_rich_min_hours]) / len(df[_min_hours])) * 100, 1)

    num_min_workers = len(df[_min_hours])
    rich_percentage = _percent_rich_min_hours

    # What country has the highest percentage of people that earn >50K?
    _foreign_total = df.groupby('native-country')['native-country'].count()
    _foreign_total = _foreign_total.drop(['United-States'], axis=0)  # remove United-States

    _highest_earning_country_df = df[df['salary'] == '>50K'].groupby('native-country')['native-country'].count()
    _highest_earning_country_df = _highest_earning_country_df.drop(['United-States'], axis=0)

    _highest_earning_country_df = (_highest_earning_country_df / _foreign_total)
    _a = _highest_earning_country_df.sort_values(ascending=False)  # sorted dataframe of highest_earning_country

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = _a.index[0]
    highest_earning_country_percentage = round(_highest_earning_country_df.max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    _india_df = df['native-country'] == 'India'
    _india_df = df[_india_df]
    _india_rich = _india_df['salary'] == '>50K'
    _india_rich = _india_df[_india_rich]
    _india_jobs = _india_rich.groupby('occupation')['occupation'].count()
    _india_jobs_sorted = _india_jobs.sort_values(ascending=False)

    top_IN_occupation = _india_jobs_sorted.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == '__main__':
    calculate_demographic_data()
    
