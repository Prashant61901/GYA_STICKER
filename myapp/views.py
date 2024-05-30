import pandas as pd
from .models import Member
from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file, engine='openpyxl')

            # Filter rows until the first column value is empty
            df = df[df.iloc[:, 0].notna()]

            # Create instances of Member model
            members = []
            for index, row in df.iterrows():
                member = Member(
                    member_id=row.iloc[0],  # Assuming ID is in the first column
                    name=row.iloc[1],  # Assuming Name is in the second column
                    gender=row.iloc[2],  # Assuming Gender is in the third column
                    dob=row.iloc[3],  # Assuming Date of Birth is in the fourth column
                    mobile=row.iloc[4]  # Assuming Mobile Number is in the fifth column
                )
                members.append(member)

            Member.objects.all().delete()
            # Bulk create Member instances
            Member.objects.bulk_create(members)
            data=Member.objects.all()
            return render(request, 'display_data.html',{"data":data})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
