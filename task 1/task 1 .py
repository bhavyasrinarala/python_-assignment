#include <stdio.h>

struct Student
{
    char name[30];
    int roll;
    int marks[5];
    float attendance;
    float income;
    int total;
    float aggregate;
    int eligible;
};

int main()
{
    struct Student s[100], temp;
    int n, i, j, k;

    printf("Enter number of students: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        s[i].total = 0;
        s[i].eligible = 1;

        printf("\nEnter details of student %d\n", i+1);

        printf("Enter name: ");
        scanf("%29s", s[i].name);

        printf("Enter roll number: ");
        scanf("%d", &s[i].roll);

        printf("Enter marks of 5 subjects:\n");

        for(j = 0; j < 5; j++)
        {
            scanf("%d", &s[i].marks[j]);

            s[i].total += s[i].marks[j];

            if(s[i].marks[j] < 40)
                s[i].eligible = 0;
        }

        s[i].aggregate = s[i].total / 5.0;

        printf("Enter attendance percentage: ");
        scanf("%f", &s[i].attendance);

        printf("Enter annual family income: ");
        scanf("%f", &s[i].income);

        if(s[i].aggregate < 75 ||
           s[i].attendance < 75 ||
           s[i].income > 250000)
        {
            s[i].eligible = 0;
        }
    }

    // Sorting eligible students
    for(i = 0; i < n; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(s[i].eligible && s[j].eligible)
            {
                if(s[i].total < s[j].total ||
                  (s[i].total == s[j].total &&
                   s[i].attendance < s[j].attendance) ||
                  (s[i].total == s[j].total &&
                   s[i].attendance == s[j].attendance &&
                   s[i].income > s[j].income))
                {
                    temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
            }
        }
    }

    printf("\nUNIVERSITY SCHOLARSHIP RESULTS\n");

    printf("\nEligibility Status:\n");

    for(i = 0; i < n; i++)
    {
        if(s[i].eligible)
            printf("%s - Eligible\n", s[i].name);
        else
            printf("%s - Not Eligible\n", s[i].name);
    }

    printf("\nSCHOLARSHIP MERIT LIST\n");
    printf("\nRank\tName\tRoll No\tAggregate\n");

    k = 1;

    for(i = 0; i < n; i++)
    {
        if(s[i].eligible)
        {
            printf("%d\t%s\t%d\t%.2f%%\n",
                   k, s[i].name, s[i].roll,
                   s[i].aggregate);
            k++;
        }
    }

    printf("\nScholarship allocation completed.\n");

    return 0;
}
