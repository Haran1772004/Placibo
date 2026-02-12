import openpyxl
from django.http import HttpResponse
from .models import FormSubmission  # Use the model we created for Task 1

def export_submissions_to_excel(request):
    # 1. Create a new Workbook
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Form Submissions"

    # 2. Add Header Row
    headers = ['ID', 'User Name', 'File URL', 'Date Submitted']
    sheet.append(headers)

    # 3. Fetch data from the database
    submissions = FormSubmission.objects.all()

    for entry in submissions:
        # Format the date properly
        date_str = entry.submitted_at.strftime('%Y-%m-%d %H:%M') if entry.submitted_at else "N/A"
        
        sheet.append([
            entry.id, 
            entry.user_name, 
            entry.uploaded_file.url if entry.uploaded_file else "No File",
            date_str # Use the actual date field you added to models.py
        ])

    # 4. Prepare the response as an Excel file
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename="submissions.xlsx"'
    
    wb.save(response)
    return response
