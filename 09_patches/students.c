#include <stdio.h>
#include <string.h>
struct Student {
    int id;
    char name[50];
    char sex[1];
};
void printStudents(struct Student students[], int count) {
    printf("List of students:\n");
    for (int i = 0; i < count; i++) {
        printf("ID: %d, Name: %s, Sex: %s.\n", students[i].id, students[i].name,students[i].sex);
    }
}
void findStudentById(struct Student students[], int count, int id) {
    for (int i = 0; i < count; i++) {
        if (students[i].id == id) {
            printf("Student found: ID: %d, Name: %s\n", students[i].id, students[i].name);
            return;
        }
    }
    printf("Student with ID %d not found.\n", id);

}
void CountMFinGroup( struct Student students[], int count)
{ 
	int MCount=0;
	int FCount=0;
	for (int i=0; i<count; i++){
		if (strcmp(students[i].sex, "F")==0)
		{
			FCount++;
		}
		else
		{ 
			MCount++; 
		}

	}
	printf("In this group we have %d girls and %d boys. \n", FCount, MCount);
}
int main() {
    struct Student students[5] = {
        {1, "John Doe",'M'},
        {2, "Jane Smith",'F'},
        {3, "Alice Johnson",'F'},
	{4, "Jeffrey Lebowski",'M'},
	{5, "Yana Dyagileva",'F'}
    };
    printStudents(students, 5);
    	int f_count = sizeof(students)/sizeof(students[0]);
    	int searchId;
    	printf("Enter student ID to search: ");
    	scanf("%d", &searchId);
    	findStudentById(students, f_count, searchId);
	CountMFinGroup (students, f_count);
    	return 0;
}
