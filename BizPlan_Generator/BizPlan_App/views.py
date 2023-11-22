import os
import re
from django.shortcuts import render
from .forms import BusinessPlanForm
from openai import OpenAI
from django.http import HttpResponse
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


def home(request):
    return render(request, 'home.html')

def create_business_plan(request):
    # predefined message for the chatGPT
    system_prompt = """
        Role: System
        Content: You are a Business Plan Generator, skilled in creating comprehensive plans for various industries.
    """
    
    # Retrieve the OpenAI API key from the environment variable
    openai_business_key = os.environ.get('OPENAI_API_KEY')
    
    if not openai_business_key:
        # Handle the case where the API key is not available
        return render(request, 'error.html', {'error_message': 'OpenAI API key not found'})

    # Create an instance of the OpenAI client
    client = OpenAI(api_key=openai_business_key)
    
    if request.method == 'POST':
        form = BusinessPlanForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            business_plan = form.save()

            # Use the new OpenAI API call
            user_input = f"{system_prompt}\n\nUser Input:\n"
            for field_name, field_value in form.cleaned_data.items():
                user_input += f"{field_name.capitalize()}: {field_value}\n"

            # Iterative conversation
            #sections = ["Executive Summary", "Market Analysis", "Specific Requirements", "Goals and Objectives", "Implementation Plan", "Financial Projections"]
            sections = ["Executive Summary", "Company description", "Goals and Objectives", "Organization and Management",
                        "Products and services", "Market analysis", "Sales and marketing", "Financial Projections"]
            generated_plan = []

            for section in sections:
                prompt = f"{user_input}\n\nUser Input:\nGenerate {section} for the business plan in a paragraph format."
                
                business_response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens = 20,
                    temperature = 0.5
                )

                response = business_response.choices[0].message.content
                generated_plan.append({"section": section, "response": response})
                

            context = {'responses': generated_plan}
            return render(request, 'created_business_plan.html', context)
    else:
        form = BusinessPlanForm()

    return render(request, 'form.html', {'form': form})
    
    


def export_to_pdf(request):
    if request.method == 'POST':
        responses = request.POST.get('responses')
        html_content = render_to_string('created_business_plan.html', {'responses': responses})

        # Convert HTML to PDF using ReportLab.
        pdf_buffer = render_html_to_pdf(html_content)

        # Create a Django response with the PDF file.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="business_plan.pdf"'

        # Write the PDF file to the response.
        response.write(pdf_buffer.getvalue())
        return response
    else:
        return HttpResponse('Invalid request method')

def render_html_to_pdf(html_content):
    # Create a buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object using ReportLab.
    pdf = canvas.Canvas(buffer, pagesize=letter)
    
    # Set font and size (optional)
    pdf.setFont("Helvetica", 12)

    # Draw the HTML content on the PDF.
    pdf.drawString(100, 750, "Generated Business Plan PDF")  # Adjust position as needed
    pdf.drawString(100, 730, html_content)  # Adjust position as needed

    # Close the PDF object cleanly, and we're done.
    pdf.showPage()
    pdf.save()

    # File response with the PDF data.
    buffer.seek(0)
    return buffer

    
    
    
    
    # if request.method == 'POST':
    #     form = BusinessPlanForm(request.POST)
    #     if form.is_valid():
    #         # Save form data to the database
    #         business_plan = form.save()

    #         # Use the new OpenAI API call
    #         user_input = f"{system_prompt}\n\nUser Input:\n"
    #         for field_name, field_value in form.cleaned_data.items():
    #             user_input += f"{field_name.capitalize()}: {field_value}\n"

    #         sections = ["Executive Summary", "Company description", "Goals and Objectives", "Organization and management",
    #                     "Products and services", "Market analysis", "Sales and marketing", "Financial Projections"]
    #         generated_plan = []

    #         for section in sections:
    #             prompt = f"{user_input}\n\nUser Input:\nGenerate {section} for the business plan in a paragraph format"

    #             # Set stream=True in the API call
    #             business_response = client.chat.completions.create(
    #                 model="gpt-3.5-turbo",
    #                 messages=[
    #                     {"role": "system", "content": system_prompt},
    #                     {"role": "user", "content": prompt}
    #                 ],
    #                 stream=True  # Set stream parameter to True
    #             )
                
    #             print("Business API Response:", business_response)

    #             # Collect and process streaming responses
    #             response = ""
    #             for chunk in business_response:
    #                 if 'choices' in chunk:
    #                     for choice in chunk.choices:
    #                         if 'delta' in choice and 'content' in choice.delta:
    #                             response += choice.delta.content
    #                         else:
    #                             # Handle the case where the structure of the response is unexpected
    #                             print("Unexpected response structure:", chunk.choices)
    #             print(f"Section: {section}, Response: {response}")   
    #             generated_plan.append({"section": section, "response": response})

    #         context = {'responses': generated_plan}
    #         print("Generated Plan:", generated_plan)
    #         return render(request, 'created_business_plan.html', context)
    # else:
    #     form = BusinessPlanForm()
        

    # return render(request, 'form.html', {'form': form})
