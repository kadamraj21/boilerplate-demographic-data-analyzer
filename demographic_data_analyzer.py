import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Advanced education vs salary >50K
    higher_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_ed = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_ed_rich = round((higher_ed['salary'] == '>50K').sum() / len(higher_ed) * 100, 1)
    lower_ed_rich = round((lower_ed['salary'] == '>50K').sum() / len(lower_ed) * 100, 1)

    # 5. Min work hours
    min_hours = df['hours-per-week'].min()

    # 6. Rich % among those who work min hours
    rich_min_workers = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')]
    rich_percentage = round(
        len(rich_min_workers) / len(df[df['hours-per-week'] == min_hours]) * 100, 1)

    # 7. Country with highest % of >50K
    country_total = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_ratio = (country_rich_counts / country_total) * 100

    highest_earning_country = rich_country_ratio.idxmax()
    highest_earning_country_percentage = round(rich_country_ratio.max(), 1)

    # 8. Top occupation in India (>50K)
    top_IN_occupation = df[
        (df['salary'] == '>50K') & (df['native-country'] == 'India')
    ]['occupation'].mode()[0]

    if print_data:
        print("Race Count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_ed_rich)
        print("Percentage without higher education that earn >50K:", lower_ed_rich)
        print("Min work time:", min_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_ed_rich,
        'lower_education_rich': lower_ed_rich,
        'min_work_hours': min_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }