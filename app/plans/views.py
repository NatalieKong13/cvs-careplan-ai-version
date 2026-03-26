import os
import anthropic
from django.shortcuts import render
from .models import CarePlan

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def index(request):
    if request.method == "POST":
        patient_name = request.POST["patient_name"]
        age = request.POST["age"]
        diagnosis = request.POST["diagnosis"]
        medications = request.POST["medications"]
        notes = request.POST.get("notes", "")

        prompt = f"""You are a clinical care coordinator. Generate a detailed care plan for the following patient:

Patient Name: {patient_name}
Age: {age}
Diagnosis: {diagnosis}
Current Medications: {medications}
Additional Notes: {notes}

Please provide a comprehensive care plan including:
1. Short-term goals (next 2 weeks)
2. Long-term goals (3-6 months)
3. Recommended interventions
4. Medication management notes
5. Follow-up schedule
6. Warning signs to watch for
7. Patient education points"""

        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )

        plan_text = message.content[0].text

        care_plan = CarePlan.objects.create(
            patient_name=patient_name,
            age=age,
            diagnosis=diagnosis,
            medications=medications,
            notes=notes,
            generated_plan=plan_text,
        )

        return render(request, "plans/result.html", {"plan": care_plan})

    return render(request, "plans/index.html")
