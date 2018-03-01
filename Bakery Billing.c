/*Backery Billing system 
version 5.33
author Siddhant Saurabh k1630_b46 LOVELY PROFESSIONAL UNIVERSITY*/

#include<stdio.h>
#include<stdlib.h>  //for clearing screen funtions and using dos functions
#include<string.h>	//for copying name of products to bill

// structure for each product description
struct product
{
	char name[20];
	long id;
	float price;
};

// structure for each bill
struct bill
{
	long bill_id;
	int no_of_items;
	char customer_name[20];
	char date[20];
	char product_name[30][20];
	long product_id[30];
	float product_price[30];
	int quantity[30];
	float total_cost;
};

//different funtions prototype
void additem();
void generateBill();
void displayBill();
void deleteBill();
void siddhant();


// for home page
void main()
{
	int hp_choice=0;
	system("cls");
	printf("\n Welcome to Bakery Billing System");
	printf("\n ================================");
	printf("\n 1 ADD PRODUCT \n 2 GENERATE A BILL \n 3 DISPLAY A BILL \n 4 DELETE A BILL \n 5 EXIT \n ================================================== \n PRESS CORRESPONDING KEYS TO PERFORM THE OPERATIONS:  ");   
	scanf("%d",&hp_choice);
	
	//choice 
	switch(hp_choice)
	{
		case 1:
			additem();
			break;
		case 2:
			generateBill();
			break;
		case 3:
			displayBill();
			break;
		case 4:
			deleteBill();
			break;
		default:
			siddhant();
	}
}

// add item function and its details
void additem()
{
	int pg_choice;
	long id;
	FILE *add_f_pt;
	int add_f_choice=1;
	system("cls");

	struct product p;

	id=0;
	// method for finding the maximum p.id 
	add_f_pt=fopen("item","rb");
	if(add_f_pt!=0)
		while(fread(&p,sizeof(p),1,add_f_pt)==1)
			if(id<p.id)
				id=p.id;
	fclose(add_f_pt);
	
	
	while(add_f_choice==1)
	{
		// inputting items values
		printf(" ============================================\n");
		printf(" ENTER PRODUCT NAME: ");
		fflush(stdin);
		gets(p.name);
		printf(" ENTER PRODUCT PRICE: ");
		scanf("%f",&p.price);
		p.id=(++id);
		
		// writing structure ta item.txt
		add_f_pt=fopen("item","ab");
		fwrite(&p,sizeof(p),1,add_f_pt);
		fclose(add_f_pt);
		
		printf(" ============================================ \n YOUR PRODUCT WITH ID %d IS ADDED SUCCESSFULLY",p.id);
		
		printf("\n \n ================================================== \n PRESS 1 TO ADD NEW PRODUCT OR ANY KEY TO EXIT: ");
		scanf("%d",&add_f_choice);
	}
	
//	add_f_pt=fopen("item","rb");
//	if(add_f_pt!=0)
//	{
//		while(fread(&p,sizeof(p),1,add_f_pt)!=0)
//		{
//			printf("\n %s \t %f \t %d",p.name,p.price,p.id);
//		}
//	}
	
	printf("\n ======================================================\n PRESS 1 TO GO TO MAIN MENU AND 0 TO EXIT: ");
	scanf("%d",&pg_choice);
	if(pg_choice==1)
	main();
	else
	siddhant();
}



void generateBill()
{
	int pg_choice;
	int gen_f_choice=1;
	long b_id,p_id; // b_id is for generating id and p_id is for storing the inputted id.
	int i=-1; // for storing no. of items temporarly
	int j=0; //for using loop for printing
	int f;
	int gen_f_choice2=0;
	struct product p;
	struct bill b;
	FILE *gen_f_pt_p;
	FILE *gen_f_pt_b;
	
	system("cls");
	
	b_id=999;
	// method for finding the maximum b.id 
	gen_f_pt_b=fopen("bill","rb");
	if(gen_f_pt_b!=0)
		while(fread(&b,sizeof(b),1,gen_f_pt_b)==1)
			if(b_id<b.bill_id)
				b_id=b.bill_id;
	fclose(gen_f_pt_b);
	printf("\n JUST ENTER PRODUCT ID OF BUYING PRODUCT TO CALCULATE BILL \n ===============================================================\n");
	b.total_cost=0;
	while(gen_f_choice==1)
	{
		//inputing product id and checking and then initialization of the stucture bill b and then writing
		printf("\n ENTER PRODUCT ID: ");
		scanf("%ld",&p_id);
		gen_f_pt_p=fopen("item","rb");
		if(gen_f_pt_p!=0)
		{
			f=0;
			while(fread(&p,sizeof(p),1,gen_f_pt_p)!=0)   //loop for checking id
			{
				if(p.id==p_id)
				{
					i++;
					printf(" PRODUCT NAME- %s    PRODUCT PRICE- %.2f",p.name,p.price);
					strcpy(b.product_name[i],p.name);
					b.product_price[i]=p.price;
					b.product_id[i]=p.id;
					printf("\n ENTER QUANTITY OF PRODUCT- ");
					scanf("%d",&b.quantity[i]);
					b.total_cost +=(b.quantity[i]*b.product_price[i]);
					f=1;
					break;
				}
				
			}
			if(f==0)
			printf("\n ITEM NOT FOUND");
		}
		else
		{
			printf("\n =======================================\n THE FILE ITEM NOT FOUND");
		}
		fclose(gen_f_pt_p);	
		
		printf("\n ==========================================================\n PRESS 1 TO ADD MORE PRODUCT OTHERWISE 0 TO GO TO BILL PAGE: ");
		scanf("%d",&gen_f_choice);
	}
	// if flag is positive
	if(f==1)
	{
		printf("\n ======================================================\n PUT DOWN CUSTOMER DETAILS: \n CUSTOMER NAME: ");
		fflush(stdin);
		gets(b.customer_name);
		b.bill_id=++b_id;
		b.no_of_items=i+1;
		printf("\n ENTER DATE: ");
		gets(b.date);
		fflush(stdin);
		// writing structure to the file bill
		gen_f_pt_b=fopen("bill","ab");
		fwrite(&b,sizeof(b),1,gen_f_pt_b);
		fclose(gen_f_pt_b);
		
		printf("\n PRESS 1 TO GENERATE THE BILL : ");
		scanf("%d",&gen_f_choice2);
		if(gen_f_choice2==1)
		{	//displaying the details of the bill
			system("cls");
			printf("\n ===================================================================== \n 		BAKERY BILLING SYSTEM \n");
			printf("\n Customer Name: %s  Bill ID %ld  Date %s \n =====================================================================",b.customer_name,b.bill_id,b.date);
			printf("\n Sr No               Item Name      Price  Quantity    Total");
			for(j=0;j<b.no_of_items;j++)
			{
				printf("\n %5d    %20s    %7.2f  %8d    %.2f",j+1,b.product_name[j],b.product_price[j],b.quantity[j],b.product_price[j]*b.quantity[j]);
			}
			printf("\n =====================================================================\n Total Bill- %.2f",b.total_cost);
		}
	}
	printf("\n =====================================================================\n PRESS 1 TO GENERATE ANOTHER BILL, 2 TO GO TO MAIN MENU AND 0 TO EXIT:  ");
	scanf("%d",&pg_choice);
	if(pg_choice==2)
	main();
	else if(pg_choice==1)
	generateBill();
	else
	siddhant();
}





void displayBill()
{
	int pg_choice;
	long id;
	struct bill b;
	FILE *dis_f_pt;
	int j=0; //for using loop for printing
	int f=0;
	system("cls");
	printf("\n PLEASE ENTER YOUR BILL ID- ");
	scanf("%ld",&id);
	
	dis_f_pt=fopen("bill","rb");
	if(dis_f_pt!=0)	// checking the file exitance
	{
		while(fread(&b,sizeof(b),1,dis_f_pt)!=0)	// checking the end of file
		{
			if(b.bill_id==id)
			{	// printing the details of bill if the bill id is found
				f=1;
				printf("\n =====================================================================\n 		BAKERY BILLING SYSTEM");
				printf("\n Customer Name: %s    Bill ID %ld    Date %s \n =====================================================================",b.customer_name,b.bill_id,b.date);
				printf("\n Sr No               Item Name      Price  Quantity    Total \n =====================================================================");
				for(j=0;j<b.no_of_items;j++)
				{
					printf("\n %5d    %20s    %7.2f  %8d    %.2f",j+1,b.product_name[j],b.product_price[j],b.quantity[j],b.product_price[j]*b.quantity[j]);
				}
				printf("\n ===================================================================== \n Total Bill- %.2f",b.total_cost);
				break;
			}
			
		}
		if(f==0)	// checking the flag value ,it returns exclamation if no bill id matched
			printf("\n =======================================\n WRONG BILL ID ENTERED");
	}
	else
	{
		printf("\n ========================================\n THE FILE BILL NOT FOUND");
	}
	fclose(dis_f_pt);	
	
	printf("\n =====================================================================\n PRESS 1 TO DISPLAY ANOTHER BILL, 2 TO GO TO MAIN MENU AND 0 TO EXIT:  ");
	scanf("%d",&pg_choice);
	if(pg_choice==2)
	main();
	else if(pg_choice==1)
	displayBill();
	else
	siddhant();
}




void deleteBill()
{
	int pg_choice;
	system("cls");
	long id;
	int f=0; //flag for sucessfull changes made
	struct bill b;
	
	FILE *del_f_pt_n;
	FILE *del_f_pt_o;
	
	system("cls");
	printf("\n PLEASE ENTER YOUR BILL ID- ");
	scanf("%ld",&id);
	
	
	del_f_pt_o=fopen("bill","rb");
	if(del_f_pt_o!=0)
	{
		while(fread(&b,sizeof(b),1,del_f_pt_o)!=0)
		{	
			if(b.bill_id==id)
			{
				f=1;
				continue;
			}
			else
			{
				del_f_pt_n=fopen("Temp_bill","ab");
				fwrite(&b,sizeof(b),1,del_f_pt_n);
				fclose(del_f_pt_n);
			}
		}
		fclose(del_f_pt_o);
		
		if(f==1)
		{
			system("del bill");	// deleting bill
			system("RENAME Temp_bill bill"); //system rename temp_bill to bill
			printf("\n =================================================\n YOUR BILL HAS BEEN DELETED SUCCESSFULLY");
		}
		else
		{
			system("del Temp_bill");	//system delete temp_bill
			printf("\n ==================================\n WRONG BILL ID ENTERED");
		}
	}
	else
	{
		printf("\n ==============================\n THE FILE BILL NOT FOUND");
	}
	
	
	
	printf("\n ================================================\n PRESS 1 TO DELETE ANOTHER BILL, 2 TO GO TO MAIN MENU AND 0 TO EXIT:  ");
	scanf("%d",&pg_choice);
	if(pg_choice==2)
	main();
	else if(pg_choice==1)
	deleteBill();
	else
	siddhant();
}

void siddhant()
{
	system("cls");
	printf("\n    Lovely Professional University \n           Siddhant Saurabh \n             11602270 B46\n    Thankyou for using my software.\n \n \n ===================================================");
	sleep(2);
	exit(1);
}
