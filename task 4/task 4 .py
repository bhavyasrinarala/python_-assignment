#include <stdio.h>

int main()
{
    int id, senior, insurance;
    char name[50];

    float consultation, diagnostic, treatment;
    float total, discount = 0, finalBill;

    printf("Enter Patient ID: ");
    scanf("%d", &id);

    printf("Enter Patient Name: ");
    scanf("%s", name);

    printf("Enter Consultation Charges: ");
    scanf("%f", &consultation);

    printf("Enter Diagnostic Charges: ");
    scanf("%f", &diagnostic);

    printf("Enter Treatment Charges: ");
    scanf("%f", &treatment);

    if (consultation < 0 || diagnostic < 0 ||
        treatment < 0)
    {
        printf("Invalid Charges!");
        return 0;
    }

    printf("Senior Citizen (1-Yes, 0-No): ");
    scanf("%d", &senior);

    printf("Insurance Available (1-Yes, 0-No): ");
    scanf("%d", &insurance);

    if ((senior != 0 && senior != 1) ||
        (insurance != 0 && insurance != 1))
    {
        printf("Invalid Input!");
        return 0;
    }

    total = consultation + diagnostic + treatment;

    if (senior == 1)
        discount += total * 0.10;

    if (insurance == 1)
        discount += total * 0.05;

    finalBill = total - discount;

    printf("\n----- HOSPITAL BILL -----\n");
    printf("Patient ID: %d\n", id);
    printf("Patient Name: %s\n", name);
    printf("Total Charges: %.2f\n", total);
    printf("Total Concession: %.2f\n", discount);
    printf("Final Bill: %.2f\n", finalBill);

    if (finalBill > 10000)
        printf("Classification: HIGH PAYMENT");
    else if (finalBill >= 5000)
        printf("Classification: MEDIUM PAYMENT");
    else
        printf("Classification: LOW PAYMENT");

    return 0;
}
