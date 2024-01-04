[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/-Fh_L3kO)
# Assignment 3

בהגשה זו ישנם שתי תרגילים, הראשון כרגיל יבדק אוטומטית ואילו את השני תצטרכו לממש אבל הוא לא יבדק.

הסבר מפורט על התרגילים מופיע בסרטון 8 של שבוע זה.

## תרגיל 1 - ניהול כיתה

בקובץ [classroom_management](./classroom_managment.py) מוגדרת רשימה של תלמידים בשם `classroom`. בתחתית הקובץ ישנם מספר פונקציות שעליך לממש, אלו פונקציות שמאפשרות גישה ל״מסד הנתונים״ של הכיתה. עלייך לאפשר הוספת תלמיד, שינוי אימייל של תלמיד קייים, מחיקת תלמיד ,קבלת ממוצע הציונים של תלמיד במקצוע מסוים והחזרת רשימה שתכיל את כל המקצועות בהם התלמיד נבחן, ללא כפילויות.

ניתן להניח כי הפרמטרים הנשלחים לפונקציה הינם חוקיים.

טיפ: הגדירי פונקצית עזר שיודעת להחזיר את האינדקס של התלמיד ברשימה עפ״י שמו.

## תרגיל 2 - אפליקצית חידון

עלייך לבנות תוכנה שמקבלת 2 ארגומנטים דרך ה`command line`: שם נושא ומספר שאלות, התוכנה תפתח את קובץ השאלות המתאים לנושא (מתוך הקבצים שנמצאים בתקייה `questions`) ותציג למשתמש את השאלות שמופיעות בו בצורה של שאלות אמריקאיות המשתמש יבחר באחת התשובות בסיום החידון הוא יקבל מידע על כמה שאלות הוא ענה נכון.

שימי לב שהשאלות מופיעות בקבצים בפורמט הבא (כל שורה זה שאלה אחת):

```txt
question ; answer ; option1, option2, option3
...
...
```

יש לממש את הקוד לשאלה זו בקובץ [quiz_app.py](./quiz_app.py).

לאחר המימוש עליך להכנס ל[quiz_app_test.py](./quiz_app_test.py) ולשנות את הערך של המשתנה `is_implemented` ל`True`.

def print_details(lst):
    for _ in range(len(lst)):
        print(f"{lst[_]['name']}\n")

print_details(classroom)

   
    


def delete_student(name):
    i=re_index(classroom, name)
    classroom[i] = ""

delete_student('Charlie')
print_details(classroom)
   # """Delete a student from the classroom"""
 #   pass

